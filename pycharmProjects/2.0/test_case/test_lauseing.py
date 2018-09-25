#coding=utf-8
import json,unittest,requests
from common import readConfig

localReadConfig = readConfig.ReadConfig()

class test_selectCustLaBaseInfo(unittest.TestCase):
    def setUp(self):
        self.http_url = localReadConfig.get_http('url')
        self.port = localReadConfig.get_port('la_port')
        pass

    def tearDown(self):
        pass

    def test_selectCustLaBaseInfo(self):
        json_path = './data/la_selectCustLaBaseInfo.json'
        data_url = "/laBaseInfo/selectCustLaBaseInfo"
        url = self.http_url+":"+ self.port + data_url
        #payload = "{\r\n  \"id\": 3\r\n}"
        with open(json_path, 'rb') as f:
            payload = json.loads(f.read())
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=data, headers=headers).json()
        print(response)
        self.assertEqual(response['code'], 200)
    def test_custLaOperation(self):
        json_path = './data/la_custLaOperation.json'
        data_url = "/laBaseInfo/custLaOperation"
        url = self.http_url+":"+ self.port + data_url
        # payload = "{\r\n  \"phoneNumber\": 13795350295\r\n}"
        with open(json_path, 'rb') as f:
            payload = json.loads(f.read())
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=data, headers=headers).json()
        print(response)
        a = response['obj']
        self.assertEqual(response['code'],200)

    def test_laTemporaryRecord(self):
        json_path = './data/la_TemporaryRecord.json'
        dataurl = "/laTemporaryRecord/list"
        url = self.http_url +":"+ self.port + dataurl
        with open(json_path, 'rb') as f:
            payload = json.loads(f.read())
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=data, headers=headers).json()
        print(response)
        self.assertEqual(response['code'], 200)

    def test_laTemporaryRecordinsert(self):
        data_url = "/laTemporaryRecord/insert"
        json_path = '../data/la_TemporaryRecordinsert.json'
        url = self.http_url+":" + self.port + data_url
        with open(json_path, 'rb') as f:
            payload = json.loads(f.read())
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=data, headers=headers).json()
        print(response)
        self.assertEqual(response['code'], 200)

if __name__ == '__main__':
    unittest.main()
