# Project Name: School Management System

# In this, you can use:
# Encapsulation for student records (marks, personal data).

# Abstraction for different types of users (Admin, Teacher, Student), each with different responsibilities.
class student:
    def __init__(self,name,cgpa,dob,semester):
        self.name=name
        self.dob=dob
        self.cgpa=cgpa
        self.semester=semester
    def details(self,n):
        self.n=n
        print(f"This is student databse of School\n{self.n}.{self.name} ,Roll_No: {self.dob} of semester: {self.semester} \n With the cgpa {self.cgpa} ")
class faculty:
    def __init__(self,name,work,sal):
        self.name=name
        self.work=work
        self.sal=sal
    def details(self,n):
        self.n=n
        print(f"This is employee database of School\n{n+1}.{self.name} employee as a {self.work} haveing a salary of: {self.sal}")
emp1=faculty("noman","VC",50000)
emp2=faculty("Ali","Teacher",30000)
emp1.details(0)
emp2.details(1)        
s1=student("Abbas jafri",3.6,"23SP-039_CS",5)
s2=student("Muneeb Ahmed ",3.0,"23SP-040_CS",5)
s3=student("Saad shakir",3.2,"23SP-041_CS",5)
s4=student("Hussain jafri",3.8,"23SP-042_CS",5)
s1.details(0)
s2.details(1)
s3.details(2)
s4.details(3)

