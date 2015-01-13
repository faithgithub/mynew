__author__ = 'wxy'

def add_log(*args):
    def decorator(fun):
        def warp():
            fun()
            for i in args:
                print i
            print 'haha'
        return warp
    return decorator
@add_log('a','b')
def log():
    print 'nono'
log()