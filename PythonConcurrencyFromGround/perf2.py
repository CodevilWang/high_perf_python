#!/usr/bin/env python
import sys
import time
from threading import Thread
from socket import *
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))
n = 0
def monitor():
    global n
    while True:
        time.sleep(1)
        print "{} reqs/pers".format(n)
        n = 0

Thread(target = monitor).start()
while True:
    start = time.time()
    sock.send(b'1')
    resp = sock.recv(100)
    n += 1