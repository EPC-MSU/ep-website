import asyncio
import logging
import posixpath
from argparse import ArgumentParser
from textwrap import dedent

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp.web_exceptions import HTTPNotFound
import importlib

import site_engine.specification.general as general
from site_engine.specification.product import find_product_by_name
from site_engine.filemanager import FileManager
from site_engine.translator.translator import all_languages, translator

logging.basicConfig(level=logging.DEBUG)
routes = web.RouteTableDef()


def translatable_template(func):
    async def handler(request):
        language = request.match_info.get("language", "ru")
        try:
            tr = translator(args.site, language)
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
            "address": general.address,
            "epc": general.epc,
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
async def index_loc(request):
    # TODO: clearer names
    return {
        "intro": other_data.intro,
        "main_section_title": other_data.main_section_title,
        "products": products,
        "technical": general.technical,
        "more_button": general.more_button,
        "our_partners": general.our_partners
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
    product = find_product_by_name(products, request.match_info["product"])
    language = request.match_info["language"]

    # TODO: clearer names
    return {
        "product": product,
        "all_software": file_manager.files[product.name],
        "latest_releases": file_manager.releases(latest=True, lang=language)[product.name],
        "old_releases": file_manager.releases(latest=False, lang=language)[product.name],
        "archive": file_manager.archives[language][product.name],

        "archive_description": download_data.all_software,
        "categories": download_data.categories,

        # Text labels
        "link": general.link,
        "size": general.size,
        "version": general.version,
        "download": general.download,
        "release_date": general.release_date,
        "older_releases": general.older_releases,
    }





def _app_factory() -> web.Application:
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("site_engine/templates"))

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
    await asyncio.create_task(http_server_coro)


if __name__ == "__main__":

    parser = ArgumentParser("EyePoint server")
    parser.add_argument("--site", type=str, help="Site folder name (e.g. 'usbadc10')",  required=True)
    args = parser.parse_args()

    logging.info(f"Arguments: {args}")

    # Dynamic import modules by site name
    download_data = importlib.import_module(f'sites.{args.site}.data.download')
    other_data = importlib.import_module(f'sites.{args.site}.data.other')
    products_data = importlib.import_module(f'sites.{args.site}.data.products')
    products = getattr(products_data, 'products')

    file_manager = FileManager(600, f"sites/{args.site}/download", "/static/download/")

    routes.static("/web", "site_engine/web")
    routes.static("/static/download", f"sites/{args.site}/download")
    routes.static("/images", f"sites/{args.site}/images")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
