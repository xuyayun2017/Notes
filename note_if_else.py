# coding=utf-8
'''
   http://www.runoob.com/python/python-if-statement.html
   Python 条件语句是通过一条或多条语句的执行结果（True 或 False)来决定执行的代码块。'
   Python 指定任何非 0 和非空（null) 值为 True,0 或者 null 为 False.
   基本形式：
   if 判断语句：
      执行语句...
   else:
      执行语句...
'''
if __name__ == '__main__':
    print('例 1：if 基本用法')
    flag = False
    name = 'luren'
    if name == 'python':               # 注意：等于为 ==
        flag = True
        print('Welcome')
    else:
        print(name)

    # python 不支持 switch 语句，所以多个条件判断只能用 elif 来实现。
    print('例 2：elif 用法')
    num = 5
    if num == 3:
        print('boss')
    elif num == 2:
        print('user')
    elif num == 1:
        print('worker')
    elif num < 0:
        print('error')
    else:
        print('random')

    # 如果判断需要多个条件时，可使用 or,and
    print('例 3：if 语句多个条件')
    num = 9
    if num >= 0 and num <= 10:
        print('hello')

    num = 10
    if num < 0 or num > 10:
        print('hello')
    else:
        print('undefine')

    num = 8
    if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
        print('hello')
    else:
        print('undefine')