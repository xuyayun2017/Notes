# coding=utf-8
'''
   python 数据可视化——seaborn 简介和实例
   https://blog.csdn.net/qq_34264472/article/details/53814653

   Seaborn 其实是在 matplotlib 的基础上进行了更高级的 API 封装，从而使得作图更加容易，在大多数情况下
   使用 seaborn 就能做出很具有吸引力的图。这里实例采用的数据集都是seaborn提供的几个经典数据集，dataset文件可见于Github。
'''
'''
   1. set_style() 作用：是用来设置主题的，Seaborn 有5个预设好的主题：
      darkgrid , whitegrid , dark , white ,和 ticks  默认： darkgrid。
   2. set()  作用：通过设置参数可以用来设置背景，调色板等，更加常用。
   3. distplot() 作用：hist()加强版
   4. kdeplot()  作用：密度曲线图
   5. bosplot()  作用：箱线图
   6. jointplot()作用：联合分布
   7. heatmap()  作用：热力图
   8. pairplot()
   9. FacetGrid( )
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
if __name__ == '__main__':
    ''' 
    1. set_style( )  set( ):set_style( )是用来设置主题的;set( )通过设置参数可以用来设置背景，调色板等，更加常用。
   
    plt.figure(num = 1,figsize = (5,5))
    sns.set_style("whitegrid")
    plt.plot(np.arange(10))

    plt.figure(num = 2,figsize = (5,5))
    sns.set(style = 'white',palette = 'muted',color_codes = True)
    plt.plot(np.arange(10))
    '''
    '''
    2. distplot( )  kdeplot( ):distplot( )为hist加强版，kdeplot( )为密度曲线图 
    
    plt.figure(num=3,figsize = (5,5))
    data = pd.read_excel('E:/2018/计量——张涤新/作业三/2017.xlsx')
    fig,axes = plt.subplots(1,2)
    sns.distplot(data['日收益率'],ax = axes[0],kde = True,rug = True)   # kde 密度曲线，rug 边际毛毯
    sns.kdeplot(data['日收益率'],ax = axes[1],shade = True)             # shade 阴影

    plt.figure(num = 4,figsize = (5,5))
    sns.set(palette = 'muted',color_codes = True)
    rs = np.random.RandomState(10)
    d = rs.normal(size = 100)
    f,axes = plt.subplots(2,2,figsize = (6,6),sharex = True)
    sns.distplot(d,kde = False,color = 'b',ax = axes[0,0])
    sns.distplot(d,hist = False,rug = True,color = 'r',ax = axes[0,1])
    sns.distplot(d,hist = False,color = 'g',kde_kws = {"shade":True},ax = axes[1,0])
    sns.distplot(d,color = 'm',ax = axes[1,1])
    '''
    '''
    3. boxplot( )  箱型图 
    plt.figure(num=6,figsize = (5,5))
    data2 = pd.read_excel('E:/2018/计量——张涤新/作业三/2017.xlsx')
    sns.set(style = 'ticks')                                            # 设置主题
    sns.boxplot(x = data2['月份'],y =data2['收盘价'],palette = 'PRGn')
    '''
    '''
    4. jointplot( )  联合分布
    plt.figure(num = 7,figsize = (5,5))
    data = pd.read_excel('E:/2018/计量——张涤新/作业三/2017.xlsx')  # 右上角为相关系数
    sns.jointplot('前收盘', '收盘价', data,kind = 'reg')
    '''
    '''
    5. heatmap( )   热点图
   
    #plt.figure(num = 8,figsize = (6,5))
    # 方法一
    data = pd.read_excel('C:/U盘备份-2/2017-11-20-论文/协定数据/total2.xls','Sheet1')
    data = data.corr()
    #sns.heatmap(data)

    # 方法二
    sns.set()
    np.random.seed(0)
    uniform_data = np.random.rand(10,12)
    # ax = sns.heatmap(uniform_data,center = 0,vmin = 0,vmax = 1)  # vmax,vmin, 图例中最大值和最小值的显示值，没有该参数时默认不显示
                                                                  # center = 0 以0为中心的数据绘制一张热力图
    # 用行和列标签绘制
    #data = sns.load_dataset('flights')                           # 获取自带的数据
    #flights = data.pivot("month", "year", "passengers")
    data2 = pd.read_excel('C:/U盘备份-2/2017-11-20-论文/协定数据/total2.xls','Sheet3')
    data2 = data2.corr()
    # 绘制 x-y-z 的热力图，比如 年-月-销量 的热力图
    f,ax = plt.subplots(figsize = (9,8))
    sns.heatmap(data2,annot=True,linewidths=.5,cmap = 'YlGnBu',ax = ax)
    # fmt='d' 设置格式；cmap = 'YlGnBu 设置颜色; annot=True 注释; linewidths=.5 每个网格上用线隔开
    # 设置坐标字体方向
    label_y = ax.get_yticklabels()
    plt.setp(label_y,rotation = 360,horizontalalignment = 'right')
    label_x = ax.get_xticklabels()
    plt.setp(label_x,rotation = 90,horizontalalignment ='right')
     '''
    '''
    6. pairplot()
    '''
    data = pd.read_excel('E:/2018/计量——张涤新/作业三/2017.xlsx','Sheet3')
    sns.set()                              # 使用默认颜色
    sns.pairplot(data,hue = '月份')      # hue 选择分类列


if __name__ == '__main__':
    plt.show()
