# coding=utf-8
'''
    Request:
    http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
'''
import requests

if __name__ == '__main__':
    # 第一次 Request:获取列表
    payload = {
        'Filters[0][filterId]':'type',
       'Filters[0][filterName]':'type',
       'Filters[0][filterValues][]':'BITs',
       'Filters[1][filterId]':'jurisdiction',
       'Filters[1][filterName]':'jurisdiction',
       'Filters[1][filterValues][]':'China',
       'Start':'0','PageSize':'5','SortBy':'score desc'
    }
    r = requests.post("http://www.kluwerarbitration.com/Api/Search", data = payload)

    Hits = r.json()['Hits']
    count = 0
    for hits in Hits:
        count += 1
        # 提取基本信息
        id = hits['Url']
        title = hits['Title']
        decisionDate = hits['DecisionDate']
        relevantDate = hits['RelevantDate']
        language = hits['Language']
        print(count,":","ID:" + id,"Language:"+language[0])

        # 根据 id 提取正文
        payload = {'id':id}
        r = requests.post("http://www.kluwerarbitration.com/Document/_Document",data = payload)

        # 导出为 html
        txt = 'E:\\' + id + '_' + language[0] + '_' + decisionDate +'.html'
        f = open(txt, "w+", encoding='utf-8')
        f.write(r.text)
        f.write("<meta charset=\"utf-8\">")
    print("TotalHits:",count)






