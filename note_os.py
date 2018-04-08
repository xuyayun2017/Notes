# coding=utf-8
'''
   http://www.iplaypy.com/module/os.html

   OS 模块简单来说是一个Python的系统编程的操作模块，可以处理文件和目录等。
'''

import os
# help(os)  查看 os 模块帮助文档，有详细的模块相关函数和使用方法

'''
   os.path.dirname(__file__)  获取当前文件的所在路径
   print (os.path.dirname(os.path.dirname(__file__))) 获取当前文件的所在目录的上级路径
   print (os.path.dirname(os.path.dirname(os.path.dirname(__file__))))  获取当前文件的所在目录的上级目录的上级路径
'''

'''
OS 模块重要函数和变量：
   os.sep        更改操作系统中的路径分隔符
   os.getwd()    获取当前路径
   os.listdir()  列出当前目录下所有文件和文件夹
   os.remove()   删除指定文件
   os.system()   用来运行 shell 命令.例：os.system("echo 'hello world!'")
   os.chdir()    改变当前目录，到指定目录中
   os.rmdir()    删除指定目录
   os.mkdir()    创建目录
   os.name()     判断现在正在实用的平台，Windows 返回 ‘nt‘; Linux 返回’posix‘
   
   os.path.isfile()  判断指定对象是否为文件。是返回True,否则False
   os.path.isdir()   判断指定对象是否为目录。是True,否则False
   os.path.exists()  检验指定的对象是否存在。是True,否则False
   os.path.split()   返回路径的目录和文件名
   os.path.getsize() 获得文件的大小，如果为目录，返回0
   os.path.abspath() 获得绝对路径
   os.path.join(path,name)  连接目录和文件名
   os.path.basename(path)   返回文件名
   os.path.dirname(path)    返回文件路径
   os.getcwd()              获得当前工作的目录（get current work dir)
   
'''

'''
OS 模块函数作用详解：
   1. os.system函数可以运行shello命令，Linux系统中就是终端模拟器中的命令。
      也有一些函数可以执行外部程序，包括execv，它会退出Python解释器，并且将控制权交给被执行的程序。
   2. os.sep变量主要用于系统路径中的分隔符。
      Windows系统通过是“\\”，Linux类系统如Ubuntu的分隔符是“/”，而苹果Mac OS系统中是“:”。
'''