def fcfs(): 

processes = [] 

ct = [] 

wt = [] 

tat = [] 

 

    num_processes = int(input("Enter the no of processes: ")) 

    for i in range(num_processes): 

process_id = input("Enter the Process id: ") 
````````````````````````````````````````````````````````````
at = int(input(f"Enter the arrival time {process_id}: ")) 

        bt = int(input(f"Enter the burst time {process_id}: ")) 

        processes.append({'Process id': process_id, "Arrival time": at, "Burst time": bt}) 

     

    processes.sort(key=lambda x: x['Arrival time'])  # Sort by Arrival Time 

     

    current_time = 0 

    for i, process in enumerate(processes):     

        if current_time < process['Arrival time']: 

            current_time = process['Arrival time'] 

        current_time += process['Burst time'] 

        ct.append(current_time) 

        tat.append(ct[i] - processes[i]['Arrival time']) 

        wt.append(tat[i] - processes[i]['Burst time']) 

        process['Completion time'] = ct[i] 

        process['Waiting time'] = wt[i] 

        process['Turn around time'] = tat[i] 

 

    avewt = sum(wt) / len(wt) 

    avetat = sum(tat) / len(tat) 

 

    print(f"\nThe average waiting time: {avewt:.2f}") 

    print(f"The average turn around time: {avetat:.2f}") 

    print(tabulate(processes, headers="keys", tablefmt="grid")) 

 

    # Gantt Chart 

    print("\nGantt Chart:") 

    for process in processes: 

        print(f"| {process['Process id']} ", end="") 

    print("|") 

    for time in ct: 

        print(f"{time:>5}", end=" ") 

    print() 

 

# Shortest Job First (SJF) 

def sjf(): 

    processes = [] 

    ct = [] 

    wt = [] 

    tat = [] 

 

    num_processes = int(input("Enter the no of processes: ")) 

    for i in range(num_processes): 

        process_id = input("Enter the Process id: ") 

        at = int(input(f"Enter the arrival time {process_id}: ")) 

        bt = int(input(f"Enter the burst time {process_id}: ")) 

        processes.append({'Process id': process_id, "Arrival time": at, "Burst time": bt}) 

     

    processes.sort(key=lambda x: (x['Burst time'], x['Arrival time']))  # Sort by Burst Time and then Arrival Time 

     

    current_time = 0 

    for i, process in enumerate(processes):     

        if current_time < process['Arrival time']: 

            current_time = process['Arrival time'] 

        current_time += process['Burst time'] 

        ct.append(current_time) 

        tat.append(ct[i] - processes[i]['Arrival time']) 

        wt.append(tat[i] - processes[i]['Burst time']) 

        process['Completion time'] = ct[i] 

        process['Waiting time'] = wt[i] 

        process['Turn around time'] = tat[i] 

 

    avewt = sum(wt) / len(wt) 

    avetat = sum(tat) / len(tat) 

 

    print(f"\nThe average waiting time: {avewt:.2f}") 

    print(f"The average turn around time: {avetat:.2f}") 

    print(tabulate(processes, headers="keys", tablefmt="grid")) 

 

    # Gantt Chart 

    print("\nGantt Chart:") 

    for process in processes: 

        print(f"| {process['Process id']} ", end="") 

    print("|") 

    for time in ct: 

        print(f"{time:>5}", end=" ") 

    print() 

 

# Priority Scheduling 

def priority_scheduling(): 

    processes = [] 

    ct = [] 

    wt = [] 

    tat = [] 

 

    num_processes = int(input("Enter the no of processes: ")) 

    for i in range(num_processes): 

        process_id = input("Enter the Process id: ") 

        at = int(input(f"Enter the arrival time {process_id}: ")) 

        bt = int(input(f"Enter the burst time {process_id}: ")) 

        priority = int(input(f"Enter the priority for {process_id}: ")) 

        processes.append({'Process id': process_id, "Arrival time": at, "Burst time": bt, "Priority": priority}) 

     

    processes.sort(key=lambda x: (x['Priority'], x['Arrival time']))  # Sort by Priority and then Arrival Time 

     

    current_time = 0 

    for i, process in enumerate(processes):     

        if current_time < process['Arrival time']: 

            current_time = process['Arrival time'] 

        current_time += process['Burst time'] 

        ct.append(current_time) 

        tat.append(ct[i] - processes[i]['Arrival time']) 

        wt.append(tat[i] - processes[i]['Burst time']) 

        process['Completion time'] = ct[i] 

        process['Waiting time'] = wt[i] 

        process['Turn around time'] = tat[i] 

 

    avewt = sum(wt) / len(wt) 

    avetat = sum(tat) / len(tat) 

 

    print(f"\nThe average waiting time: {avewt:.2f}") 

    print(f"The average turn around time: {avetat:.2f}") 

    print(tabulate(processes, headers="keys", tablefmt="grid")) 

 

    # Gantt Chart 

    print("\nGantt Chart:") 

    for process in processes: 

        print(f"| {process['Process id']} ", end="") 

    print("|") 

    for time in ct: 

        print(f"{time:>5}", end=" ") 

    print() 

 

# Main Program 

def main(): 

    while True: 

        print("\nWhich Algorithm do you want to run?") 

        print("1. FCFS") 

        print("2. SJF") 

        print("3. Priority Scheduling") 

        print("4. Exit") 

         

        choice = int(input("Enter your choice: ")) 

         

        if choice == 1: 

            fcfs() 

        elif choice == 2: 

            sjf() 

        elif choice == 3: 

            priority_scheduling() 

        elif choice == 4: 

            print("Exiting the program.") 

            break 

        else: 

            print("Invalid choice! Please try again.") 

         

        rerun = input("\nDo you want to run another algorithm? (Y/N): ").strip().upper() 

        if rerun != 'Y': 

            print("Exiting the program.") 

            break 

 

if __name__ == "__main__": 

    main() 

 

     

 

 

            