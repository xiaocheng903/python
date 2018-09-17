#coding=utf-8
import json,unittest,requests
from common import readConfig

localReadConfig = readConfig.ReadConfig()

class getLivingInfo(unittest.TestCase):
    def setUp(self):
        self.http_url = localReadConfig.get_http('url')
        self.port = localReadConfig.get_port('idvr_port')
        pass

    def tearDown(self):
        pass
    #获取验证码
    def test1_sendMpvc(self):
        json_path = './data/idvr_sendMpvc.json'
        data_url = "/idvrVrPhoneRecord/sendMpvc"
        url = self.http_url +":"+ self.port + data_url
        with open(json_path, 'rb') as f:
            payload = json.loads(f.read())
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=data, headers=headers).json()
        return response['obj']
        self.assertEqual(response['code'],200)
    #验证码验证
    def test2_idvrVrPhoneRecord(self):
        a = self.test1_sendMpvc()
        print(a)
        json_path = './data/idvr_VrPhoneRecord.json'
        data_url = "/idvrVrPhoneRecord/insert"
        url = self.http_url+':'+ self.port + data_url
        with open(json_path, 'rb') as f:
            payload = json.loads(f.read())
            payload['mpvc'] = a
            payload['vcSubmited'] = a
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=data, headers=headers).json()
        return payload['idvrId']
        self.assertEqual(response['code'],200)

    def test3_idvrVrPhoneRecordgetPhone(self):
        b = self.test2_idvrVrPhoneRecord()
        json_path = './data/idvr_VrPhoneRecordgetPhone.json'
        date_url = "/idvrVrPhoneRecord/getPhone"
        url = self.http_url + ':' + self.port + date_url
        with open(json_path, 'rb') as f:
            payload = json.loads(f.read())
            payload['idvrId']= b
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=data, headers=headers).json()
        self.assertEqual(response['code'],200)

if __name__ == '__main__':
    unittest.main()
