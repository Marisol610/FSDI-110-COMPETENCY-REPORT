import os

def print_menu():
    print("*" * 40)
    print("   Welcome to PyWarehouse   ")
    print("*" * 40)

    print("[1] Register Product")
    print("[2] View Catalog")
    print("[3] Display out of stock")
    print("[4] Total value for in stock products")
    print("[5] Cheapest Product")
    print("[6] Remove Product")
    print("[7] Update Product Price")
    print("[8] Update Product Stock")
    print('')

    print("[a] Calculate age")
    print("[b] Calculate Tip")
    print('')


    print(" [x] Close the system")

def print_header(header_text):
    clear()
    print('_' * 40)
    print(header_text)
    print('_' * 40)


def clear():
    if(os.name == 'nt'):
        return os.system("clear")
    else:
        return os.system("clear")
    

def print_line():
    print("-"* 40)

def print_product(prod):
    print(
        str(prod.id )
          + "|" + prod.title
          + "|" + prod.category
          + "|" + str(prod.stock)
          + "|" + str(prod.price)
    )