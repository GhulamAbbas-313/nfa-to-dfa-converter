import time
import threading
import random
empty=threading.Semaphore(5)
full=threading.Semaphore(0)
mutex=threading.Lock()
buffer=[]
def producer():
		num=range(5)
		nums=random.choice(num)
		global buffer
		empty.acquire()
		mutex.acquire() ##for lock
		buffer.append(num)
		print(f"produced:{buffer}{nums}")
		mutex.release() ##for unlock
		full.release()
		time.sleep(2)
def consumer():
		global buffer
		full.acquire()
		mutex.acquire()
		item=buffer.pop(0)
		print(f"Consumed{item}{buffer}")
		mutex.release()
		empty.release()
		time.sleep(3)
p1=threading.Thread(target=producer)
p2=threading.Thread(target=consumer)
p1.start()
p2.start()
p1.join()
p2.join()
print("The semaphore is completed")

