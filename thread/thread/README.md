## 开启多线程

```py
1. 创建线程多开销比创建进程的开销小，因而创建线程的速度块
from multiprocessing import Process
form threading import Thread
import os
import time

def work():
  print os.getpid()
  time.sleep(2)
  print os.getpid()

if __name__ == '__main__':
  t = Thread(target=work,)
  t.start()
  print('主',os.getpid())
  
  
2. 用类的方式
from threading import Thread
import time
class work(Thread):
   def __init__(self,name):
      super().__init__()
      self.name = name
   def run(self):
       print self.name

if __name__ == "__main__":
   t = Work('egon')
   t.start()
   print('主')
```

## 线程的开启速度大于进程的开启速度

```py
from multiprocessing import Process
from threading import Thread
import time

def work():
   time.sleep(2)
   print('hello')

if __name__ == "__main__":
   t = Thread(target=work) #如果等上几秒，他会在开启的过程中打印主，如果不等会先打印hello
   # t = Process(target=work) # 子进程会先打印主
   
```

## 在同一个进程下开多个进程和开多个线程的pid的不同

```py
from multiprocessing import Process
from threading import Threa
import os
def work():
   print os.getpid()

if __name__ == '__main__':
  #在主进程下开启多个线程,每个线程都跟主进程的pid一样
  t1 = Thread(target=work)
  t2 = Thread(target=work)
  t1.start()
  t2.start()
  print os.getpid()
  
  #来多个进程，每个进程都有不同的pid
  p1 = Process(target=work)
  p2 = Process(target=work)
  p1.start()
  p2.start()
  print os.getpid()

```

## 同一进程内的线程共享该进程的数据

> 进程之间是相互隔离的，不共享，需要借助队列，管道，共享数据来完成

```py
from threading import Thread
from multiprocessing import Process
import os

def work():
  global n
  n-=1
  print n #所以被改成99了
n = 100

if __name__ == '__main__':
   # p = Process(target=work)
   p = Thread(target=work) #当开启的是线程的时候，因为同一进程内的线程之间共享进程内的数据,所以打印的n为99
   p.start()
   p.join()
   print '主{}'.format(n) #毫无疑问子进程p已经将自己的全局n改成了0，但改的仅仅是他自己的，查看父进程的n仍为100
```
