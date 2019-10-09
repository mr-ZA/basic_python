import threading

print(threading.active_count())
current = threading.current_thread()
print(current.getName())                # in default - MainThread
print(current.is_alive())
print(current.isDaemon())

# Trying to restart Main thread
try:
    current.start()
except RuntimeError as e:
    print("ERROR: {error}".format(error=e))     # get 2 part of error message [RuntimeError: threads can only be started once]

# Rename Thread
current.setName("SuperMainThread")
print(current.name)
print(current.getName())

# Print all alive and run threads
print(threading.enumerate())

# Thread safe storage