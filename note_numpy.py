# coding=utf-8
''' numpy 是 python 中众多科学软件包的基础。提供了一个特殊的数据类型，
    其在向量计算上做了优化。这个对象是科学数值计算中大多数算法的核心。

    相比于原生的 python,利用 numpy 数组可以获得显著的性能加速，尤其是当你的计算遵循
    单指令多数据流（SIMD）范式时。然而，利用numpy 也有可能有意无意的写出未优化的代码。
'''

import numpy as np

if __name__ == '__main__':
 arr = np.array([1,2,3],dtype = np.float64)    #数组
 print(arr)

 print(np.zeros((3,6)))                        #3*6的零矩阵
 print(np.empty([2,3,2],dtype = int))          #3*2的空矩阵。   依据给定形状和类型(shape[, dtype, order])返回一个新的空数组。
                                               #shape : 整数或者整型元组，定义返回数组的形状；
                                               #dtype : 数据类型，可选。定义返回数组的类型。
 print('number of dim: ', arr.ndim)          #矩阵的维度：1
 print('dtype: ',arr.dtype)                   #矩阵的元素类型：float64
 print('shape: ',arr.shape)                   #矩阵的shape，即每一维上的元素个数：(3,)
 print('size: ',arr.size)                     #矩阵的元素总数： 3

 print(np.arange(15))                          #定义向量，0-14：[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
 print(np.arange(10,20,2))                     #定义向量，10-20之间，元素间隔为2，左闭右开：[10 12 14 16 18]

 print(np.arange(12).reshape((3,4)))          #定义向量并转为矩阵
 print(np.linspace(1,10,6).reshape(2,3))      #定义向量，类型是线性间隔


 #矩阵的加、减、点乘、平方
 a = np.array([10,20,30,40])
 b = np.arange(4)
 c = a - b
 d = a + b
 e = a * b
 f = a ** b
 print(a,b)
 print(c,d)
 print(e,f)

 #矩阵的三角运算
 sin = 10 * np.sin(a)
 print(sin)

 #矩阵的判断
 print(b < 3)                               #[ True  True  True False]
 print(b == 3)                              #[False False False  True]

 #矩阵的点乘及乘法
 a = [[1,1],[0,1]]                          #[[1, 1], [0, 1]]
 b = np.arange(4).reshape((2,2))
 c = a * b                                  #对应数字相乘，或：np.multiply(a,b)
 d = np.dot(a,b)                            #真正意义上的矩阵乘积
 print(a)
 print(b)
 print(c)
 print(d)

 # np.random返回随机的浮点数，在半开区间 [0.0,1.0]
 # 定义随机矩阵
 a = np.random.random((2,4))                # 2*4
 print(a)

 # 矩阵的求和、最小值、最大值
 print(np.sum(a))
 print(np.min(a))
 print(np.max(a))
if __name__ == '__main__':
 # 矩阵的某一维度的求和、最小值、最大值，axis=0:列，axis=1：行
 print(np.sum(a,axis = 1))
 print(np.max(a,axis = 1))
 print(np.min(a,axis = 0))

 print(arr[0:3])               #选择第1-3行
 print(arr[[0,2]])             #选择第1行和第3行
 print(arr.T)                  #转置

 # arr.mean()  arr.mean(axis=1)   算术平均数
 # arr.sum()   arr.std()  arr.var()   和、标准差、方差
 # arr.min()   arr.max()   最小值、最大值
 # arr.argmin()   arr.argmax()    #最小索引、最大索引
 # arr.cumsum()    arr.cumprod()   #所有元素的累计和、累计积
 # arr.all()   arr.any()   # 检查数组中是否全为真、部分为真
 # arr.sort()   arr.sort(1)   #排序、1轴向上排序
 # arr.unique()   #去重
 # np.in1d(arr1, arr2)  #arr1的值是否在arr2中
 # np.load() np.loadtxt() np.save() np.savez() ＃读取、保存文件
 # np.concatenate([arr, arr], axis=1)  ＃连接两个arr，按行的方向

