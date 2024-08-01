# https://ximc.ru/issues/97738

import logging
import os

from lxml import etree

# platforms:
# cubian: .7z
# firmware 8smc4: hw2.2.x.cod
# firmware 8smc5: hw2.3.x.cod
# Labview 12.0:   Labview_12.0.7z
# Labview 11.0:   Labview_11.0.7z
# Labview 8.6.7:  Labview_8.6.7z
# Libximc:        .tar.gz
# Microsmc:       .zip
# Revealer JAVA:  j.jar
# Revealer LIN32: lin32.tar.gz
# Revealer LIN64: lin64.tar.gz
# Revealer WIN:   win.zip
# Revealer MAC:   mac.zip
# Xilab WIN:      .exe
# Xilab DEB64:    amd64.deb
# Xilab DEB32:    i386.deb
# Xilab RPM64:    x86_64.rpm
# Xilab RPM32:    i586.rpm
# Xilab MACOSX:   osx64.tar.gz


def _filter_firmware(walk_files):
    firmwares = {}
    product, soft_dict = next(iter(walk_files.items()))
    for soft_name, files_list in soft_dict.items():
        for file in files_list:
            if file.basename.endswith('.cod'):
                major, minor, release = file.version.version

                if soft_name not in firmwares.keys():
                    firmwares[soft_name] = {}

                if major not in firmwares[soft_name].keys():
                    firmwares[soft_name][major] = {}

                if minor not in firmwares[soft_name][major].keys():
                    firmwares[soft_name][major][minor] = {}

                if release not in firmwares[soft_name][major][minor].keys():
                    firmwares[soft_name][major][minor][release] = [file]
                else:
                    firmwares[soft_name][major][minor][release].append(file)
    return firmwares


def _reformat_structure():
    pass


def _check_possibility_to_create_products_xml(walk_files):
    if len(walk_files.keys()) == 0:
        logging.error('Empty products files dict')
        return False
    if len(walk_files.keys()) > 1:
        logging.info('Unable to generate products.xml: Found firmwares for more then one product')
        return False

    return True


class XMLGeneratorError(Exception):
    pass


def _xml_simple_generator(simple_etree, simple_files):
    majors = list(simple_files.keys())
    majors.sort(reverse=True)

    for major in majors:
        major_etree = etree.Element("major", version=str(major))
        simple_etree.append(major_etree)

        minors = list(simple_files[major].keys())
        minors.sort(reverse=True)

        for minor in minors:
            minor_etree = etree.Element("minor", version=str(minor))
            major_etree.append(minor_etree)

            releases = list(simple_files[major][minor].keys())
            releases.sort(reverse=True)

            for release in releases:
                release_etree = etree.Element("release", version=str(release))
                minor_etree.append(release_etree)

                for file in simple_files[major][minor][release]:

                    def _write_file(etree_element):
                        sha_etree = etree.Element("sha1")
                        sha_etree.text = file.sha1
                        etree_element.append(sha_etree)

                        utc_time_etree = etree.Element("utc")
                        utc_time_etree.text = file.utc_time
                        etree_element.append(utc_time_etree)

                        # Domain independent link, {{ domain }} will replace in server.py to actual domain
                        url_etree = etree.Element("url")
                        url_etree.text = '{{ domain }}' + file.link
                        etree_element.append(url_etree)

                    platform_etree = etree.Element(file.platform)
                    release_etree.append(platform_etree)
                    _write_file(platform_etree)


def _xml_generator(out_name, files_parsers):
    xml_out = open(out_name, "w")
    xml_out.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n')
    master = etree.Element("root")

    for dir_name in files_parsers.keys():
        etree_obj = etree.Element(dir_name)

        logging.info("XML Generate {0}".format(dir_name))
        master.append(etree_obj)

        _xml_simple_generator(simple_etree=etree_obj, simple_files=files_parsers[dir_name])

    xml_out.write(etree.tostring(master, pretty_print=True).decode("utf-8"))
    xml_out.close()
    logging.info("products.xml  generation OK")


def generate_products_xml(walk_files):
    out_name = 'products.xml'
    if os.path.exists(out_name):
        os.remove(out_name)

    if not _check_possibility_to_create_products_xml(walk_files):
        return
    logging.info('Regenerate products.xml started...')

    firmwares = _filter_firmware(walk_files)

    _xml_generator(out_name, firmwares)
