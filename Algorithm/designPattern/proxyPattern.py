__author__ = 'wxy'
class GiveGift:
    def giveDolls(self):
        pass

    def giveFlowers(self):
        pass
    def giveChocolate(self):
        pass
class SchoolGirl:
    def __init__(self,name):
        self.name = name

class Pursuit(GiveGift):
    def __init__(self,mm):
        self.mm = mm
    def giveDolls(self):
        print '%s give you doll' % self.mm

    def giveFlowers(self):
        print '%s give you flower' % self.mm
    def giveChocolate(self):
        print '%s give you chocolate' % self.mm
class Proxy(GiveGift):
    def __init__(self,mm):
        self.gg = Pursuit(mm)
    def giveDolls(self):
        self.gg.giveDolls()

    def giveFlowers(self):
        self.gg.giveFlowers()
    def giveChocolate(self):
        self.gg.giveChocolate()
if __name__ == '__main__':
    lucy = SchoolGirl('MM')
    dl = Proxy(lucy.name)
    dl.giveDolls()
    dl.giveFlowers()
    dl.giveChocolate()

