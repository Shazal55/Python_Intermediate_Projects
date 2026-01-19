class Product:
    def __init__(self, id =0 ,name = "Unknown", price = 0 , stock = 0 , unit_sold = 0):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.unit_sold = unit_sold

    def is_available(self):
        if self.stock > 0:
            return True
        else:
            return False

    def reduce_stock(self):
        if self.stock > 0:
            self.stock -= 1
            self.add_sale()

    def add_sale(self):
        self.unit_sold += 1
