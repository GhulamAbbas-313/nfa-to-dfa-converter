from tabulate import tabulate

# Product Database
table_data = [
    ["1", "Blood Collection Tubes", 15000, "50"],
    ["2", "CBC Analyzer", 10, "10000"],
    ["3", "Surgical Gloves", 500, "20"]
]

# Customer Class
class Customer:
    def __init__(self, name, cell_number):
        self.name = name
        self.cell_number = cell_number

    def display_customer_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer Cell: {self.cell_number}")

# Product Class
class Product:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

    def update_stock(self):
        for row in table_data:
            if row[0] == str(self.product_id):
                if int(row[2]) >= self.quantity:
                    row[2] = int(row[2]) - self.quantity
                    print("Stock updated successfully.")
                else:
                    print("Not enough stock available.")
                break

    def check_product_limit(self, city_id):
        if city_id == 1 and self.product_id == 2 and self.quantity > 5:
            print("We don't have enough CBC Analyzer, but we will arrange it for you from our head office.")
        elif city_id == 3 and self.product_id == 2 and self.quantity > 7:
            print("We don't have enough CBC Analyzer, but we will arrange it for you from our head office.")
        elif city_id == 3 and self.product_id == 1 and self.quantity > 15000:
            print("We don't have enough Blood Collection Tubes, but we will arrange it for you from our head office.")
        else:
            print("Your order has been placed.")

    def display_product_info(self):
        product_name = next((row[1] for row in table_data if row[0] == str(self.product_id)), "Unknown")
        print(f"Product: {product_name} (Quantity: {self.quantity})")

# City Class
class City:
    def __init__(self, city_id, postal_code):
        self.city_id = city_id
        self.postal_code = postal_code

    def display_city_info(self):
        print(f"City ID: {self.city_id} (Postal Code: {self.postal_code})")

    def get_city_id(self):
        return self.city_id

# Main Function
def main():
    print("Welcome to the MedPro Ordering System!\n")

    # Display product table
    print("Available Products:")
    print(tabulate(table_data, headers=["Product ID", "Product Name", "Stock", "Price"], tablefmt="grid"))

    # Get Customer Information
    customer_name = input("\nEnter your name: ")
    customer_cell = input("Enter your cell number: ")
    customer = Customer(customer_name, customer_cell)

    # Get City Information
    city_id = 0
    for _ in range(3):
        try:
            city_id = int(input("\nFrom which city are you ordering? (1: Lahore, 2: Karachi, 3: Islamabad): "))
            if city_id in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
    else:
        print("You have exceeded the number of attempts. Exiting the system.")
        return

    postal_code = input("Enter city postal code: ")
    city = City(city_id, postal_code)

    # Get Product Information
    product_id = 0
    for _ in range(3):
        try:
            product_id = int(input("\nWhich product do you want to order? (1: Blood Collection Tubes, 2: CBC Analyzer, 3: Surgical Gloves): "))
            if product_id in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
    else:
        print("You have exceeded the number of attempts. Exiting the system.")
        return

    quantity = int(input("Enter quantity: "))
    product = Product(product_id, quantity)

    # Check product limits
    product.check_product_limit(city.get_city_id())

    # Update Stock
    product.update_stock()

    # Display Order Details
    print("\nOrder Details:")
    customer.display_customer_info()
    city.display_city_info()
    product.display_product_info()

    print("\nUpdated Product Table:")
    print(tabulate(table_data, headers=["Product ID", "Product Name", "Stock", "Price"], tablefmt="grid"))

    print("\nThank you for using our system. Goodbye!")

if __name__ == "__main__":
    main()
