import pymysql
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user='root',
    password='123456',
    database="practice"
)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select sno,sname,class as Aclass from students limit 1'
cursor.execute(sql)
results = cursor.fetchall()
print(results)
for row in results:
    print(row)
    sno = row['sno']
    sname = row['sname']
    Aclass = row['Aclass']
    print(sno)
    print(sname)
    print(Aclass)
    # print("sno,sname=%s,Aclass=%d" % \
    #       (sno, sname, Aclass))
cursor.close()
conn.close()