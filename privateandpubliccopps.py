class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def get_pass(self):
        return self.__acc_pass
    def __hello(self):
        print("hellow world")
    def welcome(self):
        self.__hello()
s1=account(123434,"abc23")
print(s1.acc_no)
print(s1.get_pass())
# print(s1.welcome())
s1.welcome()