from prettytable import PrettyTable
from Vending_Machine import VendingMachine
from product import Product


class Admin(VendingMachine):
    PASSWORD = "shazal123"
    MAX_PRODUCTS = 20
    is_login = False
    total_stock = 0

    def login(self):
        if not self.is_login:
            while True:
                passkey = input("Please enter your password for Vending Machine: ")
                if passkey == self.PASSWORD:
                    self.is_login = True
                    print("Login Successful!")
                    break
                else:
                    print("Wrong Password. Try again.")

        while True:
            self.show_options()
            cont = input("Do you want to continue again? (y/n) : ")
            if cont != 'y':
                print("Logging Out . . . ")
                break

    def show_options(self):
        self.display_inventory()
        choice = int(input("What do you want to do? : \n1.Change Product Price \n2.Restock Product \n3.Add product \n4.Show Details\n"))
        if choice == 1:
            self.change_price()
        elif choice == 2:
            self.restock()
        elif choice == 3:
            self.add_product()
        elif choice == 4:
            self.show_details()
        else:
            print("Wrong Choice. Try again.")



    def change_price(self):
        found = False
        change_id = int(input("Enter the product ID you want to change : "))
        for product in self.inventory:
            if product.id == change_id:
                found = True
                change_price = float(input("Enter the product price you want to change : "))
                product.price = change_price
                print("Successfully changed product price to: ", product.price)
                self.save_inventory()
                self.display_inventory()
                break
        if not found:
            print("Wrong ID. Try again.")
            self.change_price()

    def restock(self):
        found = False
        cid = int(input("Enter the product ID you want to restock : "))
        for product in self.inventory:
            if product.id == cid:
                found = True
                stock_number = int(input("Enter the stock amount you want to restock : "))
                cost = stock_number * product.price
                if cost < self.total_revenue:
                    product.stock += stock_number
                    self.total_revenue -= cost
                    print("Stock added Successfully.")
                    print("Remaining revenue : ",self.total_revenue)
                    self.display_inventory()
                    self.save_inventory()

                    break
                else:
                    print("Not enough revenue.")

                    break
        if not found:
            print("Invalid ID entered. Try again.")
            self.restock()

    def add_product(self):
        if self.product_count >= self.MAX_PRODUCTS:
            print("Inventory Full! Can't add more products.")
            return
        new_id = self.product_count + 1
        new_name = input("Enter the product name you want to add : ")
        new_price = float(input("Enter the product price you want to add : "))
        new_stock = int(input("Enter the stock amount you want to add : "))
        if new_price <=0 or new_stock<=0:
            print("Invalid price or stock. Try again.")
            self.add_product()
        cost = new_price * new_stock
        if cost > self.total_revenue:
            print("Not enough revenue. Try again.")
            self.add_product()
        self.inventory.append(Product(new_id, new_name, new_price, new_stock,0))
        print("Product Added Successfully.")
        self.total_revenue-= cost
        self.product_count += 1
        self.display_inventory()
        self.save_inventory()

    def show_details(self):
        table = PrettyTable()
        table.field_names = ["Details","Values"]
        table.add_row(["Total Revenue ",self.total_revenue])
        table.add_row(["Total Sold Drink",self.total_sold])
        table.add_row(["Most Popular drink",self.popular_drink()])
        print(table)


    def popular_drink(self):
        max_sold = self.inventory[0].unit_sold
        drink = self.inventory[0].name
        for product in self.inventory:
            if product.unit_sold > max_sold:
                max_sold = product.unit_sold
                drink = product.name
        return drink
