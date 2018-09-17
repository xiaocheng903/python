import test_cookit
import json
url = "http://192.168.1.248:31100/json/stockin/add"
prams = {"copartnerId": 1165, "warehouseId": 165, "orderState": 1, "goods": [
    {"gid": 183167, "name": "【散】杜7月17测试单1", "type": "normal", "nums": 3, "suggestNum": 0, "dailySold": 0}],
         "contractId": 364}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
# prams = json.dumps(prams)
# print(prams)
test_cookit.get(url, prams, headers)
