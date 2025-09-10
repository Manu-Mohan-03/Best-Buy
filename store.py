from products import Product

class Store:
    def __init__(self,product_list):
        if type(product_list) == list:
            self.product_list = product_list
        else:
            raise TypeError("Store needs a list of products")

    def add_product(self, product):
        if type(product) != Product:
            raise TypeError("Product is not yet created")
        if self.product_list.count(product) == 0:
            self.product_list.append(product)


    def remove_product(self, product):
        if self.product_list.count(product) > 0:
            self.product_list.remove(product)

    def get_total_quantity(self):
        total_quantity = 0.
        for product in self.product_list:
            if type(product) == Product:
                total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        store_list = []
        for product in self.product_list:
            if type(product) == Product:
                if product.is_active():
                    store_list.append(product)
        return store_list

    def order(self, shopping_list):
        total_price = 0
        for product,quantity in shopping_list:
            price = product.buy(quantity)
            total_price += price
        return total_price



