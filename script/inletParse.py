# coding: utf-8


def parse_xml(file_name, tag_1level, tag_2level):
    import xml.dom.minidom as mnd

    elements = ""
    if file_name:
        dom_tree = mnd.parse(file_name)
        elements = dom_tree.documentElement
    pass
    if elements.hasAttribute(tag_1level):
        print("tag_1level : {}".format(elements.getAttribute(tag_1level)))
    pass

    for item in elements.getElementsByTagName(tag_2level):
        if item.hasAttribute("title"):
            print("title: {}".format(item.getAttribute("title")))
        pass
        ele_list = ['type', 'format', 'rating', 'description']
        for item2 in ele_list:
            item_2level = item.getElementsByTagName(item2)[0]
            print("{}: {}, {}".format(item2, item_2level, item_2level.childNodes[0].data))
        pass
    pass


if __name__ == "__main__":
    fileName = "../data/xmlFile.xml"
    parse_xml(fileName, "shelf", "movie")
    pass
