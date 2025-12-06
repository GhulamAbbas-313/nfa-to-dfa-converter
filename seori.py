from tabulate import tabulate
from datetime import datetime

# Product class to manage stock and order limits
class Product:
    def __init__(self, name, max_order_limit, current_stock, price):
        self.name = name
        self.max_order_limit = max_order_limit
        self.current_stock = current_stock
        self.price = price

    def deduct_stock(self, quantity):
        if self.current_stock >= quantity:
            self.current_stock -= quantity
            return True
        else:
            return False

  

# Lab class to store lab information
class Lab:
    def __init__(self, city, name, phone, postal_code):
        self.city = city
        self.name = name
        self.phone = phone
        self.postal_code = postal_code

# Transaction class to store transaction details
class Transaction:
    def __init__(self, product_name, quantity, total_price, date):
        self.product_name = product_name
        self.quantity = quantity
        self.total_price = total_price
        self.date = date

# Create products
cbc_analyzer = Product("CBC Analyzer", 5, 5, 100000)
blood_tubes = Product("Blood Tubes", 12000, 12000, 20)
surgical_gloves = Product("Surgical Gloves", 20, 20, 500)

products = [cbc_analyzer, blood_tubes, surgical_gloves]
transaction_history = []  # List to store transactions

# Display function to show products table
def display_products():
    headers = ["Product", "Max Order", "Stock", "Price/Unit"]
    table = [[product.name, product.max_order_limit, product.current_stock, product.price] for product in products]
    return tabulate(table, headers, tablefmt="grid")

# Display function to show transaction history
def display_transaction_history():
    if not transaction_history:
        return "No transactions made yet."
    headers = ["Product", "Quantity", "Total Price", "Date"]
    table = [[transaction.product_name, transaction.quantity, transaction.total_price, transaction.date] for transaction in transaction_history]
    return tabulate(table, headers, tablefmt="grid")

# Main program flow
def main():
    while True:
        # Step 1: User enters lab details
        print("Enter Lab Information:")
        city = input("Select city \n 1. Lahore \n 2. Karachi \n 3. Peshawar: \n Select Number Provided above(1-3)  ")
        if city == '1':
            city_name = "Lahore"
        elif city == '2':
            city_name = "Karachi"
        elif city == '3':
            city_name = "Peshawar"
        else:
            print("Invalid city! Would you like to try again? (y/n)")
            retry = input()
            if retry.lower() == 'n':
                break
            else:
                continue

        lab_name = input("Enter Lab Name: ")
        phone = input("Enter Lab Phone Number: ")
        postal_code = input("Enter Postal Code: ")

        lab = Lab(city_name, lab_name, phone, postal_code)

        print(f"\nLab Info: {lab.name}, Phone: {lab.phone}, Postal Code: {lab.postal_code}, City: {lab.city}\n")
        
        # Step 2: Show the product table
        print("Available Products:")
        print(display_products())

        # Step 3: Ask user which product they want
        while True:
            product_choice = input("Which product do you need? (1. CBC Analyzer, 2. Blood Tubes, 3. Surgical Gloves): ")
            if product_choice == '1':
                selected_product = cbc_analyzer
                break
            elif product_choice == '2':
                selected_product = blood_tubes
                break
            elif product_choice == '3':
                selected_product = surgical_gloves
                break
            else:
                print("Invalid choice! Would you like to try again? (y/n)")
                retry = input()
                if retry.lower() == 'n':
                    break
                else:
                    continue

        # Step 4: User enters quantity for the product
        while True:
            try:
                quantity = int(input(f"Enter quantity for {selected_product.name}: "))
                if quantity <= 0:
                    print("Quantity must be greater than zero. Try again.")
                    continue
                if quantity > selected_product.current_stock:
                    print(f"Error: You cannot order more than the available stock of {selected_product.name}. Available stock: {selected_product.current_stock}")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid number for quantity.")

        # If sufficient stock, deduct and log transaction
        if selected_product.deduct_stock(quantity):
            total_price = quantity * selected_product.price
            transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Create a transaction and add it to the transaction history
            transaction = Transaction(selected_product.name, quantity, total_price, transaction_date)
            transaction_history.append(transaction)

            print(f"{quantity} {selected_product.name} ordered. Remaining stock: {selected_product.current_stock}")
        else:
            print(f"Insufficient stock for {selected_product.name}.")

        # Step 5: Show updated product table after order
        print("\nUpdated Product Table:")
        print(display_products())

        # Step 6: Option to view transaction history
        view_history = input("\nWould you like to view the transaction history? (y/n): ")
        if view_history.lower() == 'y':
            print("\nTransaction History:")
            print(display_transaction_history())

        # Step 7: Ask user if they want to make another order or exit
        continue_order = input("\nDo you want to place another order? (y/n): ")
        if continue_order.lower() == 'n':
            break

# Correct condition to check if the script is executed directly
if __name__ == "__main__":
    main()
