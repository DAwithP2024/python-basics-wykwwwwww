# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_categories():
    for idx, category in enumerate(products.keys(), 1):
        print(f"{idx}. {category}")
    return input_category()

def display_products(products_list):
    for idx, (product, price) in enumerate(products_list, 1):
        print(f"{idx}. {product} - ${price}")

def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = sum(price * quantity for _, price, quantity in cart)
    for product_name, price, quantity in cart:
        print(f"{product_name} - ${price} x {quantity} = ${price * quantity}")
    print(f"Total cost: ${total_cost}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print("\n----- Receipt -----")
    print(f"Name: {name}\nEmail: {email}\n")
    print("Items Purchased:")
    for product_name, price, quantity in cart:
        print(f"{product_name} - ${price} x {quantity} = ${price * quantity}")
    print(f"\nTotal Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("\nYour items will be delivered in 3 days.")
    print("Payment will be accepted after successful delivery.")
    print("--------------------")

def validate_name(name):
    return len(name.split()) == 2 and all(part.isalpha() for part in name.split())

def validate_email(email):
    return "@" in email

def input_category():
    try:
        choice = int(input("Please select a category by entering the corresponding number: "))
        return choice - 1 if 1 <= choice <= len(products) else None
    except ValueError:
        return None

def main():
    # Input and validate name
    name = input("Please enter your full name (First and Last Name): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name with only alphabets and a first and last name.")
        name = input("Please enter your full name (First and Last Name): ")

    # Input and validate email
    email = input("Please enter your email address: ")
    while not validate_email(email):
        print("Invalid email address. Please include an '@' symbol in your email.")
        email = input("Please enter your email address: ")

    cart, total_cost = [], 0

    # Shopping process
    while True:
        print("\nAvailable Categories:")
        category_index = display_categories()
        if category_index is None:
            print("Invalid category selection. Please try again.")
            continue

        category_name = list(products.keys())[category_index]
        current_products = products[category_name]

        while True:
            print(f"\nProducts in {category_name}:")
            display_products(current_products)

            print("\nOptions:\n1. Select a product to buy\n2. Sort products by price\n3. Go back to categories\n4. Finish shopping")
            option = input("Please select an option: ")

            if option == "1":
                product_choice = input("Enter the product number you want to buy: ")
                try:
                    product_choice = int(product_choice) - 1
                    if 0 <= product_choice < len(current_products):
                        quantity = int(input("Enter the quantity you want to buy: "))
                        if quantity > 0:
                            selected_product = current_products[product_choice]
                            add_to_cart(cart, selected_product, quantity)
                            total_cost += selected_product[1] * quantity
                            print(f"{quantity} x {selected_product[0]} added to cart.")
                    else:
                        print("Invalid product selection.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")

            elif option == "2":
                sort_order = input("Sort by price ('asc' for ascending, 'desc' for descending): ")
                if sort_order in ["asc", "desc"]:
                    current_products = display_sorted_products(current_products, sort_order)
                else:
                    print("Invalid input. Please enter 'asc' or 'desc'.")

            elif option == "3":
                break  # Go back to category selection

            elif option == "4":
                if cart:
                    total_cost = display_cart(cart)
                    address = input("Please enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time.")
                return  # End shopping

            else:
                print("Invalid option. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()