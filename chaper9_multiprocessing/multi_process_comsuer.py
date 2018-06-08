#!/usr/bin/env python
import os
import sys
from multiprocessing import Value, Process
import datetime

def show_date(cursor, queue):
    while True:
        current_curosr = -1
        with cursor.get_lock():
            current_curosr = cursor.value
            cursor.value += 1
        if current_curosr >= len(queue):
            return
        print "{}\t{}".format(os.getpid(),
                              datetime.datetime.strftime(queue[current_curosr], "%Y%m%d"))

if __name__ == '__main__':
    parallel = int(sys.argv[1])
    end_date_str = sys.argv[2]
    end_date = datetime.datetime.strptime(end_date_str, "%Y%m%d")
    interval = int(sys.argv[3])
    date_list = []
    cursor = Value('i', 0)
    for i in range(interval):
        cur_date = end_date - datetime.timedelta(days = i)
        date_list.append(cur_date)
    p_list = []
    for i in range(parallel):
        p_list.append(Process(target = show_date, args = (cursor, date_list)))
    for p in p_list: 
        p.start()
    for p in p_list:
        p.join()

# for x in date_list:
#     print datetime.datetime.strftime(x, "%Y%m%d")
