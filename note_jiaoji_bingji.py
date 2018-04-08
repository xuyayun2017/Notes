# coding=utf-8
'''
   Python 集合set()添加删除、交集、并集、集合操作:http://www.iplaypy.com/jichu/set.html
   python set() 集合操作符号、数学符号：
   差集：a - b
   交集：a & b
   并集; a | b
   不等于： a != b
   等于： a == b
   属于： a in b
   不属于： a not in b
'''
if __name__ == '__main__':
    s1 = set([1,2,3,4,5,'free_','ree_t','ee_tr'])
    s2 = set([4,5,6,7,8,'ee_tr','e_tra','_trad','trade'])
    # 方法一
    print("交集：",s1&s2)
    print("并集：",s1|s2)
    # 方法二
    s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s2 = [2, 5, 8, 11, 0]
    difference = [v for v in s1 if v not in s2]
    print("差集：",difference)
    union = s2.extend([v for v in s1])
    print(union)
    intersection0 = [v for v in s1 if v in s2]
    print(intersection0)

    # python 集合的添加有两种常用方法，分别是 add 和 update
    a = set('boy')
    a.add('python')           # 集合add方法：是把要传入的元素做为一个整个添加到集合中
    a.update('python')        # 集合update方法：是把要传入的元素拆分，做为个体传入到集合中
    print(a)

