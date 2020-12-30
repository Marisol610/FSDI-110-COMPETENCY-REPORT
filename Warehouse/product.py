class Product:
    id = 0
    title = ''
    category = ''
    stock = 0
    price = 0.0
    total = 0


    #contructor/method. start with double under score, the contructor will receive its own class and its own self he "self" is the same as the "this" in java
    def __init__(self, id, title, category, stock, price):
        self.id = id
        self.title = title
        self.category = category
        self.stock = stock
        self.price = price

    