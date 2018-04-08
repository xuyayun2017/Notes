# coding=utf-8
'''
   subplot 多合一显示
'''
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    plt.figure()

    # 将整个 figure 分成两行两列
    plt.subplot(2,2,1)

    # 第一个参数表示 x 的范围，第二个参数表示 y 的范围
    plt.plot([0,1],[0,1])

    plt.subplot(222)
    plt.plot([0,1],[0,2])

    plt.subplot(223)
    plt.plot([0,1],[0,3])

    plt.subplot(224)
    plt.plot([0,1],[0,4])

    plt.show()