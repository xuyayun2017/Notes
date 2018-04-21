# coding=utf-8
'''
   https://blog.csdn.net/u013634684/article/details/49646311
'''
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

if __name__ == '__main__':
    print("1.导入数据")
    data = pd.read_excel('E:/2018/2018-4-15-报告/BITs_info_China.xls')
    data.head()
    country = data["country"]
    print(country)
    classify = data['col']
    year = data['year']
    articles = data['articles']
    ax = plt.subplot(111)
    plt.figure(figsize = (9,5))
    p1 = plt.scatter(year[:107],articles[:107],c = 'r',label =  'China',marker = '*',edgecolors='r')
    p2 = plt.scatter(year[107:160],articles[107:160],c = '',label =  'USA',marker = '^',edgecolors='y')
    p3 = plt.scatter(year[160:194], articles[160:194], c='', label='Canada', marker='^', edgecolors='g')
    p4 = plt.scatter(year[194:211], articles[194:211], c='', label='Japan', marker='^', edgecolors='b')
    plt.legend(loc='upper left')
    #plt.legend(loc='upper left', title='other')
    # plt.xticks((year))
    #plt.yticks((articles))
    plt.xlabel('Year')        # 设置 x 轴标签
    plt.ylabel('Number of Articles')



    plt.show()