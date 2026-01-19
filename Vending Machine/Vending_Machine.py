import csv,os
from product import Product
from prettytable import PrettyTable

class VendingMachine:
    def __init__(self):
        self.inventory = [Product(1,"Coke",10.0, 15),
                          Product(2,  "Pepsi",11.5, 13),
                          Product(3,  "BigApple",9.0, 10),
                          Product(4,  "BigLeeche",    9.5, 10),
                          Product(5,  "Shezan",5.0, 11),
                          Product(6,  "Sprite",9.0, 12),
                          Product(7,  "Fanta",9.0, 12),
                          Product(8,  "MountainDew", 11.0, 10),
                          Product(9, "7Up", 9.0, 14),
                          Product(10, "RedBull", 18.0, 8),
                          Product(11, "Sting",12.0,9),
                          Product(12, "Pakola",8.0, 13)]
        self.total_revenue = 50.0
        self.total_sold = 0
        self.product_count = 12

    def display_inventory(self):
        table = PrettyTable()
        table.field_names = ["Id", "Name", "Price", "Stock","Unit Sold"]
        for product in  self.inventory:
            table.add_row([product.id, product.name, product.price, product.stock, product.unit_sold])
        print(table)

    def buy_product(self):
        id = int(input("Enter the id of the product you want to buy : "))
        selected_product = None
        for product in self.inventory:
            if product.id == id:
                selected_product = product
                if selected_product.is_available() :
                    money = float(input(f"Enter money for {selected_product.name} of {selected_product.price} : "))
                    if money < selected_product.price:
                        print("Not enough money")
                    else:
                        print("Transaction Successful. Enjoy your Drink")
                        selected_product.reduce_stock()
                        self.total_revenue += selected_product.price
                        self.total_sold += 1
                        change = money - selected_product.price
                        print(f"Change : {change}")
                        self.log_transaction(selected_product.name,selected_product.price,money,change)
                        self.save_inventory()
                else:
                    print("Sorry that product is not available")
        if not selected_product :
            print("Invalid ID entered!!!")

    def load_inventory(self):
        try:
            with open("inventory.csv","r") as file:
                reader = csv.reader(file)
                self.inventory.clear()
                header = next(reader)
                for row in reader:
                    if not row:
                        continue
                    if row[0] == "Product Count":
                        self.product_count = int(row[1])
                        continue
                    if row[0] == "Total Revenue":
                        self.total_revenue = float(row[1])
                        continue
                    if row[0] == "Total Sold":
                        self.total_sold = int(row[1])
                        continue

                    pid = int(row[0])
                    name = str(row[1])
                    price = float(row[2])
                    stock = int(row[3])
                    unit_sold = int(row[4])
                    p = Product(pid,name,price,stock,unit_sold)
                    self.inventory.append(p)

        except FileNotFoundError:
            self.save_inventory()
    def save_inventory(self):
        with open("inventory.csv","w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID","Name","Price","Stock","Unit Sold"])
            for data in self.inventory:
                writer.writerow([data.id,data.name,data.price,data.stock,data.unit_sold])
            writer.writerow(["Product Count", self.product_count])
            writer.writerow(["Total Revenue",self.total_revenue])
            writer.writerow(["Total Sold",self.total_sold])

    def log_transaction(self,name, price, paid, change):
        file_exist = os.path.isfile("transaction.csv")
        with open("transaction.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exist:
                writer.writerow(["Name", "Total_Price", "Paid", "Change"])
            writer.writerow([str(name), float(price), float(paid), float(change)])