#coding=utf-8
import json ,unittest ,requests
from common import readConfig

localReadConfig = readConfig.ReadConfig()

class test_identityAuthentication(unittest.TestCase):
    def setUp(self):
        self.http_url  = localReadConfig.get_http('url')
        self.port = localReadConfig.get_port('idvr_port')
        pass

    def tearDown(self):
        pass

    def test_idvrVrBiopsyRecord(self):

        json_path = "./data/idvr_VrBiopsyRecord.json"
        data_url = "/idvrVrBiopsyRecord/insert"
        url = self.http_url + ":" + self.port + data_url

        with open(json_path, 'rb') as f:
            payload = json.loads(f.read())
        data = json.dumps(payload)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        response = requests.request("POST",url, data=data, headers=headers).json()
        print(response)
        self.assertEqual(response['code'], 200)

if __name__ == '__main__':
    unittest.main()
