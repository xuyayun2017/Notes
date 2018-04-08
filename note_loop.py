# coding=utf-8
'''
   http://www.runoob.com/python/python-loops.html
   循环语句 允许我们执行一个语句或语句组多次
'''
'''
   循环类型     描述
   while循环    在给定的判断条件为 true 时执行循环体，否则退出循环体
   for循环      重复执行语句
   嵌套循环     可以在 while 循环体中嵌套 for 循环
'''
'''
   循环控制语句：可以更改语句执行的顺序。
   控制语句     描述
   break语句    在语句执行过程中终止循环，并且跳出这个循环
   continue语句 在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
   pass语句     pass是空语句，是为了保持程序结构的完整性
'''

if __name__ == '__main__':
    '''
      1.while 语句。基本形式：
        while 判断条件：
              执行语句...
    '''
    print('例 1：while语句')
    numbers = [12,37,5,42,8,3]
    even = []
    odd = []
    while len(numbers) > 0:
        number = numbers.pop()            # 弹出一个数
        if(number % 2 == 0):              # 余数为 0
            even.append(number)
        else:
            odd.append(number)
    print("偶数：",even)
    print("奇数：",odd)

    print('例 2：')
    count = 0
    while(count < 9):
        print("The count is:",count)
        count = count + 1

    # while 语句还有另外两个重要的命令 continue,break 来跳过循环。
    # continue 用于跳过该次循环，break 则是用于退出循环
    # 此外“判断条件”还可以是个常值，表示循环必定成立
    print('例 3:continue 和 break 用法')
    i = 1
    while i < 10:
        i += 1
        if i%2 >0:           # 非偶数时跳出
            continue
        print(i)             # 是偶数时，输出。输出双数2、4、6、8、10

    i = 1
    while 1:
        print(i)
        i += 1
        if i > 10:
            break           # 当 i > 10 时跳出循环

    print('例 4：无限循环')
    var = 1
    #while var == 1:        # 该条件永远为true，循环将无限执行下去。可以使用 CTRL+C 来中断循环。
        #num = input("Enter a number:")
        #print("You entered:",num)

    print('例 5：while...else。在循环条件为 false 时执行 else 语句')
    count = 0
    while count < 5:
        print(count," is less than 5")
        count += 1
    else:
        print(count," is not less than 5")

    '''
      2.for 语句。基本形式：
        for iterating_var in sequence:
            statements(s)
    '''
if __name__ == '__main__':
    print('例 1：for 循环')
    for letter in 'Python':
        print('当前字母：',letter)

    fruits = ['banana','apple','mango']
    for fruit in fruits:
        print('当前水果：',fruit)

    # 使用索引。 下面使用了内置函数 len() 和 range()。
    # len（）返回列表的长度，即元素个数。range() 返回一个序列的数。
    print('例 2：for 通过序列索引迭代')
    fruits = ['banana','apple','mango']
    for index in range(len(fruits)):
        print("当前水果：",fruits[index])

    # for...else表示这样的意思：for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完的情况下执行。
    print('例 3：for...else 判断是否为质数')
    for num in range(10,20):                                # 迭代 10 到 20 之间的数字
        for i in range(2,num):                              # 根据因子迭代
            if num%i == 0:                                   # 确定第一个因子
                j = num/i                                    # 计算第二个因子
                print('%d 等于 %d * %d' % (num,i,j))
                break                                       # 跳出当前循环，可以不写
            else:
                print(num," 是一个质数")

    '''
      3.循环嵌套：Python 语言允许在一个循环体里面嵌入另一个循环。
      （1）Python for 循环嵌套语法;
           for iterating_var in sequence:
               for interating_var in sequence:
                   satements(s)
                statements(s)
      （2）Python while 循环嵌套语法：
           while expression:
              while expression:
                 statements(s)
              statement(s)
      （3）还可以在循环体内嵌入其他的循环体，如 while 中嵌入 for, for 中嵌入 while
    '''
if __name__ == '__main__':
    print('例 1：使用嵌套循环输出 2-100 之间的素数')
    i = 2
    while(i < 100):
        j = 2
        while(j <= (i/j)):                # or j <= i
            if not(i%j):break            # 不能整除，则跳出循环
            j = j +1
        if(j > (i/j)):print(i," 是素数")
        i = i + 1