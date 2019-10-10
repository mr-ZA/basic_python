import threading

print(threading.active_count())
current = threading.current_thread()
print(current.getName())                # in default - MainThread
print(current.is_alive())
print(current.isDaemon())
print("\n")

# Trying to restart Main thread
try:
    current.start()
except RuntimeError as e:
    print("ERROR: {error}".format(error=e))     # get 2 part of error message [RuntimeError: threads can only be started once]
print("\n")

# Rename Thread
current.setName("SuperMainThread")
print(current.name)
print(current.getName())

# Print all alive and run threads
print(threading.enumerate())
print("\n")

# Thread safe storage
# If we change value in one thread, it doesn't change for another
thread_data = threading.local()
thread_data.value = 5

# print value from storage
def print_results():
    print(threading.current_thread())
    print("Result: {}".format(thread_data.value))

#
def change(started, to_value):
    print(hasattr(thread_data, 'value'))    # print attr
    thread_data.value = started     # assignment new value to storage cell
    for i in range(to_value):
        thread_data.value += 1      # increments to to_value every time
    print_results()

task1_thread = threading.Thread(target=change, args=(0, 10), name="TASK1")
task2_thread = threading.Thread(target=change, args=(100, 3), name="TASK2")

task1_thread.start()
task2_thread.start()

print_results()     # in last iteration it'll be 5 'cause of thread safe

task1_thread.join()
task2_thread.join()