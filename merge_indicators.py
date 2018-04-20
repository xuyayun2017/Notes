# coding=utf-8
import pandas as pd
import openpyxl

if __name__ == '__main__':
    print("导入数据")
    ofdi = pd.read_excel("E:/2018/2018-4-15-报告/OFDI/data_ofdi3.xlsx")
    # print("OFDI:",ofdi.head())
    fdi = pd.read_excel("E:/2018/2018-4-15-报告/FDI/fdi_data4.xlsx")
    # print("FDI:",fdi.head())
    wdi_indicators = pd.read_excel("E:/2018/2018-4-15-报告/OFDI/wdi_indicators.xlsx")
    # print("WDI_INDICATORS:",wdi_indicators)
    ofdi_wdi = ofdi.merge(wdi_indicators,on = ['country','year'],how = 'left')
    fdi_wdi = fdi.merge(wdi_indicators,on = ['country','year'],how = 'left')
    print(ofdi_wdi.head())

    print("导出数据")
    writer = pd.ExcelWriter('E:\\output.xlsx')
    ofdi_wdi.to_excel(writer,'OFDI')
    fdi_wdi.to_excel(writer,'FDI')
    writer.save()
