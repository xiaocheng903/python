#coding=utf-8
import unittest
import HTMLTestRunner
import time
import os
from email.mime.text import MIMEText
import smtplib
import configparser
# from common import readConfig
# localReadConfig = readConfig.ReadConfig()

#用例目录
test_suite_dir = './test_case/'
#报告目录
report_dir = './report/'
def creatsuite():
    testunit = unittest.TestSuite()
    #discover 方法定义
    discover = unittest.defaultTestLoader.discover(test_suite_dir, pattern = 'test*.py', top_level_dir = None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

alltestnames = creatsuite()

#定义发送邮件
def send_mail(file_new):
    config = configparser.ConfigParser()
    #读取config.ini文件
    a = config.read('./config/config.ini')
    sender = config.get('EMAIL','sender')
    sendpwd = config.get('EMAIL','sendpwd')
    #获取config数据
    receiver = config.get('EMAIL','receiver')
    print(receiver)
    #append不能使用str类型因此需要定义个一个列表，把值存进去
    b = []
    for n in str(receiver).split(","):
        b.append(n)
        print(b)
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,'html', 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect("smtp.263.net")
    smtp.login(sender,sendpwd)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print('email has send out')
#查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == "__main__":
    now = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
    filename = report_dir + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'接口测试报告',
        description=u'用例执行结果：')

    #执行测试用例
    runner.run(alltestnames)
    fp.close()
    file_path = new_report(report_dir)
    #发送测试报告
    send_mail(file_path)