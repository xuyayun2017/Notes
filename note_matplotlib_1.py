# coding=utf-8
'''
    https://blog.csdn.net/Notzuonotdied/article/details/77876080
    plot 基础画图
'''
import matplotlib.pyplot as plt
import numpy as np

# 从[-1,1] 中等距取 50 个数作为 x 的取值
if __name__ == '__main__':
    x = np.linspace(-1,1,50)
    print(x)
    y1 = 2 * x +1
    y2 = 2 ** x + 1
# 第一个是横坐标的值，第二个是纵坐标的值
    plt.plot(x,y1)                                       # 线性
    plt.xlabel("I am x")                                # 坐标轴标签
    plt.ylabel("I am y")
    plt.show()                                           # 将设置好的 figure 对象显示出来




