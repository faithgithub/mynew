import time
#1、装饰着模式，切面编程 
def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper
@timeit
def foo():
    print 'in foo()',foo.__name__
 
foo()
#2、这是一个很有用的装饰器。看过前一篇反射的朋友应该知道，函数是有几个特殊属性比如函数名，在被装饰后，上例中的函数名foo会变成包装函数的名字wrapper，如果你希望使用反射，可能会导致意外的结果。这个装饰器可以解决这个问题，它能将装饰过的函数的特殊属性保留。
import functools
 
def timeit(func):
    @functools.wraps(func)
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
    return wrapper
 
@timeit
def foo():
    print 'in foo()'
 
foo()
print foo.__name__
#3、:增强函数(装饰)函数,记住每个已经计算的Fibonacci值;如果它们在缓存中,就不需要再计算了. 
from functools import wraps 
def memo(f): 
    cache = { } 
    @wraps(f) 
    def  wrap(*arg): 
        
        if arg not in cache: cache['arg'] = f(*arg) 
        return cache['arg'] 
    return wrap
@memo
def fib(i):
    if i<2: return 1
    return fib(i-1)+fib(i-2)
