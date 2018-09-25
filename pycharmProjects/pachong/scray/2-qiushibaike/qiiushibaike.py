import re
import urllib.request
from bs4 import  BeautifulSoup
import urllib.parse

class Spider(object):
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
        self.headers = {'User-Agent': self.user_agent}
        self.url='http://www.qiushibaike.com/hot/page/'

    def start(self):
        try:
            datas=[]
            dataa=[]
            p=1
            while p<2:
                url=self.url+str(p)+'/?s=4928396'
                request=urllib.request.Request(url,headers=self.headers)
                response=urllib.request.urlopen(request)
                data=response.read()
                soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
                links = soup.find_all('div',class_='content')
                Links=soup.find_all('i',class_='number')
                for link in links:
                    datas.append(link.find('span').get_text())
                    
                for link in Links:
                    dataa.append(link.get_text())
                p=p+1

            return datas,dataa
        except Exception as e:
            print(e)


spider=Spider()
ff,dd=spider.start()
print('当您输入回车的时候，继续查看下一条，当输入其他时，退出')
i=0
cc=''
while cc=='':
    if i>=len(ff):
        print('本页加载完毕')
        break
    print('词条：'+ff[i])
    print('本词条的点赞数：'+dd[2*i])
    print('本词条的评论数：'+dd[2*i+1])
    i=i+1
    cc=input()

