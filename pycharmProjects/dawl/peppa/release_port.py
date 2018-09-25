import socket
import sys

def port_status(ip,port):

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(2)
    try:
        port1 = int(port)
        sk.connect((ip, port1))
        return 0
    except Exception:
        return 1
    sk.close()

if __name__ == '__main__':

    ip = sys.argv[1]
    port = sys.argv[2]
    a = port_status(ip, port)
    print(a)

