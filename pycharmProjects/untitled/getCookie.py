import http.cookiejar
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
post_url = "http://192.168.1.248:31100"
data_url = "/users/login"
url = post_url + data_url
prams = {"userName": "17602173295", "password": "123456"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive"}
cookie_filename = 'cookie.txt'
#创建cookie
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
data = urllib.parse.urlencode(prams).encode('utf-8')
response = urllib.request.Request(url, data,headers)
r = opener.open(response)
with urlopen(response) as res:
    res = res.read().decode() #read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
    print(res)

for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)

cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
print(cookie)
