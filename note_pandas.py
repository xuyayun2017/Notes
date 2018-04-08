# coding=utf-8
'''
   https://blog.csdn.net/cxmscb/article/details/54632492

   pandas:pannel data analysis (面板数据分析)。pandas 是基于 numpy 构建的，为时间序列分析提供了
   很好的支持。pandas 中有两个主要的数据结构，一个是 Series ，一个是 DataFrame.

   Series 类似于一维数组与字典（map)数据结构的结合。它由一组数据和一组与数据相对应的数据标签
   (索引index)组成。这组数据和索引标签的基础都是一个一维 ndarray 数组。可将 index 索引理解为行索引。
   Series 的表现形式为： 索引在左，数据在右。
   获取数据和索引： ser_obj.index, ser_obj.values
   预览数据： ser_obj.head(n), ser_obj.tail(n)

   DataFrame 是一个类似于表格的数据结构，索引包括列索引和行索引，包含有一组有序的列，每列可以是不同的值类型
   （数值、字符串、布尔值等）。DataFrame 的每一行和每一列都是一个 Series,这个 Series 的 name 属性为当前的行
   索引名/列索引名。
   通过列索引获取数据（Series类型）：df_obj[col_idx] 或 df_obj.col_idx
   .ix, 标签与位置混合索引

   网址2：https://csaladenes.wordpress.com/2015/06/21/a-visual-exploratory-of-refugee-flows-over-the-world-using-dynamic-chord-diagrams/

'''

import pandas as pd
from pandas import Series,DataFrame

'''
   一、数据结构：Series
'''
# Series 的使用代码示例
if __name__ == '__main__':
 print('用一维数组生成 Series:')
 x = Series([1,2,3,4])                           # 索引：数据
 print(x)
 print(x.values)                                 # [1 2 3 4]
 print(x.index)                                  # RangeIndex(start=0, stop=4, step=1)


 print('指定 Series 的 index :')               # 可将 index 理解为行索引
 x = Series([1,2,3,4],index = ['a','b','c','d'])
 print(x)
 print(x['a'])                                   # 通过索引来取值
 x['d'] = 6                                      # 通过行索引赋值
 print(x[['c','a','d']])                        # 类似于numpy的花式索引
 print(x[x > 2])                                 # 类似于numpy的布尔索引
 print('b' in x)                                # 类似于字典的使用。是否存在索引：True
 print('e' in x)                                # False

if __name__ == '__main__':
 print('使用字典来生成Series: ')
 data = {'a':1,'b':2,'c':3,'d':4}
 x = Series(data)
 print(x)

 print('使用字典生成 Series，并指定额外的 index,不匹配的索引数据为 NaN：')
 exindex = ['a','b','c','e']
 y = Series(data,index = exindex)
 print(y)

 print('Series 相加，相同行索引相加，不同行索引则数值为NaN: ')
 print(x + y)

 print('指定 Series 索引的名字： ')
 y.name = 'weight of letters'
 y.index.name = 'letter'
 print(y)

 print('替换 index: ')
 y.index = ['a','b','c','f']
 print(y)                                                # 不匹配的索引部分数据为 NaN

 '''
     二、数据结构：DataFrame
 '''
 #DataFrame 的使用代码示例
if __name__ == '__main__':
 print('使用字典生成 DataFrame,key 为列名： ')
 data = {'state':['ok','ok','good','bad'],
         'year':[2000,2002,2003,2004],
         'pop':[3.7,3.6,2.4,0.9]}
 print(DataFrame(data))

 print('指定列索引 columns,不匹配的为 NaN: ')
 print(DataFrame(data,columns = ['year','state','pop','debt']))

 print('指定索引 index： ')
 x = DataFrame(data,
                   columns = ['year','state','pop','debt'],    # 列名
                   index = ['one','two','three','four'])       # 索引
 print(x)

if __name__ == '__main__':
 import numpy
 print('DataFrame 元素的索引与修改：')
 print(x['state'])                                               # 返回一个名为 state 的 Series
 print(x.state)                                                   # 可直接引用，进行列索引
 print(x.ix['three'])                                            # 用 。ix[] 来区分 [] 进行行索引
 x['debt'] = 16.5                                                # 修改一整列的数据
 print(x)

 x.debt = numpy.arange(4)                                         # 用 numpy 数组修改元素
 print(x)

 print('用 Series 修改元素，没有指定的默认数据用 NaN：')
 val = Series([-1.2,-1.5,-1.7,0],index = ['one','two','five','six'])
 x.debt = val                                                     # DataFrame 的行索引不变
 print(x)

 print('给 DataFrame 添加新列：')
 x['gain'] = (x.debt > 0)                                        # 如果debt 大于0为 Truw
 print(x)

 print(x.columns)                                                 # Index(['year', 'state', 'pop', 'debt', 'gain'], dtype='object')

 print('DataFrame 转置：')
 print(x.T)

 print('使用切片初始化数据，未被匹配的数据为 NaN:')
 pdata = {'state':x['state'][0:3],'pop':x['pop'][0:2]}
 y = DataFrame(pdata)
 print(y)

 print('指定索引和列名称：')                                     # 与 Series 的 index.name 相区分
 y.index.name = '序号'
 y.columns.name = '信息'
 print(y)
 print(y.values)

'''
   三、索引对象
       pandas 的索引对象负责管理轴标签和轴名称等。构建Series 和 DataFrame时，所用到的任何数组或其他序列的
       标签都会被换成一个 index 对象。index 对象是不可修改的， Series 和 DataFrame 中的索引都是 index 对象。
'''
#代码示例
if __name__ == '__main__':
 from pandas import Index
 print('获取 index 对象：')
 x = Series(range(3),index = ['a','b','c'])
 index = x.index
 print(index)                                             # Index(['a', 'b', 'c'], dtype='object')
 print(index[0:2])                                        # Index(['a', 'b'], dtype='object')
 try:
     index[0] = 'd'
 except:
      print('Index is immutable')

 print('构造/使用Index对象:')
 index = Index(numpy.arange(3))
 obj2 = Series([1.5, -2.5, 0], index=index)
 print(obj2)

 print('判断列/行索引是否存在：')
 data = {'pop':{2.4,2.9},
         'year':{2001,2002}}
 x = DataFrame(data)
 print(x)


 '''
    四、基本功能
        1.对列/行索引重新指定索引（删除/增加：行/列）：reindex 函数
          reindex 的 method 选项：fill 或 pad:前向填充（或搬运）值
                                  bfill 或 backfill：后向填充（或搬运）值
        2.删除（丢弃）整一行/列的元素：drop 函数
        3.索引、选取和过滤
        4.算数运算和数据对齐
        5、numpy 函数应用与映射
 '''
if __name__ == '__main__':
# 1.对列/行索引重新指定索引（删除/增加：行/列）：reindex 函数
  print('重新指定索引及NaN填充值：')
  x = Series([4,7,5],index = ['a','b','c'])
  y = x.reindex(['a','b','c','d'])
  print(y)

  print('fill_value 指定不存在元素NaN的默认值：')
  print(x.reindex(['a','b','c','d'],fill_value = 0))

  print('重新指定索引并指定填充NaN的方法：')
  x = Series(['blue','purple'],index = [0,2])
  print(x.reindex(range(4),method = 'ffill'))

  print('对 DataFrame 重新指定行/列索引：')
  x = DataFrame(numpy.arange(9).reshape(3,3),
                      index = ['a','c','d'],                        # 行索引
                      columns = ['A','B','C'])                      # 列索引
  print(x)

  x = x.reindex(['a','b','c','d'],method = 'bfill')
  print(x)

  print('重新指定 column:')
  states = ['A','B','C','D']
  x = x.reindex(columns =states,fill_value = 0)
  print(x)

  print(x.ix[['a','b','d','c'],states])                            # 交换行的位置

#2.删除（丢弃）整一行/列的元素：drop 函数
if __name__ == '__main__':
  print('Series 根据行索引删除行：')
  x = Series(numpy.arange(4),index = ['a','b','c','d'])
  print(x.drop('c'))
  print(x.drop(['a','b']))

  print('DataFrame 根据索引行/列删除行/列：')
  x = DataFrame(numpy.arange(16).reshape((4,4)),
                index = ['a','b','c','d'],
                columns = ['A','B','C','D'])
  print(x)

  print(x.drop(['A','B'],axis = 1))                                   # 删除 A B 两列
  print(x.drop('a',axis = 0))                                         # 删除 a 行
  print(x.drop(['a','b'], axis=0))


# 3.索引、选取和过滤
'''
   DataFrame 的索引选项：
   obj[val]       选取DataFrame 的单个列或一组列。
   obj.ix[val]    选取DataDrame 的单个行或一组行
   obj.ix[:,val]  选取单个列或列子集
   obj.ix[val1,val]    同时选取行或列
   reindex             将一个或多个轴匹配到新索引
   xs方法              根据标签选取单行或单列，并返回一个 Series
   icol、irow方法      根据整数位置选取单行或单列，并返回一个 Series
   get_value、set_value方法      根据行标签或列标签选取单个值
'''
if __name__ == '__main__':
  print('Series 的数组索引/字典索引：')
  x = Series(numpy.arange(4),index = ['a','b','c','d'])
  print(x['b'])                                                             # 1 像字典一样索引
  print(x[1])                                                               # 1 像数组一样索引
  print(x[[1,3]])                                                           # 花式索引
  print(x[x < 2])                                                           # 布尔索引

  print('Series 的数组切片：')
  print(x['a':'c'])                                                        # 闭区间，索引顺序为前后
  x['a':'c'] = 5
  print(x)

  print('DataFrame 的索引：')
  data = DataFrame(numpy.arange(16).reshape((4,4)),
                   index = ['a','b','c','d'],
                   columns = ['A','B','C','D'])
  print(data)
  print(data['A'])                                                          # 打印列
  print(data[['A','B']])                                                    # 花式索引。注意：双括号！
  print(data[:2])                                                            # 切片索引。选择前两行
  print(data.ix[:2,['A','B']])                                               # 选择前两行、AB两列
  print(data.ix[['a','b'],[3,0,1]])                                          # 行：字典索引，列：数组索引
  print(data.ix[2])                                                           # 打印第2行
  print(data.ix[:'b','A'])                                                    # 行从开始到 b， 列A

  print('根据条件选择：')
  print(data)
  print(data[data.A > 5])                                                    # 根据条件选择行
  print(data < 5)                                                            # 打印 True 或 False
  data[data < 5] = 0                                                         # 条件索引:将小于5的数设为0
  print(data)


# 4.算术运算和数据对齐
if __name__ == '__main__':
  print('DataFrame 算术：不重叠部分为NaN,重叠部分元素运算：')
  x = DataFrame(numpy.arange(9.).reshape((3,3)),
                columns = ['A','B','C'],
                index = ['a','b','c'])
  y = DataFrame(numpy.arange(12).reshape((4,3)),
                columns = ['A','B','C'],
                index = ['a','b','c','d'])
  print(x)
  print(y)
  print(x + y)
  print('对x/y的不重叠部分填充，不是对结果NaN填充：')
  print(x.add(y,fill_value = 0))                                                  # x不变化

  print('DataFrame 与 Series 运算：每行/每列进行运算：')
  frame = DataFrame(numpy.arange(9).reshape((3,3)),
                    columns = ['A','B','C'],
                    index = ['a','b','c'])
  series = frame.ix[0]                                                            # frame 的第一行
  print(frame)
  print(series)
  print(frame - series)                                                           # frame 的每行减 series

  series2 = Series(range(4),index = ['A','B','C','D'])
  print(frame + series2)                                                          # 按行运算，缺失列则为 NaN

  series3 = frame.A                                                               # frame 的第一列
  print(frame.sub(series3,axis = 0))                                              # 按列运算


# 5.numpy 函数应用与映射
if __name__ == '__main__':
  print('numpy 函数在Series/DataFrame 的应用：')
  frame = DataFrame(numpy.arange(9).reshape(3,3),
                    columns = ['A','B','C'],
                    index = ['a','b','c'])
  print(frame)
  print(numpy.square(frame))                                                       # 平方
  series = frame.A                                                                 # A 列
  print(numpy.square(series))

  print('lambda(匿名函数）以及应用：')
  print(frame)
  print(frame.max())                                                               # 每列的最大值
  f = lambda x: x.max() - x.min()                                                 # 最大值-最小值
  print(frame.apply(f))                                                            # 作用到每一列
  print(frame.apply(f,axis = 1))                                                   # 作用到每一行

  def f(x):                                                                     # Series 的元素的类型为 Series
       return Series([x.min(),x.max()],index = ['min','max'])                  # 返回每列的最小值、最大值
  print(frame.apply(f))

  print('applymap 和 map:作用到每一个元素：')
  _format = lambda x: '%.2f' % x                                                # 定义格式:两位小数
  print(frame.applymap(_format))                                                 # 针对 DataFrame
  print(frame['A'].map(_format))                                                 # 针对 Series
