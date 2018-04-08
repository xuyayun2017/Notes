# coding=utf-8
'''
   主次坐标轴
'''
import matplotlib.pyplot as plt
import numpy as np

# 从[0, 10]以0.1为间隔，形成一个列表
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1


fig, ax1 = plt.subplots()
# 镜像（上下左右颠倒）
ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b--')

# 为轴进行命名
ax1.set_xlabel(r'$X\ data$', fontsize=16)
ax1.set_ylabel(r'$Y1$', color='g', fontsize=16)
ax2.set_ylabel(r'$Y2$', color='b', fontsize=16)

if __name__ == '__main__':
 plt.show()