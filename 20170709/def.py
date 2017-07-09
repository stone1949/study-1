#!/usr/bin/python

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
a = int(raw_input('input number : '))
print 'the number is %s' % my_abs(a)
#print my_abs(-1)