import time, os, signal

print("child process start, PID: ", os.getpid())

time.sleep(3)
# raise Exception("test")

print("child process end, PID: ", os.getpid())