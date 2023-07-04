# Zesty Zomato CLI app

menu = [
    {
        "id": 1,
        "name": "Paneer Tikka",
        "price": 150,
        "availability": True
    },
    {
        "id": 2,
        "name": "Chicken Biryani",
        "price": 250,
        "availability": True
    },
    {
        "id": 3,
        "name": "Veg Pizza",
        "price": 200,
        "availability": False
    }
]

orders = []
order_id_counter = 1


def display_menu():
    print("Zesty Zomato Menu")
    print("-----------------")
    for dish in menu:
        availability = "Available" if dish["availability"] else "Not Available"
        print(f"{dish['id']}. {dish['name']} - ₹{dish['price']} ({availability})")
    print()


def add_dish():
    dish_id = len(menu) + 1
    dish_name = input("Enter the name of the dish: ")
    dish_price = float(input("Enter the price of the dish: "))
    availability = input("Is the dish available? (yes/no): ").lower() == "yes"
    
    dish = {
        "id": dish_id,
        "name": dish_name,
        "price": dish_price,
        "availability": availability
    }
    
    menu.append(dish)
    print(f"{dish_name} has been added to the menu.\n")


def remove_dish():
    dish_id = int(input("Enter the ID of the dish to remove: "))
    for dish in menu:
        if dish["id"] == dish_id:
            menu.remove(dish)
            print(f"Dish with ID {dish_id} has been removed from the menu.\n")
            break
    else:
        print(f"No dish found with ID {dish_id}.\n")


def update_dish_availability():
    dish_id = int(input("Enter the ID of the dish to update: "))
    availability = input("Is the dish available? (yes/no): ").lower() == "yes"
    
    for dish in menu:
        if dish["id"] == dish_id:
            dish["availability"] = availability
            print(f"Dish availability has been updated for ID {dish_id}.\n")
            break
    else:
        print(f"No dish found with ID {dish_id}.\n")


def take_order():
    global order_id_counter
    
    customer_name = input("Enter the customer's name: ")
    order_dish_ids = input("Enter the dish IDs (comma-separated): ").split(",")
    
    order_dishes = []
    for dish_id in order_dish_ids:
        dish_id = int(dish_id.strip())
        for dish in menu:
            if dish["id"] == dish_id and dish["availability"]:
                order_dishes.append(dish)
                break
        else:
            print(f"Dish with ID {dish_id} is not available. Order cannot be processed.\n")
            return
    
    order = {
        "id": order_id_counter,
        "customer_name": customer_name,
        "dishes": order_dishes,
        "status": "received"
    }
    
    orders.append(order)
    order_id_counter += 1
    
    print(f"Order with ID {order['id']} has been placed.\n")


def update_order_status():
    order_id = int(input("Enter the ID of the order to update: "))
    
    for order in orders:
        if order["id"] == order_id:
            print(f"Current status of order {order_id}: {order['status']}")
            new_status = input("Enter the new status: ")
            order["status"] = new_status
            print(f"Status of order {order_id} has been updated to {new_status}.\n")
            break
    else:
        print(f"No order found with ID {order_id}.\n")


def review_orders():
    if len(orders) == 0:
        print("No orders placed yet.\n")
    else:
        print("All Orders")
        print("----------")
        for order in orders:
            print(f"Order ID: {order['id']}")
            print(f"Customer Name: {order['customer_name']}")
            print("Dishes:")
            for dish in order["dishes"]:
                print(f"- {dish['name']}")
            print(f"Status: {order['status']}")
            print()
        print()


# Main program loop
while True:
    print("Welcome to Zesty Zomato!")
    print("------------------------")
    print("1. Display Menu")
    print("2. Add Dish")
    print("3. Remove Dish")
    print("4. Update Dish Availability")
    print("5. Take Order")
    print("6. Update Order Status")
    print("7. Review Orders")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")
    print()
    
    if choice == "1":
        display_menu()
    elif choice == "2":
        add_dish()
    elif choice == "3":
        remove_dish()
    elif choice == "4":
        update_dish_availability()
    elif choice == "5":
        take_order()
    elif choice == "6":
        update_order_status()
    elif choice == "7":
        review_orders()
    elif choice == "8":
        print("Thank you for using Zesty Zomato. Have a great day!")
        break
    else:
        print("Invalid choice. Please try again.\n")
