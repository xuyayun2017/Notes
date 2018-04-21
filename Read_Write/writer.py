# coding=utf-8

"""
    Created by Kalyter on 2017-11-16.
"""
import datetime

import os
import xlwt


def create_style():
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = '微软雅黑'
    font.bold = False
    style.font = font
    return style


def write(data, filename='', relative_path='', destination_path=r'E:\2018\2018-3-12-论文-BITs\B&R_Country_info\BITs_info'):
    workbook = xlwt.Workbook()
    style = create_style()

    now = datetime.datetime.now()

    path = os.path.join(destination_path, now.strftime('%Y%m%d%H'))
    if relative_path != '':
        path = os.path.join(path, relative_path)
    if not os.path.exists(path):
        os.makedirs(path)

    if not filename:
        filename = '处理结果' + now.strftime('%Y%m%d%H%M%S') + '.xls'
    filename = os.path.join(path, filename)

    if data:
        sheet = workbook.add_sheet('处理结果', True)
        for row, content in enumerate(data):
            for column in range(len(content)):
                sheet.write(row, column, content[column], style)
        workbook.save(filename)
        print('文件写入成功   %s' % filename)
    else:
        print('数据不能为空')
