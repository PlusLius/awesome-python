import time
import threading

class GetDetailHtml(threading.Thread):
    def run(self):
        print 'get detail html started'
        time.sleep(2)
        print 'get detail html end'

class GetDetailUrl(threading.Thread):
    def run(self):
        print 'get detail html started'
        time.sleep(2)
        print 'get detail url end'


thread1 = GetDetailHtml()
thread2 = GetDetailUrl()

start_time = time.time()

thread1.start()
thread2.start() 

thread1.join()
thread2.join()


print 'last time: {}'.format(time.time() - start_time)
