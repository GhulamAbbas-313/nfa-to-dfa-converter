import threading 
# arr=[5,4,3,1,2]
def buuble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
          if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            
arr=list(map(int , input("Enter the numbers more then one by space").split()))
print("before swapping",arr)


t1=threading.Thread(target=buuble_sort, args=(arr,))

t1.start()
t1.join()
print("after swapping ",arr)

