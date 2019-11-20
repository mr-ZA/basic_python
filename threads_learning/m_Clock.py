from threading import Thread
import time

# Function variant
# def clock (interval):
#     while True:
#         print ("Current time is: %s" % time.ctime())
#         time.sleep(interval)
#
# t = Thread (target = clock, args = (15, ))
# t.daemon = True
# t.start()

# OOP variant
class ClockThread (Thread):
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval

    def run(self):
        while True:
            print("Current time is: %s" % time.ctime())
            time.sleep(self.interval)

t = ClockThread(15)
t.start()