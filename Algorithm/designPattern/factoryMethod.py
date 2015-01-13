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
class LeiFengFactory:
    def CreateLeiFeng(self):
        temp = LeiFeng()
        return temp

class StudentFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Student()
        return temp

class VolenterFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Volunteer()
        return temp

if __name__ == "__main__":
    sf = StudentFactory()
    s=sf.CreateLeiFeng()
    s.sweep()
    sdf = VolenterFactory()
    sd=sdf.CreateLeiFeng()
    sd.wash()
