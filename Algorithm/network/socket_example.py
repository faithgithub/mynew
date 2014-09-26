__author__ = 'zxh'
import socket
print "Creating socket..."
#AF_INET IpV4 SOCK_STREAM tcp
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'done'

print 'looking up port number!'
port = socket.getservbyname('http','tcp')
print 'done'
print 'connecting to remote host on port %d'%port
s.connect(('wwww.baidu.com',port))
print 'done'
print "connected from",s.getsockname()
print 'connected to',s.getpeername()


#socketopts
solist = [x for x in dir(socket) if x.startswith('SO_')]
solist.sort()
for x in solist: print x