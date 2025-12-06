from tabulate import tabulate
from datetime import datetime
class city:
    def __init__(self,city_name):
        self.city_name=city_name
    
    def transaction(self):   
        table =[
            ["City_ID","City Name","transaction_date","Quantity","Price"],
            [1," karachi "]
        ]
        print(tabulate(table, headers="firstrow",tablefmt="psql"))

class product:
    def __init__(self,product_ID,product_name, price):
        self.product_ID=product_ID
        self.product_name=product_name
        self.price=price

def main():
    print("Select City \n 1.Lahore \n 2.Karachi \n 3.Lahore")
    try:
        user=int(input("Enter the Number (1-3): "))
        if user == 1:
            print("Lahore")
        elif user==2:
            print("Karachi")
        elif user==3:
            print("Peshawar")
            city.cityy()
            
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a number.")
if __name__ == "__main__":
    main()