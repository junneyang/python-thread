#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import threading
import datetime

class MyThread(threading.Thread):
    def do1(self):
        global resA, resB
        if mutexA.acquire():
             msg = self.name+' got resA'
             print msg

             if mutexB.acquire(1):
                 msg = self.name+' got resB'
                 print msg
                 mutexB.release()
                 msg = self.name+' release resB'
                 print msg
             mutexA.release()
             msg = self.name+' release resA'
             print msg
    def do2(self):
        global resA, resB
        if mutexB.acquire():
             msg = self.name+' got resB'
             print msg

             if mutexA.acquire(1):
                 msg = self.name+' got resA'
                 print msg
                 mutexA.release()
                 msg = self.name+' release resA'
                 print msg
             mutexB.release()
             msg = self.name+' release resB'
             print msg


    def run(self):
        self.do1()
        self.do2()


def test():
    for i in range(50):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    resA = 0
    resB = 0

    mutexA = threading.Lock()
    mutexB = threading.Lock()
    test()

