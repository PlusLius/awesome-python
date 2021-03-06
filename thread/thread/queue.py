import threading
import time
from Queue import Queue

def job(I,q):
    for i in range(len(I)):
        I[i] = I[i]**2
    q.put(I)

def multithreading(a):
    q = Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)


multithreading()


