#!/usr/bin/env python
#-*- coding: utf-8 -*-
import socket
import threading
import datetime
req=0
res=0
starttime = datetime.datetime.now()


def func():
    global req,res
    while 1:
        message = "GET /helloworld?user=yangjun HTTP/1.0 \r\n\r\n"

        server = ('localhost',8421)
        clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientsocket.connect(server)


        clientsocket.sendall(message)
        req+=1
        response = clientsocket.recv(4096)
        #print response
        res+=1
        clientsocket.close()

if __name__ == '__main__':
    '''th_list=[]
    for i in xrange(100):
        th_list.append(threading.Thread(target=func,args=()))
    try:
        for th in th_list:
            th.start()
        for th in th_list:
            th.join()'''
    try:
        func()
    except KeyboardInterrupt:
        endtime = datetime.datetime.now()
        test_time=(endtime-starttime).seconds
        print test_time
        print req
        print res



