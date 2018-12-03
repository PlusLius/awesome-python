# -*-coding:utf8_*-
from multiprocessing import Process
from threading import Thread
import time

def work():
   # time.sleep(2)
    print('hello')

if __name__ == '__main__':
    t = Thread(target=work)
   # t = Process(target=work) #子进程会先打印主
    t.start()
    print('主')
