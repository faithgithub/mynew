__author__ = 'wxy'
import socket,sys,struct,time
hostname = 'time.nist.gov'
port = 37
host = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto('',(host,port))
print 'looking for replies,press ctrl-c to stop'
buf = s.recvfrom(2048)[0]
if len(buf)!=4:
    print 'wrong size reply %s:%s'%(len(buf),buf)
    sys.exit(1)
secs = struct.unpack('!I',buf)[0]
secs -= 2208988800
print time.ctime(int(secs))