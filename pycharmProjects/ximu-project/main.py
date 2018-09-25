# -*- coding:UTF-8 -*-
import os ,sys
#reload(sys)
#sys.setdefaultencoding('gbk')
from process.package import *

def package_setup(environment,*args):
    if environment =='t1':
        json_path='E:\\project\\ximu-project\\config\\test1.json'
    elif environment =='t2':
        json_path='E:\\project\\ximu-project\\config\\test2.json'
    elif environment =='t3':
        json_path='E:\\project\\ximu-project\\config\\test3.json'
    elif environment =='t5':
        json_path='E:\\project\\ximu-project\\config\\test5.json'
    elif environment =='t6':
        json_path='E:\\project\\ximu-project\\config\\test6.json'
    elif environment =='c':
        json_path='E:\\project\\ximu-project\\config\\ctest1.json'
    elif environment =='c2':
        json_path='E:\\project\\ximu-project\\config\\ctest2.json'
    else:
        raise ValueError('no supported test environment {}'.format(environment))
    support_command=['share','ce','cs','gap','dio_platform','dio','gds_platform','loan','openapi','uat_web','xmprod','accore','acfe','-a']
    for component in args[0]:
        if component not in support_command:
            raise ValueError(u'{} is not supported component,only {} is supported please check !'.format(component,support_command))

    if 'share' in args[0] or '-a' in args[0]:
        print('==============start install share module============================') 
        share = install_share(json_path)
        share.modify_configuration()
        time.sleep(1)
        share.install()
        time.sleep(2)
        print('==============start install share module============================')
        
if __name__=='__main__':
    package_setup(sys.argv[1],sys.argv[2:])
    