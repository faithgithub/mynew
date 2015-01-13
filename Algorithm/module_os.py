__author__ = 'wxy'
import os
print os.getcwd()
#os.chdir('/tmp')
print(os.path.expanduser('~'))
print(os.path.join(os.path.expanduser('~'), 'wxy'))
os.path.split(os.path.expanduser('~'))
import glob
print glob.glob('/Users/zxh/wxy/*')
os.stat('/Users/zxh/wxy/tpl')
print os.path.realpath('study.py')
print [os.path.realpath(f) for f in glob.glob('*.py')]
metadata_dict = {f:os.stat(f) for f in glob.glob('*i*.py')}
a_dict = {'a': 1, 'b': 2, 'c': 3}
b_dict = {value:key for key,value in a_dict}