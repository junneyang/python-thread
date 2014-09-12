#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import Queue
import time

class Producer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.data=queue
    def run(self):
        for i in range(10000):
            '''if self.data.qsize() > 1000:
                pass
            else:'''
            print("PUT DATA:"+str(i))
            self.data.put(i)

class Consumer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.data=queue
    def run(self):
        for i in range(4000):
            Data=self.data.get()
            print("GET DATA:"+str(Data)+",Result:"+str(Data*Data))

def main():
    queue = Queue.Queue()
    p_list=[]
    c_list=[]
    for i in range(2):
        p=Producer(queue)
        p_list.append(p)
        p.start()
    for i in range(5):
        c=Consumer(queue)
        c_list.append(c)
        c.start()
    for p in p_list:
        p.join()
    for c in c_list:
        c.join()

if __name__ =='__main__':
    main()

