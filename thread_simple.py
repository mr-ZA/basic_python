import threading

def wr_file(file, num):
    with open (file, 'w') as f:
        for i in range (num):
            if num > 500:
                f.write('Многобукв\n')
            else:
                f.write('Малобукв\n')

thread1 = threading.Thread(target=wr_file, args=('Thread1_file', 200))
thread2 = threading.Thread(target=wr_file, args=('Thread2_file', 1000))
thread2 = threading.Timer (5.0, lambda : print("Hello world!"))

thread1.start()
thread2.start()

print (thread1.is_alive())
print (threading.enumerate())
print (thread1.getName())

thread1.join()
thread2.join()