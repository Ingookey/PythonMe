# coding: utf-8

import sys
import logging


class RunCmd(object):
    @staticmethod
    def run_shell(cmd=None):
        import subprocess

        logging.debug('input cmd: {}'.format(cmd))
        subprocess.call(cmd, shell=True)
        pass


class SyncCode(object):
    def __init__(self, branch, xml):
        if (branch is not None) and (xml is not None):
            self.branch = branch
            self.xml = xml
            self.code_path = None
            self.code_base = None
            logging.debug('sync code init suc, branch: {}, xml: {}'.format(self.branch, self.xml))
        else:
            logging.debug("branch or xml is null")
        pass

    def set_code_path(self, code_path=None):
        if code_path is not None:
            self.code_path = code_path
        pass

    def set_code_base(self, code_base=None):
        if code_base is not None:
            self.code_base = code_base
        pass

    def sync_code(self):
        import os

        if self.code_path is not None:
            os.chdir(self.code_path)
        if (self.code_base is not None) and (not os.path.exists(self.code_base)):
            os.mkdir(self.code_base)
        os.chdir(self.code_base)
        logging.debug("which path: {}".format(os.getcwd()))

        # sync code
        pass


def parse_xml(file_name, tag_1level, tag_2level):
    import xml.dom.minidom as mnd

    elements = ""
    if file_name:
        dom_tree = mnd.parse(file_name)
        elements = dom_tree.documentElement
    pass
    if elements.hasAttribute(tag_1level):
        logging.debug("tag_1level : {}".format(elements.getAttribute(tag_1level)))
    pass

    for item in elements.getElementsByTagName(tag_2level):
        if item.hasAttribute("title"):
            logging.debug("title: {}".format(item.getAttribute("title")))
        pass
        ele_list = ['type', 'format', 'rating', 'description']
        for item2 in ele_list:
            item_2level = item.getElementsByTagName(item2)[0]
            logging.debug("{}: {}, {}".format(item2, item_2level, item_2level.childNodes[0].data))
        pass
    pass


def parse_json(file_name, find_item=None):
    import json

    branch, xml = "", ""
    with open(file_name, 'r') as fin:
        json_data = json.load(fin)
        logging.debug("json_data: {}".format(json_data))

        for item in json_data:
            logging.debug('item: {}'.format(item))
            if (find_item is not None) and (item == find_item):
                logging.debug('item.value: {}'.format(json_data[item]))
                branch = json_data[item]['branch']
                xml = json_data[item]['xml']
                logging.debug('branch: {}, xml: {}'.format(branch, xml))
                break
            pass
        pass
    pass

    sc = SyncCode(branch, xml)
    sc.set_code_path("$WORKSPACE")
    sc.set_code_base("code_base")
    sc.sync_code()
    pass


def parse_yaml(file_name, find_item=None):
    import yaml

    with open(file_name, 'r') as fin:
        yaml_data = yaml.safe_load(fin)
        logging.debug('yaml_data: {}'.format(yaml_data))

        if find_item is not None:
            dict_data = yaml_data.get(find_item)
            logging.debug('dict_data: {}'.format(dict_data))

            branch = dict_data[0].get('branch')
            xml = dict_data[0].get('xml')
            logging.debug('branch: {}, xml: {}'.format(branch, xml))
            pass
    pass


def inlet():
    if False:
        file_name = "../data/xmlFile.xml"
        parse_xml(file_name, "shelf", "movie")
        pass

    if False:
        file_name = "../data/testJson.json"
        parse_json(file_name, find_item="repo")
        pass

    if True:
        file_name = "../data/config.yaml"
        parse_yaml(file_name, find_item="repo1")
        pass
    sys.exit(0)
