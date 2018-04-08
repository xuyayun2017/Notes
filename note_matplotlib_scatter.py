# coding=utf-8
'''
   scatter 散点图
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    n = 1024

    X = np.random.normal(0,1,n)                   # 从 0
    Y = np.random.normal(0,1,n)
    T = np.arctan2(X,Y)

    plt.figure(num=1, figsize=(8, 5))
    plt.scatter(np.arange(5), np.arange(5))      # [ 0  1  2  3  4]

    plt.figure(num=2, figsize=(8, 5))
    plt.scatter(X, Y)

    plt.figure(num=3, figsize=(8, 5))
    plt.scatter(X,T)


    plt.xticks(())
    plt.yticks(())

    plt.show()

