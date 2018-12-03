import threading

def thread_job():
    print threading.current_thread()


def main():
    print threading.active_count()
    print threading.enumerate()
    print threading.current_thread()
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    

if __name__=="__main__":
    main()
