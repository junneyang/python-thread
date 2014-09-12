#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import threading
import datetime

#加锁状态-函数式
def func_lock(str_param):
    global cnt
    if lock.acquire():
        print(str_param+"-获取锁")
        cnt+=1
        print cnt
    print(str_param+"-释放锁")
    lock.release()


def func_start_lock():
    th_list=[]
    for i in xrange(1000):
        th_list.append(threading.Thread(target=func_lock,args=("thread-"+str(i),)))
    for th in th_list:
        th.start()
    for th in th_list:
        th.join()


#加锁状态-继承threading.Thread
class myth_lock(threading.Thread):
    def __init__(self,name,str_param):
        threading.Thread.__init__(self,name=name)
        self.str_param=str_param
    def run(self):
        global sum
        if mutex.acquire():
            print(self.str_param+"-获取锁")
            sum+=1
            print sum
        print(self.str_param+"-释放锁")
        mutex.release()


def class_start_lock():
    th_list=[]
    for i in xrange(1000):
        th_list.append(myth_lock("thread-"+str(i),"thread-"+str(i)))
    for th in th_list:
        th.start()
    for th in th_list:
        th.join()

if __name__ == '__main__':
    cnt=0
    sum=0
    lock=threading.Lock()
    mutex=threading.Lock()

    starttime = datetime.datetime.now()
    func_start_lock()
    print("cnt:"+str(cnt))
    endtime = datetime.datetime.now()
    test_time=(endtime-starttime).microseconds
    print("test_time:"+str(test_time))

    starttime = datetime.datetime.now()
    class_start_lock()
    endtime = datetime.datetime.now()
    test_time=(endtime-starttime).microseconds
    print("test_time:"+str(test_time))

