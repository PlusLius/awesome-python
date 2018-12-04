from threading import Thread,Lock
import time
n = 100

def work():
    mutex.acquire()
    global n
    temp = n
    time.sleep(0.01)
    n = temp -1
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    s = time.time()
    for i in range(100):
        t = Thread(target=work)
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()
    print "{}:{}".format(time.time()-s,n)
