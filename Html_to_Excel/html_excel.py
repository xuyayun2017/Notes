# coding=utf-8
'''
    html 转 excel:
    https://blog.csdn.net/sinat_30062549/article/details/51180518
'''

# 第一步：
import numpy as np
import pandas as pd
import linecache
if __name__ == '__main__':
    with open('E:/2018/2018-5-16-电子商务/信息技术产品（ITA)贸易数据/test/Canada_and_Australia.xls','r') as f:
    # with open('E:/2018/2018-5-16-电子商务/信息技术产品（ITA)贸易数据/test/Canada_and_Austria.xls', 'rb') as f:
    # with open('E:/2018/2018-5-16-电子商务/信息技术产品（ITA)贸易数据/test/Canada_and_Austria.xls', 'r', encoding='utf-8') as f:
        print("文件名：", f.name)
        print("行数：", len(f.readlines))

        df = pd.read_html(f.read().decode("gbk").encode('utf-8'), encoding='utf-8')
        print(df[0])
        bb = pd.ExcelWriter('out.xlsx')
        df[0].to_excel(bb)
        bb.close()