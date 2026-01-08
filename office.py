from enum import Enum
from datetime import date


class Condition(Enum):
    NEW = "New"
    REFURBISHED = "Refurbished"
    USED = "Used"


class CellPhone:
    def __init__(
        self,
        brand,
        model,
        imei,
        serial_number,
        import_date,
        supplier,
        purchase_price,
        retail_price,
        stock_quantity,
        condition,
        specifications,
        warranty_months,
        features,
        marketing_tags,
        notes=""
    ):
        self.brand = brand
        self.model = model
        self.imei = imei
        self.serial_number = serial_number
        self.import_date = import_date
        self.supplier = supplier
        self.purchase_price = purchase_price
        self.retail_price = retail_price
        self.stock_quantity = stock_quantity
        self.condition = condition
        self.specifications = specifications
        self.warranty_months = warranty_months
        self.features = features
        self.marketing_tags = marketing_tags
        self.notes = notes

    def __str__(self):
        return (
            f"Brand: {self.brand}\n"
            f"Model: {self.model}\n"
            f"IMEI: {self.imei}\n"
            f"Serial Number: {self.serial_number}\n"
            f"Import Date: {self.import_date}\n"
            f"Supplier: {self.supplier}\n"
            f"Purchase Price: {self.purchase_price}\n"
            f"Retail Price: {self.retail_price}\n"
            f"Stock Quantity: {self.stock_quantity}\n"
            f"Condition: {self.condition.value}\n"
            f"Specifications: {self.specifications}\n"
            f"Warranty (Months): {self.warranty_months}\n"
            f"Features: {', '.join(self.features)}\n"
            f"Marketing Tags: {', '.join(self.marketing_tags)}\n"
            f"Notes: {self.notes}\n"
        )


class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_phone(self, phone):
        if phone.imei in self.inventory:
            print("❌ Phone with this IMEI already exists.")
        else:
            self.inventory[phone.imei] = phone
            print("✅ Phone added successfully.")

    def remove_phone(self, imei):
        if imei in self.inventory:
            del self.inventory[imei]
            print("✅ Phone removed successfully.")
        else:
            print("❌ IMEI not found.")

    def search_by_imei(self, imei):
        return self.inventory.get(imei)

    def list_inventory(self):
        if not self.inventory:
            print("📭 Inventory is empty.")
            return

        for phone in self.inventory.values():
            print(phone)
            print("-" * 40)


def input_phone_details():
    print("\nEnter phone details step by step\n")

    brand = input("Brand: ")
    model = input("Model: ")
    imei = input("IMEI: ")
    serial_number = input("Serial Number: ")
    supplier = input("Supplier: ")

    purchase_price = float(input("Purchase Price: "))
    retail_price = float(input("Retail Price: "))
    stock_quantity = int(input("Stock Quantity: "))

    print("\nCondition:")
    print("1 - New")
    print("2 - Refurbished")
    print("3 - Used")
    condition_choice = input("Choose condition: ")

    if condition_choice == "1":
        condition = Condition.NEW
    elif condition_choice == "2":
        condition = Condition.REFURBISHED
    else:
        condition = Condition.USED

    specifications = {
        "CPU": input("CPU: "),
        "RAM (GB)": input("RAM (GB): "),
        "Storage (GB)": input("Storage (GB): "),
        "Operating System": input("Operating System: "),
        "Battery (mAh)": input("Battery (mAh): "),
        "Camera (MP)": input("Camera (MP): ")
    }

    warranty_months = int(input("Warranty Months: "))

    features = input("Features (comma separated): ").split(",")
    marketing_tags = input("Marketing Tags (comma separated): ").split(",")
    notes = input("Additional Notes: ")

    return CellPhone(
        brand,
        model,
        imei,
        serial_number,
        date.today(),
        supplier,
        purchase_price,
        retail_price,
        stock_quantity,
        condition,
        specifications,
        warranty_months,
        features,
        marketing_tags,
        notes
    )


def main_menu():
    manager = InventoryManager()

    while True:
        print("\n--- Cell Phone Inventory Management System ---")
        print("1. Add phone")
        print("2. Remove phone")
        print("3. Search phone by IMEI")
        print("4. View inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            phone = input_phone_details()
            manager.add_phone(phone)

        elif choice == "2":
            imei = input("Enter IMEI to remove: ")
            manager.remove_phone(imei)

        elif choice == "3":
            imei = input("Enter IMEI to search: ")
            phone = manager.search_by_imei(imei)
            if phone:
                print(phone)
            else:
                print("❌ Phone not found.")

        elif choice == "4":
            manager.list_inventory()

        elif choice == "5":
            print("👋 Exiting system.")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()