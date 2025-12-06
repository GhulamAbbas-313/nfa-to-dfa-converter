from tabulate import tabulate


processes=[]
for i in range(int(input("Enter the number of process: "))):
   
   pid=input("Enter the process id: ")
   at=int(input(f"Enter the numbers in arrival time for {pid}: "))
   bt=int(input(f"Enter the numbers in burst time for {pid}: "))
ct=0
for i,in processes
if ct<

   
   processes.append({'Process ID':pid,'Arrival time': at,'Burst time':bt})   

processes.sort(key=lambda x: x['Arrival time'])


print(tabulate(processes, headers="keys", tablefmt="grid"))
