import time
import threading

def get_detail_html(url):
    print 'get detail html started'
    time.sleep(2)
    print 'get detail html end'

def get_detail_url(url):
    print 'get detail url started'
    time.sleep(2)
    print 'get detail url end'

thread1 = threading.Thread(target=get_detail_html,args=("",))


thread2 = threading.Thread(target=get_detail_url,args=("",))

# thread1.setDaemon(True)
# thread2.setDaemon(True)

start_time = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print "last time: {}".format(time.time() - start_time)
