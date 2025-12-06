def inputt():
   return  int(input("Choose Question Number given above "))
 
   
# for lab 7 it is function
def UserManagement():
    UM=" Welcome To the Lobby of lab 7. \n1. Modify Example 1 to display strings via two independent threads:   thread1: 'Hello ! StudentName___',  thread 2: 'Student roll no is :__________'. \n2. Create threads message as many times as user wants to create threads by using array of threads and loop.Threads should display message that is passed through argument. "
    print("User Management")
    print(UM)
 
#for lab 8 it is fucntion 
def ServiceManagement():
   SM=" 1. Write a Python program to implement and simulate the FCFS Algorithm."
   print("Service Management")
   print(SM)
 
#for lab 9 it is function
def ProcessManagement():
    PM="1. Write a Python program to implement and simulate the Priority Algorithm.  \n2. Write a Python program to implement and simulate the Round Robin Algorithm.  \n3. Modify both algorithms for the different arrival time.  "
    print("Process Management")
    print(PM)

def Backup():
    BU="1. Write a python program that demonstrates the synchronization of Readers and Writer Problem using semaphores. \n Write a python program that demonstrates the synchronization of Consumer producer Bounded Buffer Problem using semaphores. "  
    print("Backup")
    print(BU)
# PROGRAM START FROM HERE 
def main():
    print('1.User Management \n2. Service Management\n3. Process Management\n4. Backup')
    user=int(input("Enter the number (1-4) "))
 
#{ outer loop 
    if user==1:
        choicee=inputt()
        UserManagement()
        if choicee == 1:
            print("Answer for Lab 7 Question 1")
        elif choicee == 2:
            print("Answer for Lab 7 Question 2")
        else:
            print("Invalid option for Lab 7")
    elif user ==2:
        ServiceManagement()
        choicee=inputt()
        if choicee ==1:
            print("Answer for Lab 8 Question 1")
        elif choicee == 2:
            print("Answer for Lab 8 Question 2")
        else:
            print("Invalid option for Lab 8")
    elif user==3:
        ProcessManagement()
        choiceee=inputt()
        if choiceee ==1:
            print("Answer for Lab 9 Question 1")
        elif choiceee == 2:
            print("Answer for Lab 9 Question 2")
        elif choiceee==3:
            print("Answer for lab 10 Question 3")
        else:
            print("Invalid option for Lab 9")
    elif user==4:
        Backup()
        choiceeee=inputt()
        if choiceeee ==1:
            print("Answer for lab 10 Question 1")
        elif choiceeee == 2:
            print("Answer for Lab 9 Question 2")
        else:
            print("Invalid option for Lab 9")    
    else :
        print("Please select a valid lab from  ( 1 to 4)")
main()
