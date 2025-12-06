processes=[]
ct=[]
wt=[]
tat=[]
num_process=int(input("enter the no of process id: "))
for i in range (num_process):
	pid=input("enter process id")
	at=int(input("enter Arrival time"))
	bt=int(input("enter burst time"))
	processes.append({"process id":pid ,"Arrival time":at,"burst time":bt,})
	processes.sort(key=lambda X:X["Arrival time"])
	currenttime=0
	for i,  process in enumerate (processes):
		if currenttime < process['Arrival time']:
			currenttime= process['Arrival time']
			currenttime+= process['burst time']
			ct.append(currenttime)
			tat.append(ct[i]- processes[i]['Arrival time'])
			wt.append(ct[i]-processes[i]['burst time'])
			for i,process in enumerate(processes):
				process['completiontime']=ct[i]
				process['turn around time']=tat[i]
				process['waiting time']=wt[i]
print(f"completiotime:{ct},turn around time:{tat},waiting time:{wt}")
				
			

	

