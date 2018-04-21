# coding=utf-8

"""
    Created by Kalyter on 2017-11-16.
"""
import os
import re
from bs4 import BeautifulSoup
from urllib import request
from string import punctuation

def read(filename):
    open_file = open(filename, 'r', encoding='utf-8')
    raw = open_file.read()
    soup = BeautifulSoup(raw)
    # soup = BeautifulSoup(open(filename, encoding='utf-8'))       # 与上面三句等价
    name = soup.h1.string
    # 提取签订国家
    country = soup.find_all(href=re.compile('^/bits'))
    dr = re.compile(r'<[^>]+>', re.S)
    if country[0] != "":
        country1 = dr.sub('', str(country[0]))
    else:
        country1 = ""
    if country[1] != "":
        country2 = dr.sub('', str(country[1]))
    else:
        country2 = ""
    # 提取 Article 并计数
    article = soup.find_all(class_="legis-article-title")
    count = len(article)
    dr = re.compile(r'<[^>]+>', re.S)
    article = dr.sub('', str(article))
    # 提取 article1
    article1 = soup.find_all(id='a0002', class_="legis-article")
    dr = re.compile(r'<[^>]+>', re.S)
    article1 = dr.sub('', str(article1))
    # 提取签署时间 & 生效时间
    year = soup.find_all(class_="docinfoblock-item")
    if len(year) == 6:
        sign_year = year[3]
        dr = re.compile(r'<[^>]+>', re.S)
        sign_year = dr.sub('', str(sign_year))
        dr = re.compile(r'Promulgation', re.S)
        sign_year = dr.sub('', str(sign_year))
        dr = re.compile(r'\n', re.S)
        sign_year = dr.sub('', str(sign_year))

        force_year = year[2]
        dr = re.compile(r'<[^>]+>', re.S)
        force_year = dr.sub('', str(force_year))
        dr = re.compile(r'Entry into force', re.S)
        force_year = dr.sub('', str(force_year))
        dr = re.compile(r'\n', re.S)
        force_year = dr.sub('', str(force_year))

        topic = year[4]
        dr = re.compile(r'<[^>]+>', re.S)
        topic = dr.sub('', str(topic))
        dr = re.compile(r'Topics', re.S)
        topic = dr.sub('', str(topic))
        dr = re.compile(r'\n', re.S)
        topic = dr.sub('', str(topic))
    else:
        sign_year = year[2]
        dr = re.compile(r'<[^>]+>', re.S)
        sign_year = dr.sub('', str(sign_year))
        dr = re.compile(r'Promulgation', re.S)
        sign_year = dr.sub('', str(sign_year))
        dr = re.compile(r'\n', re.S)
        sign_year = dr.sub('', str(sign_year))

        force_year = ''

        topic = year[3]
        dr = re.compile(r'<[^>]+>', re.S)
        topic = dr.sub('', str(topic))
        dr = re.compile(r'Topics', re.S)
        topic = dr.sub('', str(topic))
        dr = re.compile(r'\n', re.S)
        topic = dr.sub('', str(topic))

    result_tuple = (filename,name,country1,country2,sign_year,force_year,article,count)
    return result_tuple

    # 1.全部转换成小写
    # 2.删除所有标点符号
    # 3.删除所有数字
    # 4.删除所有空行，单词间空格不删
    # 5.删除所有高亮标签


def read_path(path, max_comparision=-1):
    file_list = os.listdir(path)
    ignore = ['TPP.xml', 'TPPspanish.xml']
    file_list = [i for i in file_list if i not in ignore]
    file_list.sort()
    file_list = file_list[:max_comparision]
    for file in file_list:
        yield path + '/' + file
