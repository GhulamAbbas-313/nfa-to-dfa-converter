import os 
arr=[5,4,3,1,2]

def buuble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
          if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    print("after swapping ",arr)

arr=list(map(int , input("enter the number by sapce ").split()))
pid = os.fork()

if pid ==0:
   print("i am child process ")
   buuble_sort(arr)

else :
   print("i am parent {pid}") 
   print("child will execute first because of os.wait()")
   os.wait()
   print("now i am going home after child execution")