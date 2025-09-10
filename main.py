from products import Product
from store import Store

QUIT = True

# setup initial stock of inventory
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
            ]

best_buy = Store(product_list)


def start(user_menu):
    """
    User Interface creation and calling the opted feature by the user
    :param user_menu: a dispatch function dictionary
    :return: True in case user choose to quit all other cases None
    """
    while True:
        print("\tStore Menu")
        print("\t----------")
        for item in enumerate(user_menu.keys(),1):
            print(f"{item[0]}. {item[1]}")
        try:
            menu_item = int(input("Please choose a number: "))
        except ValueError:
            print("Error with your choice! Try again!")
            continue
        if 1 <= menu_item <= len(user_menu.keys()):
            # Calling the required function from dispatch table
            chosen_function = list(user_menu.values())[menu_item-1]
            if chosen_function() == QUIT:
                break


def list_products():
    """Print products available in the store to the UI"""
    products = best_buy.get_all_products()
    products_numbered = enumerate(products,1)
    for number,product in products_numbered:
        print(number,". ", end="")
        print(f"{product.name}, "
              f"Price: €{product.price}, Quantity: {product.quantity}")


def show_total_items():
    """Print the total stock available in the store"""
    total_items = best_buy.get_total_quantity()
    print(f"Total of {total_items} in store")


def product_prompt(items):
    """For user entry to accept the product to be ordered"""
    while True:
        try:
            product_id = input("Which product # do you want? ")
            # User entered blank, meaning the program needs to be ended
            if not product_id:
                return None
            # Convert the user entered option to integer
            product_id = int(product_id)
        except ValueError:
            print("Invalid Selection")
            continue

        no_valid_product = False
        # Loop through the tuple to find the chosen product
        for num, product in items:
            if num == product_id:
                return product
            else:
                no_valid_product = True
        if no_valid_product:
            print("Invalid Selection")
        else:
            break

def quantity_prompt(item):
    """For user to enter quantity to be ordered"""
    while True:
        try:
            quantity = float(input("Please enter the quantity: "))
        except ValueError:
            print("Invalid quantity")
            continue
        if quantity > item.get_quantity():
            print("Insufficient Quantity! Order cannot be created")
            return None
        return quantity


def create_order():
    """Order Creation"""
    # initialize shopping cart
    shopping_cart = []
    print("-----")
    list_products()
    item_list = best_buy.get_all_products()
    items = list(enumerate(item_list,1))
    print("-----")
    print("When you want to finish order,enter empty text.")
    while True:
        item = product_prompt(items)
        if item:
            quantity = quantity_prompt(item)
            if quantity:
                shopping_cart.append((item,quantity))
                print("Product added to list!")
        else:
            break
    if shopping_cart:
        try:
            total_price = best_buy.order(shopping_cart)
            print("********")
            print(f"Order made! Total payments: €{total_price}")
        except Exception as error:
            print(error)


def quit():
    """To quit from UI @ CLI"""
    return True

def main():
    """Main"""
    user_menu = {
        "List all products in store" : list_products,
        "Show total items in store": show_total_items,
        "Make an order": create_order,
        "Quit": quit
    }

    start(user_menu)

if __name__ == '__main__':
    main()



