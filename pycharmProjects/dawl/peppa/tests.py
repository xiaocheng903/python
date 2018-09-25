import socket
# Create your tests here.


def testconn(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((host,port))
        return 200
    except Exception:
        return 300
