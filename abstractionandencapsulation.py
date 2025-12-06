class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print(f"your car has start now press brake {self.brk}")
#uper ka sarasat chupa diya unnecesary data chupa dena
car1=car()
car1.start()