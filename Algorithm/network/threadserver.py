__author__ = 'zxh'
import socket,traceback,os,sys
from threading import *
host =''
port = 51426
def handlechild(clientsock):
    print 'New child',currentThread().getName()
    print "Got connerction from ",clientsock.getpeername()
    while 1:
        data = clientsock.recv(4096)
        if  not len(data):
            break
        clientsock.sendall('%s:%s'%(clientsock.getpeername(),data))
    clientsock.close()
    print '%s closed' %clientsock.getpeername()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)
print 'server is runing'
while 1:
    try:
        clientsock,clientaddr = s.accept()
    except :
        traceback.print_exc()
        continue
    t = Thread(target= handlechild,args=[clientsock])
    t.setDaemon(1)
    t.start()