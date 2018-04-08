# coding=utf-8
'''
   https://blog.csdn.net/jinlong_xu/article/details/70183377
   hist 直方图
   bar 条形图
   区别：
1. 直方图是用面积表示各组频数的多少，矩形的高度表示每一组的频数或频率，
   宽度则表示各组的组距，因此其高度与宽度均有意义。
   条形图是用条形的长度表示各类别频数的多少，其宽度（表示类别）则是固定的；
2. 由于分组数据具有连续性，直方图的各矩形通常是连续排列，而条形图则是分开排列。
3. 条形图主要用于展示分类数据，而直方图则主要用于展示数据型数据。
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
# 概率分布直方图
# 高斯分布
# 均值为0
mean = 0
# 标准差为1，反应数据集中还是分散的值
sigma = 1
x = mean + sigma * np.random.randn(10000)
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 5))
# 第二个参数是柱子宽一些还是窄一些，越大越窄越密
plt.figure(num=1)
ax0.hist(x, 40, normed=1, histtype='bar', facecolor='yellowgreen', alpha=0.75)
##pdf概率分布图，一万个数落在某个区间内的数有多少个
ax0.set_title('pdf')
ax1.hist(x, 20, normed=1, histtype='bar', facecolor='pink', alpha=0.75, cumulative=True, rwidth=0.8)
# cdf累计概率函数，cumulative累计。比如需要统计小于5的数的概率
ax1.set_title("cdf")
fig.subplots_adjust(hspace=0.4)  # 设置图间距

plt.figure(num=2)
mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

if __name__ == '__main__':
 plt.show()