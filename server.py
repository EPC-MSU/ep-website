import asyncio
import logging
import posixpath
from argparse import ArgumentParser
from textwrap import dedent

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp.web_exceptions import HTTPNotFound
import data.download as download_data
import data.other as other_data
from data.products import product_by_name, products
from filemanager import FileManager
from translator.translator import all_languages, translator

file_manager = FileManager(
    300, "view/static/download", "/static/download"
)  # Download page files


routes = web.RouteTableDef()


def translatable_template(func):
    async def handler(request):
        language = request.match_info.get("language", "ru")
        try:
            tr = translator(language)
        except ValueError:  # No such language
            raise HTTPNotFound()
        result = await func(request)

        # Link to current page without /ru or /en prefix
        current_link_nolang = posixpath.join(*request.path.split("/")[2:])

        # Links to ru, en, ... etc versions of current page
        languages_links = {
            f"{lang}_link": posixpath.join("/" + lang, current_link_nolang)
            for lang in all_languages
        }
        return {"tr": tr, "lang": language, **languages_links, **result}

    return handler


def base_template(func):
    async def handler(request):
        result = await func(request)
        # TODO: clearer names
        return {
            "address": other_data.address,
            "epc": other_data.epc,
            "description": other_data.description,
            "tags": other_data.tags,
            "title": other_data.title,
            **result,
        }

    return translatable_template(handler)


@routes.get("/")
async def index(request):
    raise web.HTTPFound(location="/ru/")  # redirect to default language


@routes.get("/{language}/")
@aiohttp_jinja2.template("index.html")
@base_template
async def index(request):
    # TODO: clearer names
    return {
        "intro": other_data.intro,
        "products": products,
        "technical": other_data.technical,
        "more": other_data.more,
        
        "archive": file_manager.archives.get("USB_ADC"),
        "archive_description": download_data.all_software
    }


@routes.get("/robots.txt")
async def robots(request):
    content = dedent(
        """
    User-Agent: *
    Allow: /"""
    )
    return web.Response(
        body=content,
        headers={
            "Content-Type": "text/plain",
            "Content-Disposition": "attachment",
            "filename": "robots.txt",
        },
    )


@routes.get("/{language}/product/{product}/")
@aiohttp_jinja2.template("download.html")
@base_template
async def download(request):
    product = product_by_name(request.match_info["product"])

    # TODO: clearer names
    return {
        "product": product,
        "all_software": file_manager.files[product.name],
        "archive": file_manager.archives.get(product.name),
        "archive_description": download_data.all_software,
        "version": download_data.version,
        "release_date": download_data.release_date,
        "size": download_data.size,
        "link": download_data.link,
        "download": download_data.download,
        "categories": download_data.categories,
    }


routes.static("/static", "view/static")


def _app_factory() -> web.Application:
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("view/templates"))

    app.router.add_routes(routes)

    return app


async def _server_factory() -> web.TCPSite:
    app = _app_factory()
    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner)
    return site


async def main():
    file_manager.start_refresh()

    http_server_coro = (await _server_factory()).start()
    asyncio.create_task(http_server_coro)


if __name__ == "__main__":
    parser = ArgumentParser("EyePoint server")
    # TODO: robots.txt for unstable version
    parser.add_argument("--debug", help="Run with debug logging", action="store_true")
    if parser.parse_args().debug:
        logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
