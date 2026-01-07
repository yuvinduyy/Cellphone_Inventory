from enum import Enum
from datetime import date
import json

class Condition(Enum):
    NEW = "New"
    REFURBISHED = "Refurbished"
    USED = "Used"

class CellPhone:
    def __init__(self, brand, model, imei, serial_number, import_date,
                 supplier, purchase_price, retail_price, stock_quantity,
                 condition, specifications, warranty_months,
                 features, marketing_tags, notes=""):
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
            f"Brand: {self.brand}
"
            f"Model: {self.model}
"
            f"IMEI: {self.imei}
"
            f"Serial No: {self.serial_number}
"
            f"Import Date: {self.import_date}
"
            f"Supplier: {self.supplier}
"
            f"Purchase Price: {self.purchase_price}
"
            f"Retail Price: {self.retail_price}
"
            f"Quantity: {self.stock_quantity}
"
            f"Condition: {self.condition.value}
"
            f"Specifications: {self.specifications}
"
            f"Warranty (months): {self.warranty_months}
"
            f"Features: {', '.join(self.features)}
"
            f"Marketing Tags: {', '.join(self.marketing_tags)}
"
            f"Notes: {self.notes}
"
        ): {self.warranty_months}
"
            f"Features: {', '.join(self.features)}
"
            f"Marketing Tags: {', '.join(self.marketing_tags)}
"
            f"Notes: {self.notes}
"
        )

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_phone(self, phone):
        if phone.imei in self.inventory:
            print("Phone with this IMEI already exists.")
        else:
            self.inventory[phone.imei] = phone
            print("Phone added successfully.")

    def remove_phone(self, imei):
        if imei in self.inventory:
            del self.inventory[imei]
            print("Phone removed successfully.")
        else:
            print("IMEI not found.")

    def search_by_imei(self, imei):
        return self.inventory.get(imei)

    def list_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        for phone in self.inventory.values():
            print(phone)
            print("-" * 40)


def input_phone_details():
    print("Enter phone details step by step")
    brand = input("Brand: ")
    model = input("Model: ")
    imei = input("IMEI: ")
    serial_number = input("Serial Number: ")
    supplier = input("Supplier: ")
    purchase_price = float(input("Purchase Price: "))
    retail_price = float(input("Retail Price: "))
    stock_quantity = int(input("Stock Quantity: "))

    print("Condition (1-New, 2-Refurbished, 3-Used)")
    condition_choice = input("Choose condition: ")
    condition = Condition.NEW if condition_choice == "1" else \
                Condition.REFURBISHED if condition_choice == "2" else Condition.USED

    specifications = {
        "CPU": input("CPU: "),
        "RAM_GB": input("RAM (GB): "),
        "Storage_GB": input("Storage (GB): "),
        "OS": input("Operating System: "),
        "Battery_mAh": input("Battery (mAh): "),
        "Camera_MP": input("Camera (MP): ")
    }

    warranty_months = int(input("Warranty Months: "))
    features = input("Features (comma separated): ").split(",")
    marketing_tags = input("Marketing Tags (comma separated): ").split(",")
    notes = input("Additional Notes: ")

    return CellPhone(
        brand, model, imei, serial_number, date.today(), supplier,
        purchase_price, retail_price, stock_quantity, condition,
        specifications, warranty_months, features, marketing_tags, notes
    )


def main_menu():
    manager = InventoryManager()

    while True:
        print("
--- Cell Phone Inventory Management ---")
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
            print(phone if phone else "Phone not found.")
        elif choice == "4":
            manager.list_inventory()
        elif choice == "5":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
```python
from enum import Enum
from datetime import date
import json

class Condition(Enum):
    NEW = "New"
    REFURBISHED = "Refurbished"
    USED = "Used"

class CellPhone:
    def __init__(self, brand, model, imei, serial_number, import_date,
                 supplier, purchase_price, retail_price, stock_quantity,
                 condition, specifications, warranty_months,
                 features, marketing_tags, notes=""):
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