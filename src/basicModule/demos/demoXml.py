# coding: utf-8
''' In SAX
import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if (__name__ == "__main__"):
    parser = xml.sax.make_parser()   # 创建一个 XMLReader
    parser.setFeature(xml.sax.handler.feature_namespaces,
                      0)  # turn off namepsaces

    # 重写ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("../config/testxml.xml")
'''

# In DOM
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("../config/testxml.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root elements : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))
        pass
    types = movie.getElementsByTagName('type')[0]
    print("Type: %s" % types.childNodes[0].data)
    formats = movie.getElementsByTagName('format')[0]
    print("Format: %s" % formats.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print("Rating: %s" % rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print("Description: %s" % description.childNodes[0].data)
    pass