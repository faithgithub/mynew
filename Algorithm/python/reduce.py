__author__ = 'wxy'
def char2numlist(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
a = map(char2numlist, '13579')
print a
def char2num(s):
    return reduce(lambda x,y:x*10+y,map(char2numlist,s))
print char2num('123')