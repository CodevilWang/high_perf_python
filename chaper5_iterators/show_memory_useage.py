#!/usr/bin/env python
'''
    对于range可以看到memory的明显增长
    相对于xrange没有明显增长
'''
import sys
import resource
import  time
import sys
range_flag = None
if sys.argv[1] == "range":
    range_flag = range
else:
    range_flag = xrange

# print init memory usage
cur_res = resource.getrusage(resource.RUSAGE_SELF)
print "init memory usage:"
print cur_res.ru_maxrss
sum = 0
for i in range_flag(0, 1000000):
    sum += i
    if i == 999999:
        cur_res = resource.getrusage(resource.RUSAGE_SELF)
        print "after range memory useage[{}]:".format(sys.argv[1])
        print cur_res.ru_maxrss
print sum