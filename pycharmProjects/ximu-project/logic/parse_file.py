# -*- coding:UTF-8 -*-

import xml.dom.minidom as md
import parse_property_file
import win32process
import win32event

# 获取所有<bean>节点
def getAllBean(file_path):  
    dom = md.parse(file_path)
    print(dom.toxml('utf-8'))
    root = dom.documentElement
    beans = root.getElementsByTagName('bean')
    # 显示所有bean
    for bean in beans:
        if bean.getAttribute('id')=='targetConnectionFactory':
            properties=bean.getElementsByTagName('property')
            for property in properties:
                if property.getAttribute('name')=='brokerURL':
                    print(property.getAttribute('value'))
                    property.setAttribute('value','789')
                    print(property.getAttribute('value'))  
    data=open(file_path,'w')          
    dom.writexml(data,encoding='utf-8')
    data.close()
    



# 获取所有property节点，以字典的的形式返回，属性名/property节点
def getAllProperty(beans):
    propList = {}
    for bean in beans:
        propertysE = bean.getElementsByTagName('property')
        for prop in propertysE:
            if prop.getAttribute('name')=='brokerURL':
                prop.setAttribute('name','456')


# 根据bean的属性id获取bean的class属性值
def getBeanClassAttr(beanid):
    bean = getBeanById(beanid)
    return bean.get('class')  # 获取节点属性为class的值


# 根据id获取bean节点
def getBeanById(beanid):
    beans = getAllBean()
    for bean in beans:
        id = bean.get('id')  # 获取属性名为id的值
        if beanid == id:
            return bean


# 根据bean的属性id获取其所有property节点
def getPropertysByBeanid(beanid):
    bean = getBeanById(beanid)
    props = bean.findall('property')
    return props;


# 根据bean的属性id和property的名称获取实际值
def getPropertyValue(beanid, proname):
    props = getPropertysByBeanid(beanid)
    for prop in props:
        name = prop.getAttribute('name')
        if proname == name:
            valueE = prop.find('value')
            if valueE != None:
                return valueE.text
            
def modify_ip(beanlist,key,value):
    if beanlist != []:
        for bean in beanlist:
            if bean.getAttribute('id')=='targetConnectionFactory':
                bean.setAttribute(key,value)
                
def modify_property_file(file_path):
    parser=parse_property_file.Properties(file_path)
    value=parser.get('gds.shared.message.center.redeliveryDelay')
    print(value)
    parser.put('gds.shared.message.center.redeliveryDelay', '500')
    value=parser.get('gds.shared.message.center.redeliveryDelay')
    print(value)
    
def modify_sample_file(file_path):
    parser=parse_property_file.Properties(file_path)
    value=parser.get('gds.cs.domain.server')
    print(value)
    parser.put('gds.cs.domain.server', '10.17.12.21')
    value=parser.get('gds.cs.domain.server')
    print(value)    
    
def openconsole(input,path="E:\\shared\\install.bat",waittime=-1):
    try:
        inputnumber=str(input)
        handle = win32process.CreateProcess(path, path+' '+inputnumber, None , None , 0 ,win32process.CREATE_NEW_CONSOLE , None , None ,win32process.STARTUPINFO())
        tm=win32event.WaitForSingleObject(handle[0], waittime)
        print(tm)
        return True
    except Exception as err:
        print('打开install.bat时有错误产生，错误是:%s'%str(err))
        return False
    
        


if __name__ == '__main__':
    flag=openconsole('')
    print(flag)
    #modify_sample_file('../config/antx.properties.sample')
#    modify_property_file('../config/sharedMessage.properties')
    
 # beans = getAllBean('../config/gds-shared-message-center-content.xml')
#    getAllProperty(beans)

    
    
    #print (getPropertyValue('userService', 'userDAO'))