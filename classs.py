class student:
   # name="abbas"
    college='abc college'
    #constructor
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("creatin new stuent in datbase")
        #method
    def welcome(self):
        print(f"welcome student {self.name}")
    def get_marks(self):
        return self.marks
        
#object
s1=student("karan",96)
print(s1.name,s1.marks,s1.college)
s1.welcome()
print(s1.get_marks())
s2=student("abbas",88)
print(s2.name,s2.marks,s2.college)
s2.welcome()


# print(s1.name)
# s2=student()
# print(s2.name)
# class car:
#     color="blue"
#     brand="mercedes"
# car1=car()
# print(car1.color)
# print(car1.brand)
# k


