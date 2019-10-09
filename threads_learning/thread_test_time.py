import threading
import time

def handler(started = 0, finished = 0):
    result = 0
    for i in range(started, finished):
        result += i
    results.append(result)

results = []

task1 = threading.Thread(target=handler, kwargs={'finished': 2 **12})
task2 = threading.Thread(target=handler, kwargs={'started': 2 **12, 'finished': 2 ** 24})

started_at = time.time()

task1.start()
task2.start()

task1.join()
task2.join()

print("RESULTS 1 thread here")
print("Time: {}".format(time.time() - started_at))

results = []
started_at = time.time()
handler(finished = 2**24)
print("RESULTS no_Thread")
print("Time: {}".format(time.time() - started_at))