# coding=utf-8
'''
   图中图
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# 大图
left, bottom, width, weight = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, weight])
ax1.plot(x, y, 'r')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.set_title(r'$××Interesting××$')

# 左上小图
left, bottom, width, weight = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, weight])
ax2.plot(y, x, 'b')
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$y$')
ax2.set_title(r'$title\ inside\ 1$')

# 右下小图
plt.axes([0.6, 0.2, 0.25, 0.25])
# 将y的数据逆序输出[::1]
plt.plot(y[::-1],x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'$title\ inside\ 2$')

if __name__ == '__main__':
 plt.show()
