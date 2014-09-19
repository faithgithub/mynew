__author__ = 'zxh'
import time
n = raw_input('please enter the num:')
n = int(n)

a ={1:1,2:2}
def timeit(func):
    def wrapper(*args,**kwargs):
        print 'haha'
        start = time.clock()
        ret=func(*args,**kwargs)
        end =time.clock()
        print 'used:', end - start
        return ret
    return wrapper

def print_n(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return print_n(n-1)+print_n(n-2)

def print_n_fast(n,a):
    if n in a:
        return a[n]
    else:
        a[n] = print_n_fast(n-1,a)+print_n_fast(n-2,a)
        return a[n]
#print print_n(n)
print print_n_fast(n,a)
