# class student:
    
#     def __init__(self,name,maths,science,ai,sum,average):
#         self.name=name
#         self.maths=maths
#         self.science=science
#         self.ai=ai
#         sum=ai+maths+science
#         average=sum/3
#     def cal_average(self):
#         print(f"The average of given subject is {average}")
# s1=student("Abbas",99,87,79)
#new
class student:
    @staticmethod
    def helo():
        print("hello")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def cal_average(self):
        sum=0
        for value in self.marks:
            sum+=value
        print(f"Hi {self.name},your average score is: {sum/3}")
s1=student("Abbas",[99,87,79])
# s1.cal_average()
#can change name directly
s1.name="Ali"
s1.cal_average()
s1.helo()