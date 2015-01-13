__author__ = 'wxy'
import socket,sys,time
host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,e:
    print 'error creating socket:%s' % e
    sys.exit(1)
try:
    port = int(textport)
except ValueError:
    try:
        port = socket.getservbyname(textport,'tcp')
    except socket.error,e:
        print 'could not find you port:%s' %e
        sys.exit(1)
try:
    s.connect((host,port))
except socket.gaierror,e:
    print 'address-related error connecting to server %s' % e
    sys.exit(1)
except socket.error,e:
    print 'connection error:%s' %e
    sys.exit(1)
fd = s.makefile('rw',0)
print 'sleeping...'
time.sleep(1)
print 'continuing'
try:
    fd.write('Get %s Http \r\n'%filename)
except socket.error,e:
    print "error sending data:%s" %e
    sys.exit(1)
try:
    fd.flush()
except socket.error,e:
    print 'error sending data(detected by flush):%s' %e
    sys.exit(1)
try:
    s.shutdown(1)
    s.close()
except socket.error,e:
    print 'error sending data(detected by shutdown):%s' %e
    sys.exit(1)
while 1:
    try:
        buf = fd.read(2048)
    except socket.error,e:
        print "error receiving data:%s"%e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)