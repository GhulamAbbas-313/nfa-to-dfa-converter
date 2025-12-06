from tabulate import tabulate

def mainprocess():
    processes = []
    num_processes = int(input("Enter the number of processes: "))
    for i in range(num_processes):
        process_id = input("Enter the process id: ")
        arrival_time = int(input(f"Enter the arrival time for {process_id}: "))
        burst_time = int(input(f"Enter the burst time for {process_id}: "))
        processes.append({'Process id': process_id, 'Arrival time': arrival_time, 'Burst time': burst_time})
    return processes

def fcfs():
    processes = mainprocess()
    processes.sort(key=lambda x: x['Arrival time'])

    current_time = 0
    ct = []
    tat = []
    wt = []

    for i, process in enumerate(processes):
        if current_time < process['Arrival time']:
            current_time = process['Arrival time']
        current_time += process['Burst time']
        ct.append(current_time)

    for i, process in enumerate(processes):
        tat.append(ct[i] - processes[i]['Arrival time'])
    for i, process in enumerate(processes):
        wt.append(tat[i] - processes[i]['Burst time'])

    for i, process in enumerate(processes):
        process['Completion Time'] = ct[i]

    for i, process in enumerate(processes):
        process['Turn Around time '] = tat[i]
    for i, process in enumerate(processes):
        process['Waiting time '] = wt[i]

    s_wt = sum(wt) / len(wt)
    averagewt = s_wt / 100
    print("average waiting ", averagewt)

    print("Table form :")
    print(tabulate(processes, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    fcfs()
