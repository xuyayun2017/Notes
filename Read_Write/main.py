# coding=utf-8

"""
    Created by Kalyter on 2017-11-16.
"""
import time

from learning.xuyayun.learning.BITs.Read_Write import reader
from learning.xuyayun.learning.BITs.Read_Write import writer



def main(step=5, max_comparision=-1):
    """使用jaccard算法，计算出xml文件夹下的文本之间的相似度。

    :param step: 分词系数
    :param max_comparision: 最大需要比较的文件数，默认是所有文件
    """

    start_time = time.time()
    data = []
    title = ('文件名', '协定名', '国家1', '国家2','签署时间','生效时间', '条款','条款数目')
    data.append(title)
    # for filename in reader.read_path('./Canada_BITs', max_comparision):
    for filename in reader.read_path('E:/2018/2018-3-12-论文-BITs/B&R_Country_info/BITs_html', max_comparision):
        # 读取文件夹下面的，文件内容
        result_tuple = reader.read(filename)
        filename, name, country1, country2,sign_year,force_year,article,count = result_tuple

        print('%s  %s   %s   %s   %s   %s   %s  %s' % (filename, name, country1, country2,sign_year,force_year,article,count))
        # 保存结果
        data.append((filename, name, country1, country2,sign_year,force_year,article,count))
    end_time = time.time()
    data.append(('耗时:', '%.2fs' % (end_time - start_time)))

    print('写入结果')
    writer.write(data)
    print('写入xls文件成功')


if __name__ == '__main__':
    main()
