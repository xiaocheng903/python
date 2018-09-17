#coding=utf-8
import json ,unittest ,requests
from common import readConfig
import random
localReadConfig = readConfig.ReadConfig()

class test_loanManagerment(unittest.TestCase):
    def setUp(self):
        self.http_url = localReadConfig.get_http('url')
        self.port = localReadConfig.get_port('loan_port')
        pass

    def tearDown(self):
        pass

    #场景方进入支用申请
    def test1_dsbsApplyPlfm(self):
        json_path = "./data/loan_dsbsApplyPlfm.json"
        data_url = "/dsbsApply/dsbsApplyPlfm"
        url = self.http_url + ":" + self.port + data_url
        print(url)
        with open(json_path, 'rb') as f:
            payload = json.loads(f.read())
        a = "".join(random.choice("1234567") for i in range(6))
        payload['plfmLoanOrderNo'] = a
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST",url, data=data, headers=headers).json()
        a = response['obj']
        print(a)
        dsbsApplyNo = str(a).split("=")[1]
        return dsbsApplyNo
        self.assertEqual(response['code'], 200)
    #支用申请-初始化页面
    def test2_dsbsApplyInit(self):
        dsbsApplyNo = self.test1_dsbsApplyPlfm()
        json_path = "./data/loan_dsbsApplyInit.json"
        data_url = "/dsbsApply/dsbsApplyInit"
        url = self.http_url + ":" + self.port + data_url
        print(url)
        payload  = dsbsApplyNo
        print(dsbsApplyNo)
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=data, headers=headers).json()
        print(response)
        print(2)
        # self.assertEqual(response['code'], 200)
    #支用申请提交
    def test3_dsbsApplyInit(self):
        dsbsApplyNo = self.test1_dsbsApplyPlfm()
        json_path = "./data/loan_dsbsApplyCommit.json"
        data_url = "/dsbsApply/dsbsApplyCommit"
        url = self.http_url + ":" + self.port + data_url

        with open(json_path, 'rb') as f:
            payload = json.loads(f.read())
            payload['dsbsApplyNo'] = dsbsApplyNo
            print(dsbsApplyNo)
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST",url, data=data, headers=headers).json()
        print(response)
        print(3)
        self.assertEqual(response['code'], 200)
if __name__ == '__main__':
    unittest.main()