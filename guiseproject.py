from tabulate import tabulate

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

    def restock(self, quantity):
        self.current_stock += quantity

# Lab class to store lab information
class Lab:
    def __init__(self, city, name, phone, postal_code):
        self.city = city
        self.name = name
        self.phone = phone
        self.postal_code = postal_code

# Create products
cbc_analyzer = Product("CBC Analyzer", 5, 5, 100000)
blood_tubes = Product("Blood Tubes", 12000, 12000, 20)
surgical_gloves = Product("Surgical Gloves", 20, 20, 500)

products = [cbc_analyzer, blood_tubes, surgical_gloves]

# Display function to show products table
def display_products():
    headers = ["Product", "Max Order", "Stock", "Price/Unit"]
    table = [[product.name, product.max_order_limit, product.current_stock, product.price] for product in products]
    return tabulate(table, headers, tablefmt="grid")

# Main program flow
def main():
    # Step 1: User enters lab details
    print("Enter Lab Information:")
    city = input("Select city (1. Lahore, 2. Karachi, 3. Peshawar): ")
    if city == '1':
        city_name = "Lahore"
    elif city == '2':
        city_name = "Karachi"
    elif city == '3':
        city_name = "Peshawar"
    else:
        print("Invalid city!")
        return

    lab_name = input("Enter Lab Name: ")
    phone = input("Enter Lab Phone Number: ")
    postal_code = input("Enter Postal Code: ")

    lab = Lab(city_name, lab_name, phone, postal_code)

    print(f"\nLab Info: {lab.name}, Phone: {lab.phone}, Postal Code: {lab.postal_code}, City: {lab.city}\n")
    
    # Step 2: Show the product table
    print("Available Products:")
    print(display_products())

    # Step 3: Ask user which product they want
    product_choice = input("Which product do you need? (1. CBC Analyzer, 2. Blood Tubes, 3. Surgical Gloves): ")

    if product_choice == '1':
        selected_product = cbc_analyzer
    elif product_choice == '2':
        selected_product = blood_tubes
    elif product_choice == '3':
        selected_product = surgical_gloves
    else:
        print("Invalid choice!")
        return

    # Step 4: User enters quantity for the product
    quantity = int(input(f"Enter quantity for {selected_product.name}: "))
    if selected_product.deduct_stock(quantity):
        print(f"{quantity} {selected_product.name} ordered. Remaining stock: {selected_product.current_stock}")
    else:
        print(f"Insufficient stock for {selected_product.name}.")
    
    # Step 5: Show updated product table after order
    print("\nUpdated Product Table:")
    print(display_products())

if __name__ == "__main__":
    main()