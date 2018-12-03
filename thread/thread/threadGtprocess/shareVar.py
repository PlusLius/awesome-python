# -*-coding:utf8-*-
from threading import Thread
from multiprocessing import Process
import os

def work():
    global n
    n -=1
    print(n) 

n = 100

if __name__ == '__main__':
    p = Process(target=work)
   # p = Thread(target=work)

    p.start()
    p.join()
    print '主{}'.format(n)
