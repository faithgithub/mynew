# coding=utf-8
__author__ = 'wxy'
'''
但是，如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
从object派生的话就是new style class，不带object就是classic class。具体的区别建议你去python.org的文档中有专题介绍。new style class支持内置类型的派生，可以处理metaclass(元类)，还有property(属性)，总之是一些相对高级的特性，以后也许会全部使用new style class。不学关系也不是很大。
'''
from types import MethodType
class Student:
    pass
def set_age(self,age):
    self.age = age
s = Student()
s.name = 'wxy'
print s.name
s.set_age = MethodType(set_age,s,Student)
s.set_age(24)
print s.age
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score,None,Student)
s2 = Student()
s2.set_score(100)
print s2.score
class Student2(object):
    __slots__ = ('name',)
s3 = Student2()
s3.name =9
print s3.name
s3.cc =8
print s3.cc