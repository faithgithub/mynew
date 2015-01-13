# coding=utf-8
'''
装饰者模式
'''
class Person:
    def __init__(self,name):
        self.name = name
    def show(self):
        print 'dressed %s' % self.name
class Finery(Person):
    def __init__(self):
        pass
    def decorate(self,ct):
        self.component = ct
    def show(self):
        if self.component:
            self.component.show()
class TShirts(Finery):
    def __init__(self):
        pass
    def show(self):
        print "Big T-shirt "
        self.component.show()
class BigTrouser(Finery):
    def __init__(self):
        pass
    def show(self):
        print "Big Trouser "
        self.component.show()
if __name__ == "__main__":
    p = Person("wxy")
    bt = BigTrouser()
    ts = TShirts()
    bt.decorate(p)
    ts.decorate(bt)
    ts.show()