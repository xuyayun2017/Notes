# coding=utf-8
'''
   http://www.runoob.com/python/python-xml.html
'''
'''
    1.什么是XML?
      XML 指可扩展标记语言（eXtensible Markup Language）。
      XML 被设计用来传输和存储数据。
      XML是一套定义语义标记的规则，这些标记将文档分成许多部件并对这些部件加以标识。
    2.python对XML的解析
      常见的XML编程接口有DOM和SAX，这两种接口处理XML文件的方式不同，当然使用场合也不同。
      python有三种方法解析XML，SAX，DOM，以及ElementTree:
      (1)SAX (simple API for XML )
         python 标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。
      (2)DOM(Document Object Model)
         将XML数据在内存中解析成一个树，通过对树的操作来操作XML。
      (3)ElementTree(元素树)
         ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。
    注：因DOM需要将XML数据映射到内存中的树，一是比较慢，二是比较耗内存，而SAX流式读取XML文件，比较快，占用内存少，但需要用户实现回调函数（handler）。
'''

'''
    python使用SAX解析xml
    SAX是一种基于事件驱动的API。利用SAX解析XML文档牵涉到两个部分:解析器和事件处理器。
    解析器负责读取XML文档,并向事件处理器发送事件,如元素开始跟元素结束事件;
    事件处理器则负责对事件作出相应,对传递的XML数据进行处理。 
'''
import xml.sax
if __name__ == '__main__':
    class MovieHandler(xml.sax.ContentHandler):
        def __init__(self):
            self.CurrentData = ""
            self.type = ""
            self.format = ""
            self.year = ""
            self.rating = ""
            self.stars = ""
            self.description = ""

        # 元素开始事件处理
        def startElement(self, tag, attributes):
            self.CurrentData = tag
            if tag == "movie":
                print("*****Movie*****")
                title = attributes["title"]
                print("Title:", title)

        # 元素结束事件处理
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

        # 内容事件处理
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

            parser = xml.sax.make_parser()

            parser.sestFeature(xml.sax.handler.feature_namespaces,0)

           # 重写 ContextHandler
            Handler = MovieHandler()
            parser.setContenHandler(Handler)

            parser.parse("movies.xml")


'''
    使用xml.dom解析xml
    文件对象模型（Document Object Model，简称DOM），是W3C组织推荐的处理可扩展置标语言的标准编程接口。
    一个 DOM 的解析器在解析一个 XML 文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，之后你可以利用DOM 提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过的内容写入xml文件。 
'''
from xml.dom.minidom import parse
import xml.dom.minidom
if __name__ == '__main__':
    # 使用 minidom 解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse('movies.xml')
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
        print("Root element:%s" % collection.getAttribute("shelf"))     # Root element:New Arrivals

    # 在集合中获取所有电影
    movies = collection.getElementsByTagName("movie")            # movie 标签

    # 打印每部电影的详细信息
    for movie in movies:
        print("*****Movie*****")
        if movie.hasAttribute("title"):
            print("Title:%s" % movie.getAttribute('title'))

        type = movie.getElementsByTagName('type')[0]             # type 标签
        print("Type:%s" % type.childNodes[0].data)               # type 子节点
        format = movie.getElementsByTagName('format')[0]
        print("Format:%s" % format.childNodes[0].data)
        year = movie.getElementsByTagName('year')[0]
        print("Year:%s" % year.childNodes[0].data)
        description = movie.getElementsByTagName('description')[0]
        print("Description:%s" % description.childNodes[0].data)
