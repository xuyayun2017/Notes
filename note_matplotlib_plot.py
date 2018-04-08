# coding=utf-8
'''
   plot 多个图及各种设置
'''
import matplotlib.pyplot as plt
import numpy as np

# 多个 figure
if __name__ == '__main__':
    x = np.linspace(-1,1,50)
    y1 = 2 * x + 1
    y2 = 2 ** x +1

'''第一幅图：figure1'''
if __name__ == '__main__':
    plt.figure()                                  # 注意：每次调用figure的时候都会重新申请一个 figure 对象
    plt.plot(x,y1)                                # (横坐标，纵坐标)

'''第二幅图：figure2'''
if __name__ == '__main__':
    plt.figure(num = 2,figsize = (8,5))           # 第一个参数表示编号，第二个参数表示图标长宽
    l1, = plt.plot(x,y2,                          # 当我们需要在画板中绘制两条线的时候，可使用此方法
                   label = 'aaa' )
    l2, = plt.plot(x,y1,
                 color = 'red',                   # 线条颜色
                 linewidth = 1.0,                  # 线条粗细
                   linestyle='--',                 # 线条样式
                 label = 'bbb' )                   #标签
    plt.legend(handles = [l1,l2],                   # 使用legend 绘制多条曲线
               labels = ['aaa','bbb'],
               loc = 'best')
    plt.xlabel("I am x")                           # 坐标轴标签
    plt.ylabel("I am y")

    plt.xlim((-1,2))                               # x 参数的范围
    plt.ylim((1,3))                                # y 参数的范围

    new_ticks = np.linspace(-1,2,5)                # 设置点的位置
    plt.xticks(new_ticks)
    plt.yticks([-2,-1.8,-1,1.22,3],                # 为点的位置设置对应的文字
               [r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])

    ax = plt.gca()                                 # gca = 'get current axis'
    ax.spines['right'].set_color('none')          # 将右边和上边的边框（脊）的颜色去掉
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')          # 绑定 x 轴和 y 轴
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data',0))   #  定义 x 轴和 y 轴的位置
    ax.spines['left'].set_position(('data',0))

'''第三幅图：figure3'''
if __name__ == '__main__':
    plt.figure(num=3, figsize=(12, 8))
    plt.plot(x,y2)
    plt.plot(x,y1,color = 'red',linewidth = 1.0,linestyle = '--')

    ax = plt.gca()
    ax.spines['right'].set_color('none')           # 去边框颜色
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')           # 绑定轴
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))

    x0 = 1                                           # 显示交叉点
    y0 = 2 * x0 +1
    plt.scatter(x0,y0,s = 66,color = 'b')            # s 表示点的大小，默认 rcParams['lines.markersize']**2
    plt.plot([x0,x0],[y0,0],'k-.',lw = 2.5)          # 定义线的范围，X 的范围是定值，Y 的范围是从 y0 到 0
                                                      # lw 是线宽

    plt.annotate(r'$2x+1=%s$' % y0,                 # 设置关键位置的提示信息
                 xy = (x0,y0),
                 xycoords = 'data',

                 xytext = (+30,-30),
                 textcoords = 'offset points',
                 fontsize = 16,
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2') # 设置箭头
                 )

    plt.text(0,3,
             r'$This\ is\ a\ good\ idea.\ \mu\ \sigma_i\ \alpha_t$',
             fontdict = {'size':16,'color':'r'})

    plt.show()




