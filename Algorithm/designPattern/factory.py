# coding=utf-8
__author__ = 'wxy'
class LeiFeng:
    def __init__(self):
        self.name = '雷锋'
    def sweep(self):
        print '%s 扫地' % self.name
    def wash(self):
        print '%s 洗衣'% self.name
    def cook(self):
        print '%s 做饭'% self.name
class Student(LeiFeng):
    def __init__(self):
        self.name = '学生'

class Volunteer(LeiFeng):
    def __init__(self):
        self.name = '志愿者'
class SimpleFactory:
    def __init__(self):
        pass
    def createLeiFeng(self,name):
        op = {
            'student':'Student()',
            'volunteer':'Volunteer()'
        }
        a= eval(op[name])
        return a
if __name__=='__main__':
    p = SimpleFactory().createLeiFeng('student')
    p.wash()
