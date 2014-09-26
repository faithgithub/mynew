__author__ = 'zxh'
#print( ''.join( sorted( a ,key = lambda x : ord( x.lower( ) ) * 2 + x.islower( ) ) ) )
def get_single(word):
    word = word.lower()
    single_word = ''.join(sorted(word,key= lambda x:ord(x)))
    return single_word
a = 'test'
print get_single(a)
