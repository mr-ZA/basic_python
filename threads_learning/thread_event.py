import threading
import time

# Mean of events is - if one thread is waiting for event,
# other is working ('cause of GIL) and generate the event

def producer():
    time.sleep(10)
    print("Product found!")
    product.set()       # warning for all listeners 'bout occured of event
    product.clear()     # clear event, for next wait(). If we'll remove this line - next product.wait() in the other threads will pass

def consumer():
    print("product wait")
    product.wait()              # waiter of event, when some thread call set(), blocker of wait() will stop and then -
    print("product exists")     # - we'll print()
    #product.wait()              # will be deadlock, 'cause of no second set() in def producer()

product = threading.Event()     # logic of event

th_1 = threading.Thread(target=producer)
th_2 = threading.Thread(target=consumer)

th_1.start()
th_2.start()

th_1.join()
th_2.join()