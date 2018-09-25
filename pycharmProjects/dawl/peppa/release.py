import paramiko

class ParamikoClient:


    def __init__(self):

        self.client = paramiko.SSHClient()

        self.private_key=paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    def connect(self,ip):
        try:
            self.client.connect(
                hostname=ip,
                port=22,
                username='root',
                pkey=self.private_key
            )
        except Exception as e:
            print(e)
            try:
                self.client.close()
            except:
                pass
    def runcmd(self,cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        res_out=stdout.read().decode()
        print(res_out)

    def close_connect(self):

        self.client.close()


    def transport(self,ip):

        trans=paramiko.Transport((ip,22))
        trans.connect(username='root',pkey=self.private_key)
        self.client._transport=trans
        sftp=paramiko.SFTPClient.from_transport(trans)
        sftp.put(localpath='/Users/wangle/test/a.txt',remotepath='/root/test/b.txt')
        trans.close()




if __name__=='__main__':
    client=ParamikoClient()
    client.transport('192.168.1.105')





