import threading 


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

def main ():
   print("1.User Management\n2.Service Managemet\n3.Process Management\n4.Backup ")
   choice=int(input("Enter your choice [1-4]: "))
   if choice==1:
    print("1.User Creation\n2.User Deletion\n3.User Update\n4.User List")
   elif choice==2:
	   print("1.Create folders and files \n2.Change File Rights \n3.File Search")
   elif choice==3:
      print("1. \n2.Sort Array through Threading \n3.Solve Matrix Using Threads")
   elif choice==4:
      print("1.Backup Database \n2.Backup File \n3.Backup System")