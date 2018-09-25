import unittest
import requests
class get_request(unittest.TestCase):
    def setUp(self):
        self.get_url = "https://www.baidu.com/"

    def test_get_01(self):
        url=self.get_url
        print(url)
        r=requests.get(url,verify = False)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()