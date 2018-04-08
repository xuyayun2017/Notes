# coding=utf-8
'''
   subplot2grid 分格显示
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

if __name__ == '__main__':
    plt.figure()
    # 第一个元素表示将总的面板进行划分，划分为3行3列，
    # 第二个元素表示该面板从0行0列开始，列的跨度（colspan）为3列，行的跨度（rowspan）为1
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
    # 第一个元素的表示X的范围为[1,2]，第二个元素表示Y的范围为[1,2]
    ax1.plot([1, 2], [1, 2])
    ax1.set_title(r'$ax1\_title$')
    # 第一个元素表示将总的面板进行划分，划分为3行3列，
    # 第二个元素表示该面板从1行0列开始，列的跨度（colspan）为2列，行的跨度（rowspan）取默认值1
    ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
    ax2.set_title(r'$ax2\_title$')
    # 第一个元素表示将总的面板进行划分，划分为3行3列，
    # 第二个元素表示该面板从1行2列开始，行的跨度（rowspan）为2列，列的跨度（colspan）取默认值1
    ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    ax3.set_title(r'$ax3\_title$')
    # 第一个元素表示将总的面板进行划分，划分为3行3列，
    # 第二个元素表示该面板从2行0列开始,行的跨度（rowspan）为2列，列的跨度（colspan）取默认值1
    ax4 = plt.subplot2grid((3, 3), (2, 0))
    ax4.set_title(r'$ax4\_title$')
    # 第一个元素表示将总的面板进行划分，划分为3行3列，
    # 第二个元素表示该面板从2行1列开始,行的跨度（rowspan）为2列，列的跨度（colspan）取默认值1
    ax5 = plt.subplot2grid((3, 3), (2, 1))
    ax5.set_title(r'$ax5\_title$')

    plt.tight_layout()
    plt.show()