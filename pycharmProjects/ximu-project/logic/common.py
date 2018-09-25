# -*- coding:UTF-8 -*-
#实现通用功能
#2017-6-8
#xushuolei

import xml.dom.minidom as md
import parse_property_file as ppf
import json
import re , os ,time,sys
import codecs
import subprocess

from logic import logger,logger_install

#解析修改带定义beans的xml文件 
#key 待修改的属性值
#value 修改后的属性值
def modify_atypia_xml_bean(file_path,key,value):
    try:
        dom = md.parse(file_path)
        root = dom.documentElement
        beans = root.getElementsByTagName('bean')
        # 显示所有bean
        for bean in beans:
            if bean.getAttribute('id')=='targetConnectionFactory':
                properties=bean.getElementsByTagName('property')
                for property in properties:
                    if property.getAttribute('name')==key:
                        #logger.info(property.getAttribute('value'))
                        property.setAttribute('value',value)
                        #logger.info(property.getAttribute('value'))  
        data=codecs.open(file_path,'w','utf-8')        
        dom.writexml(data,encoding='utf-8')
        time.sleep(1)
        data.close()
    except Exception as e:
        logger.info ('modify xml failed ,error is %s '%(e))
        return False

#解析修改property文件 
#key 待修改的属性值
#value 修改后的属性值    
#失败返回False
def modify_common_file(file_path,key,value):
#    try:
    parser=ppf.Properties(file_path)
    parser.put(key,value)
#    except Exception as e:
#        logger.info('parse property file failed, error is %s !' %(e))
#        return False

#实现运行mvn命令
#input 需要输入的值
#waittime 窗口超时时间  -1为无限等待
def openconsole(input,path="E:\\checkoutversion\\version\\install.bat",waittime=60):
    
    inputcontent=str(input)
    dirname=os.path.dirname(path)
    os.chdir(dirname)
    os.system('mvn clean install -Denforcer.skip=true -Dmaven.test.skip=true -U')
    
def runinstall(path,module):
    dirname=os.path.dirname(path)
    os.chdir(dirname)
    logger.info(u'开始 {}!'.format(str(module)))
    response=subprocess.Popen('mvn clean install -Denforcer.skip=true -Dmaven.test.skip=true -U',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    standar_out=response.communicate()
    if standar_out[0].find("[Yes][No]")>=0:
        standar_out=response.communicate("No")  
    for raw in standar_out:
        logger_install.info(raw) 
    if standar_out[0].find("BUILD SUCCESS")>=0: 
        logger.info(u"{} 成功!".format(module))
        return True
    else:
       logger.info(u"{} 失败 ，有错误产生请查看日志!".format(module)) 
       return False
    
def read_json(json_path='E:\\project\\ximu-project\\config\\test2.json'):
    with open(json_path) as json_file:
        data=json.load(json_file)
    return data

def get_value_from_json(json_data,component_name,*args):
    component_value=json_data[component_name]
    valuelist=[]
    valuelist.append(component_value)
    for num in range(len(args)):  
        read_value=valuelist[-1][args[num]]      
        if isinstance(read_value,dict):
            valuelist.append(read_value)
        else:
            actural_value=read_value
    actural_value=valuelist[-1][args[len(args)-1]]
#    logger.info(actural_value)
    return actural_value

def delete_pause_from_install(bat_path):
    if os.path.exists(bat_path):
        origin_bat=open(bat_path)
        data=origin_bat.read()
        modify_data=re.sub('call pause','',data)
        origin_bat.close()
        modify_bat=open(bat_path,'w+')
        modify_bat.write(modify_data)
        modify_bat.close()
        time.sleep(1)
    else:
        logger.info('bat file not found in path %s'%bat_path)
        
def Window_to_Linux_File(window_path, Linux_path, Linux_ip, username, password,environment):    
    if environment== 't1':
           environment='testone' 
    elif environment== 't2':
            environment='testtwo'
    elif environment== 't3':
            environment='testthree'
    elif environment== 't5':
            environment='testfive'
    elif environment== 't6':
            environment='testsix'
    elif environment== 'c':
            environment='changjing'
    elif environment== 'c2':
            environment='changjing2'
    Linux_path = Linux_path.replace('test_environment',environment)
#    logger.info(Linux_path)
    try:
        os.chdir('C:\\Program Files\\PuTTY\\')
        logger.info("haha")
        cmd='pscp.exe -pw {password} {window_path} {username}@{Linux_ip}:{Linux_path}'.format(password=password, window_path=window_path, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path)    
        logger.info(cmd)
        os.system(cmd)
        time.sleep(5)
        logger.info('copy war file to linux successfully!')
    except:
        logger.info('copy war file to linux failed !')
    
def Window_to_Linux_Dir(window_path, Linux_path, Linux_ip, username, password):      
    try:
       os.chdir('C:\\Program Files\\PuTTY\\')
       cmd='pscp.exe -pw {password} -r {window_path} {username}@{Linux_ip}:{Linux_path}'.format(                password=password, window_path=window_path, username=username,Linux_ip=Linux_ip, Linux_path=Linux_path)   
       logger.info(cmd)
       os.system(cmd) 
       time.sleep(10)
       logger.info('copy dir file to linux successfully!')
    except:
        logger.info('copy dir file to linux failed !')
   
def gitclone_ximuprod(repourl):
    try:
        os.chdir('e:\\version')
        if os.path.exists('ximu-prod'):
            os.popen('RD /S/Q e:\\version\\ximu-prod')           
        os.popen('git clone '+repourl) 
        time.sleep(1)
        if os.path.exists('ximu-prod'):
            logger.info('clone ximu-prod code successfully!')

    except Exception as e:
        logger.info('clone produce some errors!')
               
        
    
 
   
                     
        
     
if __name__=='__main__':
    gitclone_ximuprod()
#    runinstall("E:\\version\\gds-shared\\")
#    delete_pause_from_install('e:\\install.bat')
   # modify_common_file('E:\\version\\cs\\antx.properties','gds.cs.message.center.address','abcd1234')
    #get_value_from_json(read_json('../config/data.json'),'shared','gds-shared-message-center-content','brokerURL')
        