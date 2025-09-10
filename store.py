from products import Product

class Store:
    def __init__(self,product_list):
        if type(product_list) == list:
            self.product_list = product_list
        else:
            raise TypeError("Store needs a list of products")

    def add_product(self, product):
        """To add product to the store"""
        if type(product) != Product:
            raise TypeError("Only products can be added")
        if self.product_list.count(product) == 0:
            self.product_list.append(product)


    def remove_product(self, product):
        """To remove product from the store"""
        if self.product_list.count(product) > 0:
            self.product_list.remove(product)

    def get_total_quantity(self):
        """To return the total stock of all items in store"""
        total_quantity = 0
        for product in self.product_list:
            if type(product) == Product:
                total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """To return a list of all products availabe in store"""
        store_list = []
        for product in self.product_list:
            if type(product) == Product:
                if product.is_active():
                    store_list.append(product)
        return store_list

    def order(self, shopping_list):
        """To create a sales order"""
        total_price = 0
        for product,quantity in shopping_list:
            try:
                price = product.buy(quantity)
            except Exception as error:
                raise Exception(error)
            total_price += price
        return total_price



