import unittest
from common import configMysql
client = configMysql.mysqldb()
sy = client.configMysql()
class post_requset(unittest.TestCase):
    def setUp(self):
        self.sql = ""

    def test_mysql_01(self):
        sql = "select * from goods where id = '125';"
        sy.execute(sql)
        row = sy.fetchall()
        print(row)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()


