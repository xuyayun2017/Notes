# coding=utf-8
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame

if __name__ == '__main__':
    print("载入数据")
    data = pd.read_excel('E:/2018/2018-4-15-报告/Sub-category.xlsx')
    category = data['category']
    #country = data['country']
    #percentage = data['percentage']
    china = data['china']
    USA = data['USA']
    Canada = data['Canada']
    japan = data['Japan']

    figure = plt.figure(figsize=(20, 20), facecolor='w')
    ax = figure.add_subplot(111, position=[0.05, 0.4, 0.5, 0.5])
    xcategory = range(0,len(category))
    xcategory1 = [i + 0.15 for i in xcategory]
    xcategory2 = [i + 0.15 for i in xcategory1]
    xcategory3 = [i + 0.15 for i in xcategory2]
    #data.pivot('category','country','percentage').plot.bar()
    plt.bar(xcategory,china,width = 0.15,color = 'r',label = 'China',alpha = 0.8)
    plt.bar(xcategory1,USA,width = 0.15,color = 'orange',label = 'USA',alpha = 0.8)
    plt.bar(xcategory2,Canada,width = 0.15,color = 'g',label = 'Canada',alpha = 0.8)
    plt.bar(xcategory3,japan,width = 0.15,color = 'blue',label = 'Japan',alpha = 0.8)
    plt.xlabel('Category')
    plt.ylabel('Percentage')
    plt.xticks(range(0,8),category,rotation = 50)
    #p2 = plt.bar(category,USA,width = 0.2,color = 'y',label = 'USA')
    plt.legend(loc='upper right')
    plt.show()

