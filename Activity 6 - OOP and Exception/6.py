class Item:
    """Represents an item with an ID, name, description, and price."""
    
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    """Manages the CRUD operations for items."""
    
    def __init__(self):
        self.items = {}

    def create_item(self):
        """Creates a new item with user input and adds it to the list."""
        try:
            item_id = input("Enter Item ID: ").strip()
            if item_id in self.items:
                print("Error: Item ID already exists!")
                return
            
            name = input("Enter Item Name: ").strip()
            if not name:
                print("Error: Name cannot be empty!")
                return

            description = input("Enter Item Description: ").strip()

            price = float(input("Enter Item Price: ").strip())
            if price < 0:
                print("Error: Price cannot be negative!")
                return

            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")
        
        except ValueError:
            print("Error: Price must be a valid number!")

    def read_items(self):
        """Displays all stored items."""
        if not self.items:
            print("No items available.")
            return

        print("\n--- Item List ---")
        for item in self.items.values():
            print(item)
    
    def update_item(self):
        """Updates an existing item's details."""
        item_id = input("Enter Item ID to update: ").strip()
        if item_id not in self.items:
            print("Error: Item ID not found!")
            return
        
        name = input("Enter new name (leave blank to keep unchanged): ").strip()
        description = input("Enter new description (leave blank to keep unchanged): ").strip()
        
        try:
            price_input = input("Enter new price (leave blank to keep unchanged): ").strip()
            if price_input:
                price = float(price_input)
                if price < 0:
                    print("Error: Price cannot be negative!")
                    return
                self.items[item_id].price = price

            if name:
                self.items[item_id].name = name
            if description:
                self.items[item_id].description = description

            print("Item updated successfully!")

        except ValueError:
            print("Error: Price must be a valid number!")

    def delete_item(self):
        """Deletes an item by ID."""
        item_id = input("Enter Item ID to delete: ").strip()
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Error: Item ID not found!")

    def menu(self):
        """Displays the menu and handles user choices."""
        while True:
            print("\nItem Management System")
            print("[1] Create Item")
            print("[2] View Items")
            print("[3] Update Item")
            print("[4] Delete Item")
            print("[5] Exit")
            
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.create_item()
            elif choice == "2":
                self.read_items()
            elif choice == "3":
                self.update_item()
            elif choice == "4":
                self.delete_item()
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    manager = ItemManager()
    manager.menu()
