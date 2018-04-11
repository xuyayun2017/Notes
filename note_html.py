# coding=utf-8
'''
    BeautifulSoup:https://blog.csdn.net/lilong117194/article/details/75504962
    四大对象种类:Tag,NavigableString,BeautifulSoup,Comment
'''
from bs4 import BeautifulSoup
from urllib import request

if __name__ == '__main__':
    # 创建 beautifulsoup 对象
    soup = BeautifulSoup(open('./Data/Algeria.html',encoding='utf-8'))
    # 打印 soup 的内容，格式化输出
    # print(soup.prettify())

    # 对于 Tag ,有两个重要的属性：name 和 attrs.
    print(soup.name)                                     # [document]
    print(soup.a.attrs)                                  # {'class': ['tocAlink'], 'href': '#a0002', 'data-bypass': ''}

    # 获取标签内部的文字.它的类型是一个 NavigableString，翻译过来叫 可以操作的字符串
    print('Name:',soup.h1.string)

    # BeautifulSoup 对象表示的是一个文档的全部内容

    # 遍历文档树。 contents 和 children 属性。
    # contents 属性可以将 tag 的子节点以列表的方式输出
    # print(soup.h1.contents)                              # ["Agreement between the Government of the People's Republic of China and the Government of the Democratic and Popular Republic of Algeria concerning Encouragement and Reciprocal Protection of Investments"]

    # children 返回的不是一个 list,不过可以通过遍历获取所有的子节点
if __name__ == '__main__':
    #for child in soup.div.children:
        #print(child)

    # .contents 和 .children 属性仅包含tag的直接子节点
    # .descendants 属性可以对所有tag的子孙节点进行递归循环，和 children类似，我们也需要遍历获取其中的内容。
    #for child in soup.descendants:
        #print(child)

    # 多个内容。.strings和.stripped_strings 属性
    # .strings，获取多个内容，不过需要获取：
    #for string in soup.strings:
        #print(repr(string))

    # 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
    #for string in soup.stripped_strings:
        #print(repr(string))

    '''搜索文档树'''
    # 1. fina_all(name , attrs , recursive , text , **kwargs )
    #    ind_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
    # (1) name 参数可以查找所有名字为 name 的,字符串对象会被自动忽略掉
    # A. 传字符串. 下面的例子查找文档中所有的 <a> 标签
if __name__ == '__main__':
    soup.find_all('a')
    # B. 传正则表达式。Beautiful Soup会通过正则表达式的 match() 来匹配内容。下面的例子找以 h 开头的标签
    import re
    for tag in soup.find_all(re.compile("^h")):
        tag.name
    # C.传列表。如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>
    soup.find_all(["a","p"])
    # D. 传 True.True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
    for tag in soup.find_all(True):
        tag.name
    # E. 传方法。如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 [4] ,
    #    如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
    #    下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:
    def has_class_but_no_id(tag):
        return(tag.has_attr('class') and not tag.has_attr('id'))
    soup.find_all(has_class_but_no_id)

    # (2) keyword 参数。如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索
    #   如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性
    #   如果传入 href 参数,Beautiful Soup会搜索每个的”href”属性
    #
if __name__ == '__main__':
    # print("根据 id 提取：",soup.find_all(id="a0001"))                             # 获取所有正文
    print("根据 href 提取：",soup.find_all(href=re.compile('^/bits')))            # 获取签订国家
    print("根据 class_ 提取：",soup.find_all(class_="legis-article-title"))     # 获取所有的 Article
    print("使用多个指定名字的参数：",soup.find_all(id='a0002',class_="legis-article"))  # 提取 Article1
    print("所有 Article 及其正文：",soup.find_all(class_="legis-article"))          # 从 article1 开始的所有内容

    # (3) text 参数。可以搜搜文档中的字符串内容，text 参数接受 字符串 , 正则表达式 , 列表, True
    print("根据 text 提取：",soup.find_all(text=['Article 1','Article 2']))
    print("根据 text 提取：",soup.find_all(text=re.compile('^Article')))             # 提取所有的 Article i

    # (4) limit 参数。find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢，
    #     如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量。当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
    soup.find_all('a',limit=2)

    # (5) recursive 参数。调用tag的 find_all() 方法时,Beautiful Soup会检索当前的所有子孙节点,
    #     如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
    soup.html.find_all("a", recursive=False)

    # 2. find( name , attrs , recursive , text , **kwargs )
    #   它与 find_all() 方法唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果
    # 3. find_parents() find_parent()
    #   find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等. find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容
    #4. find_next_siblings() find_next_sibling()
    #   这2个方法通过 .next_siblings 属性对当 tag 的所有后面解析的兄弟 tag 节点进行迭代, find_next_siblings() 方法返回所有符合条件的后面的兄弟节点,find_next_sibling() 只返回符合条件的后面的第一个tag节点
    #5. find_previous_siblings() find_previous_sibling()
    #   这2个方法通过 .previous_siblings 属性对当前 tag 的前面解析的兄弟 tag 节点进行迭代, find_previous_siblings() 方法返回所有符合条件的前面的兄弟节点, find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点
    #6. find_all_next() find_next()
    #   这2个方法通过 .next_elements 属性对当前 tag 的之后的 tag 和字符串进行迭代, find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点
    #7. find_all_previous() 和 find_previous()
    #   这2个方法通过 .previous_elements 属性对当前节点前面的 和字符串进行迭代, find_all_previous() 方法返回所有符合条件的节点, find_previous()方法返回第一个符合条件的节点

    '''CSS选择器:标签名不加任何修饰，类名前加点，id名前加 #,用到的方法是 soup.select()，返回类型是 list'''
if __name__ == '__main__':
    #1. 通过标签名查找
    print('通过标签名查找：',soup.select('h1'))                        # 协定名称
    #2. 通过类名查找
    docinfo = soup.select('.docinfoblock-item')
    print('通过类名查找：',docinfo[0])       # 所有的 Article

    #3. 通过 id 查找
    #print('通过 id 查找：',soup.select('#a0001'))                      # 所有正文
    #4. 组合查找
    #print('组合查找：',soup.select('td .text70'))
    #5. 直接子标签查找
    print('直接子标签查找:',soup.select('div > div > div'))
    #6. 属性查找
    #   查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和属于同一节点，所以中间不能加空格，否则会无法匹配到。
    print('属性查找：',soup.select('a[href="/bits?jurisdiction=China"]'))
