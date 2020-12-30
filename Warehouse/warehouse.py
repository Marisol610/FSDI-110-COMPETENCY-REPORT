#imports
from menu import print_menu, print_header, clear, print_line, print_product
from homework import calculate_age, calculate_tip
from product import Product
#global variables

catalog =[]
next_id = 1

#functions



def register_product():
    global next_id 
    try:
        print_header("Register a new Product")
        #title, category, stock, price
        title= input("Please provide the Title:")
        category = input("Please provide the Category")
        stock = int(input("Please provide the Stock Qty:"))
        price = float(input("Please provide the Price:"))


        #create obj
        the_product = Product(next_id, title, category, stock, price)
        next_id = next_id + 1

  # add obj to a list
        catalog.append(the_product)

        print_line()
        print("**Product Registered")

    except:
        print("**** Error: verify values and try again")


def print_catalog():
        print_header("Current Catalog")

        for prod in catalog:
            print_product(prod)

def print_stock():
    print_header("Stock available 0")

    for prod in catalog:
        if(prod.stock == 0):
            print_product(prod)


def total_value():
    print_header("Total value for in stock products")
    
    total = 0.0
    for prod in catalog:
        total = total + (prod.stock * prod.price)

    print(str(total))


def cheapest_prod():
    print_header("Cheapest product")

    prices = []
    
    for prod in catalog:
        prices.append(prod.price)

    cheapest = min(prices)
    print("The cheapest product" + str(cheapest))

def cheapest_product_adv():
    print_header("Cheapest product in our catalog")

    if(len(catalog)<1):
        print("**Error, empty catalog. Must register product first")
        return

    cheapest =catalog[0]

    for prod in catalog:
        if(prod.price < cheapest.price):
            cheapest = prod

    print_product(cheapest)



def delete_product():
    print_header(" Remove Product")

    print_catalog()
    id =input("Choose the product ID you wish to remove:")
    found = False

    for prod in catalog:
        if(str(prod.id )== id):
            catalog.remove(prod)
            found =True
    if(found):
        print(" ** Product Removed!!")
    else:
            print("** Error: Invalid ID")

    input("Press enter to Confirm")
    print(str(prod.id) + "REMOVED")

    
    
def update_price():
    print_header(" Update Price")

    print_catalog()
    id = input("Choose the Product you wish to update price")

    price = input("Enter the update price")
    found = False

    for prod in catalog:
        if(str(prod.id)== id):
            prod.price= (float(price))
            found =True

    if(found):
        print("** Product price has been updated")
    else:
        print(" ** Error!! cannot update price!")


def update_stock():
    print_header(" Update Stock")

    print_catalog()
    id = input("Enter product ID")

    
    qty = int(input("Enter the quantity"))
    found = False

    for prod in catalog:
        if(str(prod.id)== id):
            prod.stock = (int(qty))
            found = True

    if(found):
        print("***Stock has been updated***")
    else:
        print("***Error!! cannot update stock")


#intructions

opc= ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input("Please choose an option:")


    #compare based on the user option
    if(opc == "1"): # compare strings with strings
        register_product()
    elif(opc == '2'):
        print_catalog()

    elif(opc == '3'):
        print_stock()

    elif(opc == '4'):
        total_value()

    elif(opc == '5'):
        cheapest_prod()

    elif(opc == '6'):
        delete_product()

    elif(opc == '7'):
        update_price()

    elif(opc == '8'):
        update_stock()

    elif(opc == 'a'):
        calculate_age()
    elif(opc == 'b'):
        calculate_tip()

    input("Press enter to continue...")

print("Good bye!!")



