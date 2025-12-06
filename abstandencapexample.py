class account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def debit(self,amount):
        self.balance-=amount
        print(f"Rs , {amount} was debited")
        print(f"total amount= {self.get_balance()}")
    def credit(self,amount):
        self.balance+=amount
        print(f"Rs, {amount} was credit")
        print(f"total amount= {self.get_balance()}")

    def get_balance(self):
        return self.balance
acc1=account(10000,1234)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(5000)

print(acc1.balance,acc1.account_no)