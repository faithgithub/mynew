__author__ = 'zxh'
import socket,sys
port = 70
host = sys.argv[1]
filename = sys.argv[2]
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((host,port))
except socket.gaierror,e:
    print 'Error connecting to sever :%s' % e
    sys.exit(1)
def send():
    s.sendall(filename+"\r\n")
    while 1:
        buf = s.recv(2048)
        if not  len(buf):
            break
        sys.stdout.write(buf)
def send2():
    fd = s.makefile('rw',0)
    fd.write(filename+"\r\n")
    for line in fd.readlines():
        sys.stdout.write(line)


def easy_gopherclient():
    pass
def urllib_client():
    import urllib,sys
    f = urllib.urlopen(sys.argv[1])
    while 1:
        buf = f.read(2048)
        if not  len(buf):
            break
        sys.stdout.write(buf)
