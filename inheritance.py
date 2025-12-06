class car:
    color="blue"
    @staticmethod
    def start():
        print("Start")
    @staticmethod
    def stop():
        print("Stop")
class Toyotacar(car):
        def __init__(self,name):
            self.name=name
car1=Toyotacar("BMW")
print(car1.name)
car1.start()
print(car1.color)