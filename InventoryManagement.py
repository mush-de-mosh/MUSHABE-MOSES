# Initialize empty inventory dictionary
inventory = {}

def display_menu():
    """Display the main menu"""
    print("\nINVENTORY MANAGEMENT SYSTEM")
    print("1. Add new item")
    print("2. View all items")
    print("3. Update item quantity")
    print("4. Delete item")
    print("5. Exit")

def add_item():
    """Add a new item to inventory"""
    name = input("Enter item name: ")
    if name in inventory:
        print("Item already exists! Use update option instead.")
        return
    
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        inventory[name] = {"quantity": quantity, "price": price}
        print(f"{name} added to inventory!")
    except ValueError:
        print("Invalid input! Quantity must be whole number and price must be numeric.")

def view_items():
    """Display all items in inventory"""
    if not inventory:
        print("Inventory is empty!")
        return
    
    print("\nCURRENT INVENTORY:")
    print("{:<20} {:<10} {:<10}".format("Item", "Quantity", "Price"))
    print("-" * 40)
    for item, details in inventory.items():
        print("{:<20} {:<10} ${:<10.2f}".format(item, details["quantity"], details["price"]))

def update_item():
    """Update quantity of existing item"""
    name = input("Enter item name to update: ")
    if name not in inventory:
        print("Item not found!")
        return
    
    try:
        new_quantity = int(input(f"Enter new quantity for {name}: "))
        inventory[name]["quantity"] = new_quantity
        print(f"{name} quantity updated to {new_quantity}")
    except ValueError:
        print("Invalid input! Quantity must be a whole number.")

def delete_item():
    """Remove item from inventory"""
    name = input("Enter item name to delete: ")
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from inventory!")
    else:
        print("Item not found!")

# Main program loop
while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 1:
            add_item()
        elif choice == 2:
            view_items()
        elif choice == 3:
            update_item()
        elif choice == 4:
            delete_item()
        elif choice == 5:
            print("Exiting inventory system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")
    except ValueError:
        print("Invalid input! Please enter a number.")