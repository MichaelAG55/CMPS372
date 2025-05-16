class Transaction:
    def __init__(self, inventory):
        self.inventory = inventory
        self.cart=[]
        self.total=0

    def select_items(self):
        while True:
            print("\nAvailable Inventory: ")
            for item in self.inventory:
                print(f"- {item['name']} (${item['price']})")
            item_name = input("Enter the name of the item: ").strip()
            found = False
            for item in self.inventory:
                if item['name'].lower() == item_name.lower():
                    self.cart.append(item)
                    found = True
                    break
            if not found:
                print("Item Not Found.")
                continue
            more = input("Would you like to add more items? (yes/no)").strip().lower()
            if more != 'yes': 
                break
    def calculate_total(self):
        self.total = sum(item["price"] for item in self.cart)
        return self.total

    def clear_cart(self):
        self.cart.clear()
        self.total = 0


class Purchase(Transaction):
    def process(self, reports):
        self.select_items()
        total_price = self.calculate_total()
        print(f"\nTotal Purchase Amount: ${total_price:.2f}")
        reports.append(total_price)
        print("Thank you for shopping with us!")
        self.clear_cart()


class Return(Transaction):
    def process(self, reports):
        self.select_items()
        total_price = self.calculate_total()
        print(f"\nTotal Refund Amount: ${total_price:.2f}")
        print("Your return is completed.")
        self.clear_cart()


def manage_inventory(inventory):
    while True:
        print("\nInventory Management")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: "))
                inventory.append({"name": name, "price": price})
                print(f"{name} added.")
            except ValueError:
                print("Invalid price.")
        elif choice == '2':
            name = input("Enter item name to remove: ").strip()
            found = False
            for item in inventory:
                if item["name"].lower() == name.lower():
                    inventory.remove(item)
                    print(f"{name} removed.")
                    found = True
                    break
            if not found:
                print("Item not found.")
        elif choice == '3':
            break
        else:
            print("Invalid option.")


def view_reports(reports):
    print("\n=== Reports ===")
    print(f"Number of Customers: {len(reports)}")
    print(f"Total Profit: ${sum(reports):.2f}")
    input("Press any key to return to the main menu...")


def main():
    inventory = [
        {"name": "Apple", "price": 1.00},
        {"name": "Banana", "price": 0.50},
        {"name": "Milk", "price": 3.00}
    ]
    reports = []

    while True:
        print("\n=== Welcome to Python POS System ===")
        print("1. Make a Purchase")
        print("2. Make a Return")
        print("3. Manage Inventory")
        print("4. View Reports")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            purchase = Purchase(inventory)
            purchase.process(reports)
        elif choice == '2':
            return_process = Return(inventory)
            return_process.process(reports)
        elif choice == '3':
            manage_inventory(inventory)
        elif choice == '4':
            view_reports(reports)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
        

