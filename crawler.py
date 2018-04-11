coding = "utf-8"
import urllib.request
if __name__ == '__main__':
    url = "http://www.kluwerarbitration.com/document/kli-ka-1226109-n?type=BITs&jurisdiction=China"
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode('utf-8')
    #print(html)

    txt='E:\\india.html'
    f = open(txt,"w+",encoding='utf-8')
    f.write(html)
    f.write("<meta charset=\"utf-8\">")


        
        
