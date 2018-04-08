# coding=utf-8
'''
   http://www.runoob.com/python/python-numbers.html
'''
'''
   1.Number 数据类型用于存储数值。不允许改变。
   （1）python支持四种不同的数值类型：
     int(整型)——通常被称为是整型或整数，是正或负整数，不带小数点。
     long integers(长整型)——无限大小的整数，整数最后是一个大写或小写的L。
     floating point real values(浮点型)——浮点型由整数部分与小数部分组成。
     complex numbers(负数)——复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
   （2）Python Number 类型转换
      int(x [,base ])         将x转换为一个整数  
      long(x [,base ])        将x转换为一个长整数  
      float(x )               将x转换到一个浮点数  
      complex(real [,imag ])  创建一个复数  
      str(x )                 将对象 x 转换为字符串 
      repr(x )                将对象 x 转换为表达式字符串  
      eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
      tuple(s )               将序列 s 转换为一个元组  
      list(s )                将序列 s 转换为一个列表  
      chr(x )                 将一个整数转换为一个字符  
      unichr(x )              将一个整数转换为Unicode字符  
      ord(x )                 将一个字符转换为它的整数值  
      hex(x )                 将一个整数转换为一个十六进制字符串  
      oct(x )                 将一个整数转换为一个八进制字符串  repr(x )                将对象 x 转换为表达式字符串  
   （3）Python math 模块、cmath 模块 
        Python math 模块提供了许多对浮点数的数学运算函数。Python cmath 模块包含了一些用于复数运算的函数。
        import math
        dir(math)   查看 math 查看包中的内容.
   （4）Python数学函数
        函数    返回值
        abs(x)	  返回数字的绝对值，如abs(-10) 返回 10
        ceil(x) 	返回数字的上入整数，如math.ceil(4.1) 返回 5
        cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
        exp(x) 	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
        fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
        floor(x) 	返回数字的下舍整数，如math.floor(4.9)返回 4
        log(x) 	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
        log10(x) 	返回以10为基数的x的对数，如math.log10(100)返回 2.0
        max(x1, x2,...) 	返回给定参数的最大值，参数可以为序列。
        min(x1, x2,...) 	返回给定参数的最小值，参数可以为序列。
        modf(x) 	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
        pow(x, y)	x**y 运算后的值。
        round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
        sqrt(x) 	返回数字x的平方根
'''
if __name__ == '__main__':
    var = 1                 # 在变量赋值时 Number 对象将被创建
    del var                 # 删除对象

'''
    2.Python 字符串。
    (1)Python转义字符:
    转义字符    描述
    \(在行尾时) 	续行符
    \\ 	反斜杠符号
    \' 	单引号
    \" 	双引号
    \a 	响铃
    \b 	退格(Backspace)
    \e 	转义
    \000 	空
    \n 	换行
    \v 	纵向制表符
    \t 	横向制表符
    \r 	回车
    \f 	换页
    \oyy 	八进制数，yy代表的字符，例如：\o12代表换行
    \other 	其它的字符以普通格式输出
    
    (2)Python字符串运算符。下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：
    操作符     描述      实例
    +	    字符串连接	    >>>a + b    'HelloPython'
    *	    重复输出字符串	    >>>a * 2    'HelloHello'
    []	    通过索引获取字符串中字符	    >>>a[1]     'e'
    [ : ]	    截取字符串中的一部分	    >>>a[1:4]   'ell'
    in	    成员运算符 - 如果字符串中包含给定的字符返回 True 	>>>"H" in a     True
    not in 	成员运算符 - 如果字符串中不包含给定的字符返回 True 	    >>>"M" not in a True
    r/R	    原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	>>>print r'\n'  \n
    %	    格式字符串   	请看下一章节
    
    (3) python 字符串格式化符号：
    符号      描述
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
'''
if __name__ == '__main__':
    # 创建字符串很简单，只要为变量分配一个值即可。
    var1 = 'Hello World!'
    var2 = "Python Runoob"

    # Python不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
    # Python访问子字符串，可以使用方括号来截取字符串.
    print("var1[0]:",var1[0])                            # var1[0]: H
    print("var2[1:5]:",var2[1:5])                        # var2[1:5]: ytho

    # Python字符串更新
    print("更新字符串：",var1[:6] + 'Runoob!')          # 更新字符串： Hello Runoob!

    print('例：字符串运算')
    a = 'Hello'
    b = 'Python'
    print('a + b:',a + b)
    print('a * 2:',a * 2)                 # a * 2: HelloHello
    print('a[1]:',a[1])                   # a[1]: e
    print('a[1:4]:',a[1:4])               # a[1:4]: ell

    if('H' in a):
        print('H 在变量 a 中')
    else:
        print('H 不在变量 a 中')

    print(r'\n')
    print(R'\n')

    print("字符串格式化-My name is %s and weight is %d kg." % ('Zara',21))

'''
    3.Python 列表(List).序列中的每个元素都分配一个数字- 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
      Python有6个序列的内置类型，但最常见的是列表和元组。序列都可以进行的操作包括索引，切片，加，乘，检查成员。
    (1) 列表函数
        	cmp(list1, list2)  比较两个列表的元素
        	len(list)          列表元素个数
        	max(list)          返回列表元素最大值
        	min(list)          返回列表元素最小值
        	list(seq)          将元组转换为列表
    (2) 列表方法
           list.append(obj)   在列表末尾添加新的对象
           list.count(obj)    统计某个元素在列表中出现的次数
           list.extend(seq)   在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
           list.index(obj)    从列表中找出某个值第一个匹配项的索引位置
           list.insert(index, obj)  将对象插入列表
           list.pop(obj=list[-1])   移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
           list.remove(obj)         移除列表中某个值的第一个匹配项
           list.reverse()           反向列表中的元素
           list.sort([func])        对原；列表进行排序   
'''
if __name__ == '__main__':
    # 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。
    list1 = ['physics','chemistry',1997,2000]
    list2 = [1,2,3,4,5,6,7]
    list3 = ["a","b","c","d"]

    # 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
    print("下标索引访问-list1[0]:",list1[0])
    print("倒数第二个-list1[-2]:",list1[-2])
    print("截取字符访问-list2[1:5]:",list2[1:5])

    # 修改、更新列表，或使用append()方法来添加列表项
    list = []                # 空列表
    list.append('Google')
    list.append('Runoob')
    print("List:",list)

    # 删除
    list1 = ['physics', 'chemistry', 1997, 2000]
    del(list1[2])
    print("After deleting value at index 2:",list1)

'''
    4.Python 元组。
      Python的元组与列表类似，不同之处在于元组的元素不能修改。
      元组使用小括号，列表使用方括号。
'''
if __name__ == '__main__':
    # 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
    tup1 = ('physics','chemistry',1997,2002)
    tup2 = (1,2,3,4,5,6,7)
    tup3 = "a","b","c","d"              # 任意无符号的对象，以逗号隔开，默认为元组
    tup4 = ()                            # 创建空元组
    tup5 = (50,)                         # 元组中只包含一个元素时，需要在元素后面加逗号

    # 访问元组
    print("下标索引访问元组-tup1[0]:",tup1[0])
    print("截取元组-tup2[1:5]:",tup2[1:5])

    # 修改元组
    tup1 = (12,34,56)
    tup2 = ('abc','xyz')
    tup3 = tup1 + tup2

    # 删除元组。元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组。
    del tup3
    #print("After deleting tup:",tup3)    # 输出变量会有异常信息:NameError: name 'tup3' is not defined

    # 任意无符号的对象，以逗号隔开，默认为元组
    print('abc',-2.34,45,'xyz')
    x,y = 1,2
    print("Value of x,y:",x,y)

'''
    5.Python 字典(Dictionary).字典是另一种可变容器模型，且可存储任意类型对象。
      格式：d = {key1 : value1, key2 : value2 }
      键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
      值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
'''
if __name__ == '__main__':
    # 创建字典
    dict = {'a':1,'b':2,'b':3}
    print("Dict:",dict)

    # 访问字典里的值——根据键值
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print("dict['Name']:",dict['Name'])

    # 修改、添加、删除
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    dict['Age'] = 8                                          # 修改
    dict['School'] = "DPS School"                          # 添加
    del dict['Name']                                        # 删除键是’Name'的条目
    del dict                                                 # 删除字典
'''
    6.Python 日期和时间。Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
      时间间隔是以秒为单位的浮点小数。每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
      python中时间日期格式化符号：
      %y 两位数的年份表示（00-99）;%Y 四位数的年份表示（000-9999）;%m 月份（01-12）;
      %d 月内中的一天（0-31）;%H 24小时制小时数（0-23）;%I 12小时制小时数（01-12）;
      %M 分钟数（00=59）;%S 秒（00-59）;%a 本地简化星期名称;%A 本地完整星期名称;
      %b 本地简化的月份名称;%B 本地完整的月份名称;%c 本地相应的日期表示和时间表示;
      %j 年内的一天（001-366）;%p 本地A.M.或P.M.的等价符;%U 一年中的星期数（00-53）星期天为星期的开始;
      %w 星期（0-6），星期天为星期的开始;%W 一年中的星期数（00-53）星期一为星期的开始;
      %x 本地相应的日期表示;%X 本地相应的时间表示;%Z 当前时区的名称.
'''
if __name__ == '__main__':
    # 函数time.time()用于获取当前时间戳
    import time                               # 引入 time 模块
    ticks = time.time()
    print("当前时间戳为：",ticks)             # 当前时间戳为： 1523011806.13482

    # 从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如 time.localtime() 之类的函数。
    localtime = time.localtime(time.time())
    print("本地时间为：",localtime)           # 本地时间为： time.struct_time(tm_year=2018, tm_mon=4, tm_mday=6, tm_hour=18, tm_min=50, tm_sec=6, tm_wday=4, tm_yday=96, tm_isdst=0)

    # 获取格式化的时间——time.asctime()
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为：",localtime)          # 本地时间为： Fri Apr  6 19:08:28 2018

    # 格式化日期——time.strftime(format[, t])
    print(time.strftime("%Y-%m-%d %H:%M:%S"),time.localtime())  # 2018-04-06 19:08:28
    print(time.strftime("%a %b %H:%M:%S %Y",time.localtime()))  # Fri Apr 19:08:28 2018
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))) # 1459175064.0

    # 获取每月日历
    # Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
    import calendar
if __name__ == '__main__':
    cal = calendar.month(2016,1)
    print("输出2016年1月份的日历：",cal)