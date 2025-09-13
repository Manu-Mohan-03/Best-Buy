from idlelib.zoomheight import set_window_geometry


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
        """To retrieve available quantity"""
        return self.quantity

    def set_quantity(self, quantity):
        """To set new quantity and to set inactive if stock goes below zero """
        available_quantity = self.get_quantity()
        self.quantity  = available_quantity + quantity
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()


    def is_active(self):
        """To check if a product is active"""
        return self.active

    def activate(self):
        """To set a product active"""
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, "
              f"Quantity: {self.quantity}")

    def buy(self, required_quantity):
        """
        Buys a given quantity of the product
        Updates the quantity of the product.
        Returns the total price (float) of the purchase.
        """
        if not self.is_active():
            raise Exception("Product out of stock!!!")
        elif required_quantity < 0:
            raise Exception("Positive value expected for quantity")
        else:
            available_stock = self.get_quantity()
            if required_quantity > available_stock:
                raise Exception(f"Insufficient Stock for {self.name}!!!")
            current_stock = available_stock - required_quantity
            self.set_quantity(current_stock)

        total_price = required_quantity * self.price
        return total_price