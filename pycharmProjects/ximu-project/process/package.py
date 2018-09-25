#-*-coding:utf-8-*-
###################################
#实现自动打包的主流程
#2017-6-8
#xushuolei

import shutil
import os, time,sys
#reload(sys)
#sys.setdefaultencoding('gbk')
from logic import common
import paramiko
from process import logger
class install_share:

    def __init__(self,json_path):
        self.json_path=json_path
        self.url = common.get_value_from_json(common.read_json(self.json_path), 'shared', 'url')
        self.console_path = common.get_value_from_json(common.read_json(self.json_path), 'shared', 'console-path')

    def modify_configuration(self):
        common.modify_atypia_xml_bean(self.message_center_path, 'brokerURL', self.message_center_value)
        common.modify_common_file(self.share_message_path, 'gds.shared.message.center.address', self.share_message_value)

    def install(self):
        return common.runinstall(self.console_path,self.__class__.__name__)
    # 把打成的包上到linux  服务器
    def copyfile_tolinux(self, environment):
        common.Window_to_Linux_File(self.war_path, self.war_path_linux, self.linux_ip, self.linux_username, self.linux_password, environment)
        
class  connection:
    
    def __init__(self,json_path):
        self.json_path=json_path
        self.ip = common.get_value_from_json(common.read_json(self.json_path), 'ftpconfig', 'ip')          
        self.port = int(common.get_value_from_json(common.read_json(self.json_path), 'ftpconfig', 'port'))   
        self.username = common.get_value_from_json(common.read_json(self.json_path), 'ftpconfig', 'username')   
        self.password = common.get_value_from_json(common.read_json(self.json_path), 'ftpconfig', 'password') 
    def excute_command1(self, *args):
#        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, self.port, self.username, self.password, timeout=5)  
            output=[]
            chan=ssh.invoke_shell()
            stdin = chan.makefile('wb')
            stdout = chan.makefile('rb')
            stdin.write('ls')
            stdin.write('./dio/bin/startup.sh')
            stdin.flush()
            print(stdout.read())
            stdout.close()
            stdin.close()
            ssh.close()
            return output

    def excute_command(self, *args):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, self.port, self.username, self.password, timeout=5)  
            output=[]  
            for cmd in args:       
                stdin, stdout, stderr = ssh.exec_command(cmd)                  
                out = stdout.readlines()
                output.append(out)
            ssh.close()
            return output
        except:
            logger.info('excute cmd {} failed!'.format(args))
            ssh.close()
            return False

    def handle_component_service(self, environment, component, flag):
        support_component = ['cs', 'dio', 'loan', 'openapi', 'gap', 'uat_web','xmprod','accore','acfe']
        support_environment = ['t1', 't2', 't3','t5','t6', 'c', 'c2']
        date = time.strftime('%y%m%d%H%M%S', time.localtime(time.time()))   
        if environment not in support_environment:
            raise Exception('{} is not supported test environment!'.format(environment))
        if component not in support_component:
            raise Exception('{} is not supported component!'.format(environment))       
        if component == 'gap':
            service_path = u'/loan/bin/'
            war_path = u'/loan/webapps/gds-gap-web.war'
            start_service_cmd = u'docker exec ' + environment + 'loan' + ' .' + service_path + 'startup.sh'
#            enter_docker_cmd = u'docker exec -it '+environment+'loan '+'/bin/bash'
#            start_service_cmd = u'.' + service_path + 'startup.sh'
            stop_service_cmd = u'docker exec ' + environment + 'loan' + ' .' + service_path + 'shutdown.sh'
            copy_cmd = u'docker exec ' + environment + 'loan' + ' cp ' + war_path + ' /root/'+component + date + '.war'
            remove_cmd = u'docker exec ' + environment + 'loan' + ' rm -rf ' + war_path.split('.')[0] + '/'
            kill_cmd = u'docker exec ' + environment + 'loan' + ' kill -9 '
            ps_cmd = u'docker exec ' + environment + 'loan' + ' ps -ef | grep java' 
        elif component == 'openapi':
            service_path = u'/openapi/bin/'
            war_path = u'/openapi/webapps/gds-openapi-web.war'
            start_service_cmd = u'docker exec ' + environment + component + ' .' + service_path + 'startup.sh'
            stop_service_cmd = u'docker exec ' + environment + component + ' .' + service_path + 'shutdown.sh'
            copy_cmd = u'docker exec ' + environment + component + ' cp ' + war_path + ' /root/'+component + date + '.war'
            ps_cmd = u'docker exec ' + environment + component + ' ps -ef | grep java' 
            kill_cmd = u'docker exec ' + environment + component + ' kill -9 '
            remove_cmd = u'docker exec ' + environment + component + ' rm -rf ' + war_path.split('.')[0] + '/'
        elif component == 'uat_web':
            service_path = u'/openapi/bin/'
            war_path = u'/openapi/webapps/ROOT.war'
#            enter_docker_cmd = u'docker exec -it '+environment+'openapi '+'/bin/bash'
#            start_service_cmd = u'.' + service_path + 'startup.sh'
            stop_service_cmd = u'docker exec ' + environment + 'openapi' + ' .' + service_path + 'shutdown.sh'
            start_service_cmd = u'docker exec ' + environment + 'openapi' + ' .' + service_path + 'startup.sh'
            ps_cmd = u'docker exec ' + environment + 'openapi' + ' ps -ef | grep java'             
            copy_cmd = u'docker exec ' + environment + 'openapi' + ' cp ' + war_path + ' /root/'+component + date + '.war'
            remove_cmd = u'docker exec ' + environment + 'openapi' + ' rm -rf ' + war_path.split('.')[0] + '/'
            kill_cmd = u'docker exec ' + environment + 'openapi' + ' kill -9 '
        elif component == 'accore':
            service_path = u'/accore/bin/'
            war_path = u'/accore/webapps/gds-ac-core-web.war'
            start_service_cmd = u'docker exec ' + environment + component + ' .' + service_path + 'startup.sh'
            stop_service_cmd = u'docker exec ' + environment + component + ' .' + service_path + 'shutdown.sh'
            copy_cmd = u'docker exec ' + environment + component + ' cp ' + war_path + ' /root/'+component + date + '.war'
            ps_cmd = u'docker exec ' + environment + component + ' ps -ef | grep java' 
            kill_cmd = u'docker exec ' + environment + component + ' kill -9 '
            remove_cmd = u'docker exec ' + environment + component + ' rm -rf ' + war_path.split('.')[0] + '/'
        elif component == 'acfe':
            service_path = u'/acfe/bin/'
            war_path = u'/acfe/webapps/ROOT.war'
            start_service_cmd = u'docker exec ' + environment + component + ' .' + service_path + 'startup.sh'
            stop_service_cmd = u'docker exec ' + environment + component + ' .' + service_path + 'shutdown.sh'
            copy_cmd = u'docker exec ' + environment + component + ' cp ' + war_path + ' /root/'+component + date + '.war'
            ps_cmd = u'docker exec ' + environment + component + ' ps -ef | grep java' 
            kill_cmd = u'docker exec ' + environment + component + ' kill -9 '
            remove_cmd = u'docker exec ' + environment + component + ' rm -rf ' + war_path.split('.')[0] + '/'
        elif component == 'xmprod':
            service_path = u'/xmprod/bin/'
            war_path = u'/xmprod/webapps/ximu-prod-web.war'
            start_service_cmd = u'docker exec ' + environment + component + ' .' + service_path + 'startup.sh'
            stop_service_cmd = u'docker exec ' + environment + component + ' .' + service_path + 'shutdown.sh'
            copy_cmd = u'docker exec ' + environment + component + ' cp ' + war_path + ' /root/'+component + date + '.war'
            ps_cmd = u'docker exec ' + environment + component + ' ps -ef | grep java' 
            kill_cmd = u'docker exec ' + environment + component + ' kill -9 '
            remove_cmd = u'docker exec ' + environment + component + ' rm -rf ' + war_path.split('.')[0] + '/'
              
        else:
            service_path = u'/' + component + '/bin/'
            war_path = u'/' + component + '/webapps/ROOT.war'
#            enter_docker_cmd = u'docker exec -it '+environment+component+' /bin/bash'
#            start_service_cmd = u'.' + service_path + 'startup.sh'
            start_service_cmd = u'docker exec ' + environment + component + ' .' + service_path + 'startup.sh'
            stop_service_cmd = u'docker exec ' + environment + component + ' .' + service_path + 'shutdown.sh'                    
            copy_cmd = u'docker exec ' + environment + component + ' cp ' + war_path + ' /root/'+component + date + '.war'
            ps_cmd = u'docker exec ' + environment + component + ' ps -ef | grep java' 
            kill_cmd = u'docker exec ' + environment + component + ' kill -9 '
            remove_cmd = u'docker exec ' + environment + component + ' rm -rf ' + war_path.split('.')[0] + '/'

        logger.info(start_service_cmd)  
        logger.info(stop_service_cmd)             
        logger.info(copy_cmd)
        logger.info(ps_cmd)
        logger.info(kill_cmd)
        if flag == 'stop':
            out = self.excute_command(ps_cmd)
            logger.info(out)
            if out != [[]]:
                for lists in out:
                    for content in lists:
                        pid = content.split()[1]
                        logger.info(pid)
                kill_pid = self.excute_command(kill_cmd + pid)
                logger.info(kill_pid)
                time.sleep(1)
            bak_file = self.excute_command(copy_cmd)
            #sometimes can not find the ROOT folder,so add this logic
            exist_root = self.excute_command(u'docker exec ' + environment + component + ' ls ' + war_path.split('.')[0])
#            logger.info(exist_root)
            no_exit = True
            for exist_str in exist_root:
                for exist in exist_str:
                    if exist.find('No such file or directory') >= 0:
                        logger.info('No such file or directory in {}'.format(war_path))
                        no_exit = False
            if no_exit:
                logger.info(u'remove cmd 是 '+remove_cmd)
                remove_root = self.excute_command(remove_cmd)
                logger.info(remove_root)
                logger.info(u'delete '+environment+component +' successfully')
            time.sleep(1)
        elif flag == 'start':
#            logger.info(enter_docker_cmd)
            logger.info(start_service_cmd)
            out = self.excute_command(start_service_cmd)
            time.sleep(1)
            logger.info(out)
        else:
            logger.info('no support type!')
        
        
                
if __name__ == '__main__':
    aa=connection("E:\\project\\ximu-project\\config\\test5.json")
    out=aa.excute_command('docker exec t1loan ps -ef | grep java')
    print(out)
