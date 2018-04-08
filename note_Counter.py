# coding=utf-8
'''
   《Python collections中的Counter作用以及源码分析》
   collections — High-performance container datatypes
   网址： https://blog.csdn.net/Shiroh_ms08/article/details/52653385
'''

'''
   该模块实现了专用的容器数据类型来替代python的通用内置容器：
   dict（字典），list（列表）， set（集合）和tuple（元组）。
   
   容器    描述    
   namedtuple()    使用工厂方法创建带有命名的字段的元组的子类
   deque           类似列表的容器，能够快速响应在任何一端进行pop
   Counter         字典子类，为可以进行哈希的对象计数
   OrderedDict     字典子类，记录了字典的添加次序
   defaultdict     字典子类，调用一个工厂方法来提供缺失的值
   
   除了具体的容器类，collections模块还提供了abstract_base_classes来测试一个类是否体用了
   一个特定的接口，例如，这是可哈希的还是一个映射
'''

'''
   Counter   counter工具用于支持便捷和快速地计数
'''
from collections import Counter
if __name__ == '__main__':
    print('例 1：Counter() 计数：')
    cnt = Counter()
    for word in ['red','blue','red','green','blue','blue']:      # word 相当于参数 x
        cnt[word] +=1
    print(cnt)                                                       # 输出：Counter({'blue': 3, 'red': 2, 'green': 1})
