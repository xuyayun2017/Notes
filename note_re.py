# coding=utf-8
'''
   网址1：https://blog.csdn.net/yjj20007665/article/details/52370264

   RE 模块（Regular Expression 正则表达式）提供各种正则表达式的匹配操作，在文本解析、
   复杂字符串分析、信息提取时是一个非常有用的工具。

   使用python的re模块，尽管不能满足所有复杂的匹配情况，但足够在绝大多数情况下能够有效地
   实现对复杂字符串的分析并提取出相关信息。python 会将正则表达式转化为字节码，利用 C 语言的
   匹配引擎进行深度优先的匹配。
     import re
     print re.__doc__
   可以查询re模块的功能信息

    网址2：https://www.cnblogs.com/jiangzhaowei/p/5738590.html
    函数：group（），start(),end(),span()

   廖雪峰的官方网站：
   https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832260566c26442c671fa489ebc6fe85badda25cd000
'''

import re
    # print(re.__doc__)               查询 re 模块的功能信息

'''
1. re 的正则表达式语法：
   语法     意义     说明
   "."     任意字符
   "^"     字符串开始    '^hello'匹配'helloworld'而不匹配'aaaahellobbb'
   "$"     字符串结尾    与上同理
   "*"     0 个或多个字符（贪婪匹配）   <*>匹配<title>chinaunix</title>
   "+"     1 个或多个字符（贪婪匹配）   与上同理
   "?"     0 个或多个字符（贪婪匹配）
   *?, +?, ??   以上三个取第一个匹配结果（非贪婪匹配）   <*>匹配<title>
   {m,n}        对于前一个字符重复m到n次，{m}亦可       a{6}匹配6个a、a{2,4}匹配2到4个a  
   {m,n}?       对于前一个字符重复m到n次，并取尽可能少   aaaaaa’中a{2,4}只会匹配2个
   "\\"         特殊字符转义或者特殊序列
   []           表示一个字符集                          [0-9]、[a-z]、[A-Z]、[^0]
   "|"          或                                      A|B,或运算 
   (...)        匹配括号中任意表达式
   (?#...)      注释，可忽略
   (?=...)      '(?=test)'  在hellotest中匹配hello
   (?!...)      '(?!=test)'  若hello后面不为test，匹配hello
   (?<=...)     '(?<=hello)test'  在hellotest中匹配test
   (?<!...)     '(?<!hello)test'  在hellotest中不匹配test
   
2. 正则表达式特殊序列表如下：
   特殊序列符号    意义
   \A    只在字符串开始进行匹配
   \Z    只在字符串结尾进行匹配
   \b    匹配位于开始或结尾的空字符串
   \B    匹配不位于开始或结尾的空字符串
   \d    相当于[0-9]
   \D    相当于[^0-9]
   \s    匹配任意空白字符:[\t\n\r\r\v]
   \S    匹配任意非空白字符:[^\t\n\r\r\v]
   \w    匹配任意数字和字母:[a-zA-Z0-9]
   \W    匹配任意非数字和字母:[^a-zA-Z0-9]
   
3. re 的主要功能函数
   常用的功能函数包括：compile、search、match、split、findall（finditer）、sub（subn）
   （1）compile  作用：把正则表达式语法转化成正则表达式对象
        flags定义包括：
        re.I：忽略大小写
        re.L：表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
        re.M：多行模式
        re.S：’ . ’并且包括换行符在内的任意字符（注意：’ . ’不包括换行符）
        re.U： 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
        更多用法可以在http://www.devexception.com/sitemap_index.xml上查找
   （2）search  作用：在字符串中查找匹配正则表达式模式的位置，返回MatchObject 的实例，
        如果没有找到匹配的位置，则返回 None。
        re.search(pattern, string[, flags])
        search (string[, pos[, endpos]])
   （3）match  作用：match()函数只在字符串的开始位置尝试匹配正则表达式，，也就是只报告
        从位置 0 开始的匹配情况，而 search() 函数是扫描整个字符串来查找匹配。
        re.match(pattern, string[, flags])
        match(string[, pos[, endpos]])
   (4)split  作用：可以将字符串匹配正则表达式的部分割开并返回一个列表
        re.split(pattern, string[, maxsplit=0, flags=0])
        split(string[, maxsplit=0])
   (5)findall  作用：在字符串中找到正则表达式所匹配的所有子串，并组成一个列表返回
        re.findall(pattern, string[, flags])
        findall(string[, pos[, endpos]])
   (6)findfilter()  作用：和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，
      并组成一个迭代器返回。
        re.finditer(pattern, string[, flags])
        finditer(string[, pos[, endpos]])
   (7)sub()  作用：在字符串 string 中找到匹配正则表达式 pattern 的所有子串，用另一个字符串 repl 进行替换。
      如果没有找到，则返回未被修改的 string。Repl 既可以是一个字符串也可以是一个函数。
        re.sub(pattern, repl, string[, count, flags])
        sub(repl, string[, count=0])
        
   match(),search(),findfilter()如果匹配成功，则返回一个Match Object对象，
   该对象有一下属性、方法：
   (1)group()  作用：返回被 RE 匹配的字符串
   (2)start()  作用：返回匹配开始的位置
   (3)end()    作用：返回匹配结束的位置
   (4)span()   作用：返回一个元祖包含匹配（开始，结束）的位置
'''
# 最基本的用法，通过re.RegexObject对象调用
if __name__ == '__main__':
    print('例 1：match() 与 search():')

    r1 = re.compile(r'world')
    if r1.match('helloworld'):
        print('match succeeds')
    else:
        print('match fails')

    if r1.search('helloworld'):
        print('search succeeds')
    else:
        print('search fails')
'''
   说明一下：r是raw(原始)的意思。因为在表示字符串中有一些转义符，如表示回车'\n'。如果要表示\表需要写为'\\'。
   但如果我就是需要表示一个'\'+'n'，不用r方式要写为:'\\n'。但使用r方式则为r'\n'这样清晰多了。
'''
if __name__ == '__main__':
    print('例 2：search() 设置flag:')
    # r2 = re.compile(r'n$',re.S)
    # r2 = re.compile('\n$',re.S)
    r2 = re.compile('World$',re.I)                   # re.I 忽略大小写
    if r2.search('helloworld\n'):
        print('search succeeds')
    else:
        print('search fails')

    print('例 3：split() 直接调用：')
    if re.search(r'abc',r'helloaaabcdworldn'):
        print('search succeeds')
    else:
        print('search fails')


    print('例 3：split() 简单分析 ip:')
    r1 = re.compile('(\W+)')                                 # '\W'  匹配非[A-Za-z0-9]
    print(r1.split('192.168.1.1'))
    print(re.split('(\W+)','192.168.1.1'))
    print(re.split('(\W+)','192.168.1.1',1))

    print(re.split('(\D+)', '192.168.1.1'))                # '\D'  匹配非数字
    print(re.split('(\d+)', '192.168.1.1'))                # '\d'  匹配数字0-9
if __name__ == '__main__':
    print('例 4：findall() 查找[]包括的内容（贪婪和非贪婪查找）：')
    r1 = re.compile('[.*]')
    print(re.findall(r1,"hello[hi]heldfsdsf[iwonder]lo"))
    r1 = re.compile('[.*?]')
    print(re.findall(r1, "hello[hi]heldfsdsf[iwonder]lo"))
    print(re.findall('[0-9]{2}',"fdskfi1323jfkdj"))                    # {2}  类似于 length
    print(re.findall('([0-9]{2}[a-z]{3})','fdskfi1323jfkdj'))
    print(re.findall('(.*)(?=www)(.*)',"afdsfwwwfkdjfsdfsdwww"))             # ?=www  匹配 www 前面部分
    print(re.findall('(.*)(?<=www)(.*)',"afdsfwwwfkdjfsdfsdwww"))            # ?<= www  匹配 www

'''
   group() 返回 re 整体匹配的字符串，可以一次输入多个组号，对应组号匹配的字符串。
   1.group() 返回 re 整体匹配的字符串
   2.group(n,m) 返回组号为 n 和 m 所匹配的字符串，如果组号不存在，则返回 indexError 异常。
'''
if __name__ == '__main__':
    p = re.compile('(a(b)c)d')
    m = p.match('abcd')
    print(m.group(0))                  # 第 0 组
    print(m.group(1))                  # 第 1 组
    print(m.group(2))                  # 第 2 组
    print(m.group(0,1,2))

'''
   groups() 返回一个包含正则表达式中所有小组字符串的元祖，从 1 到所含的小组好，
   通常 groups() 不需要参数，返回一个元组，元组中的元就是正则表达式中定义的组。
'''
if __name__ == '__main__':
    p = re.compile('(a(b)c)d')
    m = p.match('abcd')
    print(m.groups())
