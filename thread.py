import time
import threading

def task1():
   time.sleep(2)
   print("task1 completed")
def task2():
	time.sleep(2)
	print("task2 completed")

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()

t1.join()
t2.join()
print("All task completed")