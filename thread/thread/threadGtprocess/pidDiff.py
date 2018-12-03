# -*-coding:utf8-*-
from multiprocessing import Process
from threading import Thread
import os

def work():
    print 'hello{}'.format(os.getpid())

if __name__ == '__main__':
    #在主进程下开启多个线程，每个线程都跟主进程的pid一样
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    print '主线程pid{}'.format(os.getpid())

    #来多个进程，每个进程都有不同的pid
    p1 = Process(target=work)
    p2 = Process(target=work)
    p1.start()
    p2.start()
    print '主进程pid{}'.format(os.getpid())
