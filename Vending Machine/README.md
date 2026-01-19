# Vending Machine System (Python OOP Project)

A fully functional **Vending Machine System** built using **Object-Oriented Programming in Python**, featuring persistent inventory management, admin controls, and transaction logging.

This project simulates a real-world vending machine where users can buy drinks and an admin can manage inventory, prices, and stock with data saved using CSV files.

---

## Features

### User Features

* View available drinks
* Buy a drink using cash input
* Automatic change calculation
* Stock reduction after purchase
* Transaction logging

### Admin Features

* Secure admin login
* Change product prices
* Restock products
* Add new products
* View machine statistics

  * Total revenue
  * Total drinks sold
  * Most popular drink

### Data Persistence

* Inventory saved in `inventory.csv`
* Transactions saved in `transaction.csv`
* Data is preserved even after program restarts

---

##  Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* CSV File Handling
* PrettyTable (for table display)

---

## 📂 Project Structure

```
Vending_Machine_Project/
│
├── main.py
├── Vending_Machine.py
├── Admin.py
├── product.py
├── inventory.csv
├── transaction.csv
└── README.md
```

---



## 🔑 Admin Login

Default Admin Password:

```
shazal123
```

*(You can change it inside `Admin.py`)*

---

## 📸 Sample Output

```
---Vending Machine---
Welcome to the Vending Machine!

Id | Name | Price | Stock | Unit Sold
-------------------------------------
1  | Coke | 10.0  | 15    | 0
2  | Pepsi| 11.5  | 13    | 0
...
```

---

## 🧠 OOP Concepts Used

* Inheritance
* Encapsulation
* Polymorphism
* Abstraction
* File Handling

---

## 🎯 Learning Outcomes

* Real-world OOP design
* CSV-based persistence
* Polymorphic object usage
* Debugging design-level bugs
* Clean software architecture

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it motivates me to build more projects!

---

**Made with ❤️ and Python**
