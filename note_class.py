# coding=utf-8
'''
    Python 面向对象:http://www.runoob.com/python/python-object.html
    Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。

'''
'''
    1.面向对象技术简介
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    类变量：   类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员： 类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
    方法重写： 如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    实例变量： 定义在方法中的变量，只作用于当前实例的类。
    继承：     即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：   创建一个类的实例，类的具体对象。
    方法：     类中定义的函数。
    对象：     通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
    使用 class 语句来创建一个新类，class 之后的名称以冒号结尾:
    class ClassName:
        '类的帮助信息'        # ClassName.__doc__
         class_suite          # class_suite 由类成员，方法，数据属性组成。
'''
if __name__ == '__main__':
    print('例 1：创建类、实例化、属性')
    class Employee:
        '所有员工的基类'
        empCount = 0                     # empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。

        # 第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法。
        # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        def __init__(self,name,salary):
            self.name = name
            self.salary = salary
            Employee.empCount += 1

        def displayCount(self):
            print("Total Employee %d" % Employee.empCount)

        def displayEmployee(self):
            print("Name:",self.name,", Salary:",self.salary)

    # 以下使用类的名称 Employee 来实例化，并通过 __init__ 方法接收函数。
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni", 5000)
    # 访问属性。可以使用点号 . 来访问对象的属性。使用如下类的名称访问类变量：
    emp1.displayEmployee()
    emp2.displayEmployee()
    print("Total Employee %d" % Employee.empCount)

    # 添加、修改、删除类的属性
    emp1.age = 7                      # 添加一个 age 属性
    emp1.age = 8                      # 修改 age 属性
    del emp1.age                      # 删除 age 属性

    # 访问属性
    hasattr(emp1,'age')               # 如果存在 age 属性，返回 True
    getattr(emp1,'name')              # 返回 name属性的值
    setattr(emp1,'age',8)             # 添加属性 age,值为 8
    delattr(emp1,'age')               # 删除属性 age

    # Python 内置属性
    print("Employee.__doc__:",Employee.__doc__)         # 类的文档字符串
    print("Employee.__name__:",Employee.__name__)       # 类名
    print("Employee.__module__:",Employee.__module__)   # 类定义所在的模块
    print("Employee.__bases__:",Employee.__bases__)     # 类的所有父类构成元素（包含了一个由所有父类组成的元组）
    print("Employee.__dict__:",Employee.__dict__)       # 类的属性（包含一个字典，由类的数据属性组成）


    print('例 2：self 的含义')
    # self 代表类的实例，而非类
    # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称，按照惯例它的名称是 self.
    class Test:
        def prt(self):
            print(self)                  # self 代表的是类的实例，代表当前对象的地址:<__main__.Test object at 0x059E5170>
            print(self.__class__)        # self.class 则指向类:<class '__main__.Test'>
    t = Test()
    t.prt()
    # self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
    class Test2:
        def prt(runoob):
            print(runoob)               # <__main__.Test object at 0x053453D0>
            print(runoob.__class__)     # <class '__main__.Test'>
    t = Test()
    t.prt()

    # 对象销毁。
    # Python 使用了引用计数这一简单技术来跟踪和回收垃圾。在 Python 内部记录着所有使用中的对象各有多少引用。
    # 一个内部跟踪变量，称为一个引用计数器。当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。
    # 但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。
    print('例 3：Python 对象销毁（垃圾回收）')
    a = 40              # 创建对象 <40>
    b = a               # 增加引用，<40> 的计数
    c = b               # 增加引用，<40> 的计数

    del a               # 减少引用 <40> 的计数
    b = 100             # 减少引用 <40> 的计数
    c = -1           # 减少引用 <40> 的计数

    # 垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环引用的情况。
    # 循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。这种情况下，仅使用引用计数是不够的。
    # Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。作为引用计数的补充， 垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。 在这种情况下， 解释器会暂停下来， 试图清理所有未引用的循环。
if __name__ == '__main__':
    print('例 4：析构函数 __del__')
    # __del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行。
    class Point:
        def __init__(self,x=0,y=0):
            self.x = x
            self.y = y
        def __del__(self):
            class_name = self.__class__.__name__           # 类名
            print(class_name,'销毁')                       # Point 销毁

    pt1 = Point()
    pt2 = pt1
    pt3 = pt1
    print(id(pt1),id(pt2),id(pt3))                         # 打印对象的 id：93852240 93852240 93852240
    del pt1                                                # 执行析构函数 __del__
    del pt2
    del pt3

    # 类的继承。
    # 面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的类型和子类型关系。
    # 需要注意的地方：继承语法 class 派生类名（基类名）：//... 基类名写在括号里，基本类是在类定义的时候，在元组之中指明的。
    # 在python中继承中的一些特点：
    #     1.在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
    #     2.在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别在于类中调用普通函数时并不需要带上self参数
    #     3.Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
    # 如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
    # 语法：派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：
    # class SubClassName (ParentClass1[, ParentClass2, ...]):
    #      'Optional class documentation string'
    #       class_suite
if __name__ == '__main__':
    print('例 5:类的继承')
    class Parent:                              # 定义父类
        parentAttr = 100
        def __init__(self):
            print("调用父类构造函数")

        def parentMethod(self):
            print("调用父类方法")

        def setAttr(self,attr):
            Parent.parentAttr = attr

        def getAttr(self):
            print("父类属性：",Parent.parentAttr)

    class Child(Parent):                      # 定义子类
        def __init__(self):
            print("调用子类构造方法")

        def childMethod(self):
            print("调用子类方法")

    c = Child()                # 实例化子类
    c.childMethod()            # 调用子类方法
    c.parentMethod()           # 调用父类方法
    c.setAttr(200)             # 再次调用父类的方法 - 设置属性值
    c.getAttr()                # 再次调用父类的方法 - 获取属性值

    # 方法重写。
    # 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：
if __name__ == '__main__':
    print('例 6：方法重写')
    class Parent:
        def myMethod(self):
            print('调用父类的方法')

    class Child(Parent):
        def myMethod(self):
            print('调用子类方法')

    c = Child()                              # 子类实例
    c.myMethod()                             # 子类调用重写方法

    print('例 7：运算符重载')
    class Vector:
        def __init__(self,a,b):
            self.a = a
            self.b = b

        def __str__(self):
            return('Vector(%d, %d)' % (self.a,self.b))

        def __add__(self,other):
            return(Vector(self.a +other.a,self.b + other.b))

    v1 = Vector(2,10)                          # 实例化
    v2 = Vector(5,-2)
    v3 = Vector(1,1)
    print(v1 + v2 + v3)

    # 类的私有属性
    # __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
    # 在类内部的方法中使用时 self.__private_attrs。
    # 类的私有方法
    # __private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用
    # 在类的内部调用 self.__private_methods
if __name__ == '__main__':
    print('例 8：类的私有属性、方法')
    class JustCounter:
        __secretCount = 0         # 私有变量
        publicCount = 0           # 公开变量

        def count(self):
            self.__secretCount += 1
            self.publicCount += 1
            print(self.__secretCount)

    counter = JustCounter()        # 实例化
    counter.count()                # 调用方法 1 次，自增 1
    counter.count()                # 调用方法 2 次，再自增 1
    print(counter.publicCount)
    print(counter.__secretCount)  # 报错，实例不能访问私有变量