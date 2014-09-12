#!/usr/bin/env python
#-*- coding: utf-8 -*-

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            msg = self.name+' get num '
            print msg
            num = num+1
            msg = self.name+' set num to '+str(num)
            print msg
            mutex.acquire()
            msg = self.name+' get num '
            print msg
            mutex.release()
            msg = self.name+' release num '
            print msg
            mutex.release()
            msg = self.name+' release num '
            print msg

num = 0
#mutex = threading.Lock()
#使用可重入锁进行规避
mutex = threading.RLock()
def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()

