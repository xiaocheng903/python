import pymysql
from common import readConfig
localReadConfig = readConfig.ReadConfig()

class mysqldb:
    def configMysql(self):
        global host, port, user, passwd, database, charset, config
        host = localReadConfig.get_db("host")
        port = localReadConfig.get_db("port")
        user = localReadConfig.get_db("user")
        passwd = localReadConfig.get_db("passwd")
        database = localReadConfig.get_db("database")
        charset = localReadConfig.get_db("charset")
        config = {'host': str(host),
                  'user': user,
                  'passwd': passwd,
                  'port': int(port),
                  'database': database}
        self.db = pymysql.connect(**config)
                # create cursor
        self.cursor = self.db.cursor()
        print("Connect DB successfully!")
        # sql = "select * from cust_base_info where cust_code='custCode';"
        # self.cursor.execute(sql)
        # row = self.cursor.fetchall()
        # print(row)

if __name__ == "__main__":
    a= mysqldb()
    a.configMysql()
    print(id(a))


