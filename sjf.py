from tabulate import tabulate
ct,wt,tat=[],[],[]
processes=[]
num_process=int(input("Enter the no of processes"))
for i in range(num_process):
	pid=input("Enter the Process id: ")
	at=int(input("Enter the no of arrival time: "))
	bt=int(input("Enter the no of burst time: "))
	processes.append({'Process id':pid,'Arrival time':at,'Burst time':bt})
processes.sort(key=lambda x:x['Burst time'])
currentime=0
for i,process in enumerate(processes):
	if currentime < process['Arrival time']:
		currentime=process['Arrival time']
	currentime +=process['Burst time']
	ct.append(currentime)
	tat.append(ct[i]-processes[i]['Arrival time'])
	wt.append(tat[i]-processes[i]['Burst time'])
	process['Completion time']=ct[i]
	process['Waiting time']=wt[i]
	process['Turn Around time']=tat[i]
avewt=sum(wt)/len(wt)
print(f"The average waiting time:{avewt}")
avetat=sum(tat)/len(tat)
print(f"The turn around time:{avetat}")
print(tabulate(processes,headers="keys" ,tablefmt="grid"))