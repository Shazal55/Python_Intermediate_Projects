from Admin import Admin
print("---Vending Machine---")
print("Welcome to the Vending Machine!")
vm = Admin()
vm.load_inventory()
admin = vm
vm.load_inventory()
again = 'y'
while again == 'y':
    input1 = input("Enter any key to continue or Enter 'a' for Admin Login : ")
    if input1 == "a":
        admin.login()
    else:
        vm.display_inventory()
        print("So What do you like to Drink?")
        vm.buy_product()
    again = input("Do you want to continue using Vending Machine? (y/n) : ")
    if again =='n':
        print("Thanks for using Vending Machine!")

