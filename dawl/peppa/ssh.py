import paramiko
from peppa import release



client=release.ParamikoClient()
client.connect('192.168.1.105')
client.runcmd('date')



