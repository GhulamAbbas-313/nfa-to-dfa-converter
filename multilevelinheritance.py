class car:
    def __init__(self,type):
         self.type=type
    color="blue"
    @staticmethod
    def start():
        print("Start")
    @staticmethod
    def stop():
        print("Stop")
# class Toyotacar(car):
#         def __init__(self,brand):
#             self.brand=brand
class fortuner(car):
     def __init__(self,type):
        super().__init__(type)
        super().stop()
          
car1=fortuner("BMW")
print(car1.type)
car1.start()
print(car1.color)