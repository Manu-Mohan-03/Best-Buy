class Product:
    def __init__(self, name, price, quantity):
        if name:
            self.name = name
        else:
            raise Exception("Product name cant be blank")
        if price < 0 or quantity < 0:
            raise Exception("Price/Quantity need positive values")
        else:
            self.price = price
            self.quantity = quantity
        if quantity > 0:
            self.active = True
        else:
            self.active = False

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        available_quantity = self.get_quantity()
        self.quantity  = available_quantity + quantity
        #self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: {self.price}, "
              f"Quantity: {self.quantity}")


    def buy(self, quantity):
        if not self.is_active():
            raise Exception("Product out of stock!!!")
        elif quantity < 0:
            raise Exception("Positive value expected for quantity")
        else:
            available_stock = self.get_quantity()
            self.quantity = available_stock - quantity
        total_price = quantity * self.price
        return total_price