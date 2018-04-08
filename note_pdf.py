# coding=utf-8
'''
    https://blog.csdn.net/zhaohansk/article/details/51711441
    https://blog.csdn.net/u011389474/article/details/60139786
'''
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfparser import PDFPage
from pdfminer.pdfinterp  import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import os
if __name__ == '__main__':
    fp = open('./Data/Albania.pdf','rb')