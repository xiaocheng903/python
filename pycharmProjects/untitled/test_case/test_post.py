import requests
import unittest
from common import configMysql
from common import setCookie
from common import readCookie
client = configMysql.mysqldb()
sy = client.configMysql()
class post_requset(unittest.TestCase):
    global cookie
    def setUp(self):
        self.post_url = "http://192.168.1.248:31100"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest"
        }

    def test_post_01(self):
        data_url = "/users/login"
        url = self.post_url + data_url
        print(url)
        prams = {"userName":"17602173295","password":"123456"}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest"}
        setCookie.setCookie(url,prams,headers)
        # r =requests.post(url,prams,headers)
        # print(r.text)

    # def test_post_02(self):
    #     data_url = "/json/stockin/add"
    #     url = self.post_url + data_url
    #     print(url)
    #     prams = {"copartnerId": 1165, "warehouseId": 165, "orderState": 1, "goods": [
    #         {"gid": 183167, "name": "【散】杜7月17测试单1", "type": "normal", "nums": 3, "suggestNum": 0, "dailySold": 0}],
    #               "contractId": 364}
    #     # headers = self.headers
    #     # readCookie.get(url,prams,headers)
    #     headers = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #         "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    #         "Accept-Encoding": "gzip, deflate, br",
    #         "Content-Type": "application/x-www-form-urlencoded",
    #         "X-Requested-With": "XMLHttpRequest",
    #         "Connection": "keep-alive",
    #         "cookie":"ncgCurrentCityId=320903,purchase_sales_management=s%3AbimaXc9yBZhKApxIVkp1gZD4qrQ843BA.l8Xd00iLQqcjsZImMkH7Jd6mo4X81IUrXMZymbaUpLQ"
    #     }
    #     r = requests.post(url,json=prams,headers=headers)
    #     print(r.text)
    def test_post_02(self):
        url = "http://192.168.1.248:31100/json/stockin/add"
        prams = {"copartnerId": 1165, "warehouseId": 165, "orderState": 1, "goods": [
            {"gid": 183167, "name": "【散】杜7月17测试单1", "type": "normal", "nums": 3, "suggestNum": 0, "dailySold": 0}],
                 "contractId": 364}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        readCookie.get(url, prams, headers)

    # def test_post_03(self):
    #     global order_id
    #     sql = "select id from stock_in_orders ORDER BY id desc limit 1;"
    #     sy.execute(sql)
    #     order_id = sy.fetchall()
    #     print(order_id)
    #     data_url = "/json/stockin/commit"
    #     url = self.post_url + data_url
    #     param = {"id": order_id}
    #     r = requests.post(url,json=param,headers = self.headers)
    #     print(r.text)
    #
    # def test_post_04(self):
    #     data_url = "/json/stockin/ag"
    #     url = self.post_url + data_url
    #     param = {"id": order_id,"message":"","hoster":"manager"}
    #     r = requests.post(url,json=param,headers = self.headers)
    #     s= r.text
    #     self.assertIn("success",s)
    #     print(s)
    #
    # def test_post_05(self):
    #     data_url = "/json/stockin/purchase"
    #     url = self.post_url + data_url
    #     param = {"id": order_id,"warehouseTime":"2018-07-22+17%3A25"}
    #     r = requests.post(url,json=param,headers = self.headers)
    #     s = r.text
    #     self.assertIn("success",s)
    #     print(s)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
