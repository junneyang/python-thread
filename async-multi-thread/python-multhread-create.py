#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import threading
import datetime


#函数调用式
def func(str_param):
    print("start...")
    for i in xrange(3):
        print(str_param+"-循环体"+str(i))
        time.sleep(1)
    print("end...")

def func_start():
    th_list=[]
    for i in xrange(2):
        th_list.append(threading.Thread(target=func,args=("thread-"+str(i),)))
    for th in th_list:
        th.start()
    for th in th_list:
        th.join()


#继承threading.Thread方式
class myth(threading.Thread):
    def __init__(self,name,str_param):
        threading.Thread.__init__(self,name=name)
        self.str_param=str_param
    def run(self):
        print("start...")
        for i in xrange(3):
            print(self.str_param+"-循环体"+str(i))
            time.sleep(1)
        print("end...")


def class_start():
    th_list=[]
    for i in xrange(2):
        th_list.append(myth("thread-"+str(i),"thread-"+str(i)))
    for th in th_list:
        th.start()
    for th in th_list:
        th.join()

#无锁状态
def func_unlock(str_param):
    global cnt

    print(str_param+"-操作开始")
    cnt+=1
    print cnt
    print(str_param+"-操作结束")

def func_unlock_start():
    th_list=[]
    for i in xrange(1000):
        th_list.append(threading.Thread(target=func_unlock,args=("thread-"+str(i),)))
    for th in th_list:
        th.start()
    for th in th_list:
        th.join()


if __name__ == '__main__':
    cnt=0
    '''func_start()
    class_start()'''
    starttime = datetime.datetime.now()
    func_unlock_start()
    print("cnt:"+str(cnt))
    endtime = datetime.datetime.now()
    test_time=(endtime-starttime).microseconds
    print("test_time:"+str(test_time))

