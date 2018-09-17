import requests
import http.cookiejar
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import requests
def setCookie(url,prams,headers):
    # cookie_filename = './config/cookie.txt'
    cookie_filename = 'D:\\PycharmProjects\\untitled\\config\\cookie.txt'
    #创建cookie
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    data = urllib.parse.urlencode(prams).encode('utf-8')
    response = urllib.request.Request(url, data,headers)
    # 写入返回的cookie
    r = opener.open(response)
    with urlopen(response) as res:
        res = res.read().decode() #read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
        print(res)
    cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
    print(cookie)

if __name__ == "__main__":
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
    setCookie(url,prams,headers)
    # r = requests.post(url,prams,headers)
    # print(r.text)
    # print(r.status_code)
    # print("成功")

    # data_url = "/json/stockin/add"
    # url = post_url + data_url
    # print(url)
    # prams = {"copartnerId": 1165, "warehouseId": 165, "orderState": 1, "goods": [
    #     {"gid": 183167, "name": "【散】杜7月17测试单1", "type": "normal", "nums": 3, "suggestNum": 0, "dailySold": 0}],
    #           "contractId": 364}
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #     "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Content-Type": "application/json",
    #     "X-Requested-With": "XMLHttpRequest",
    #     "Connection": "keep-alive",
    #     "Referer": "http://192.168.1.248:31100/stockin/apply/add",
    #     "Cookie": "ncgCurrentCityId=320903; purchase_sales_management=s%3AfQ4FJf1R8T0zSQz5sfizJZa-jDCmtXEM.Ysk0B%2Fs2j7Tl%2FdxZPJTiymLbl%2FDr6yLinnR5%2BzoKJlQ"
    # }
    # r = requests.post(url,json=prams,headers=headers)
    # print(r.text)
    # print("成功")
