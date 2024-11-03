import math

products = {
    "FR1": {
        "Name": "Fruit Tea",
        "Price": 3.11,
    },
    "SR1": {
        "Name": "Strawberries",
        "Price": 5.00,
    },
    "CF1": {
        "Name": "Coffee",
        "Price": 11.23,
    }
}

class Trolley():
    # define a trolley class with the four requested functions
    def __init__(self, contents):
        self.contents = contents

    def add_product (self, product_label):
        self.contents.append(product_label)

    def remove_product (self, product_label):
        self.contents.remove(product_label)

    def view (self):
        for product in set(self.contents):
            print (str(self.contents.count(product)) + " x " + products[product]['Name'])

    def total_cost(self, product_catalogue):
        # before running this, we will need to define a "product catalogue"
        # to link the product dictionary above with the created instances of the Product class
        running_cost = 0
        for p in product_catalogue:
            running_cost += product_catalogue[p]["Product"].total_product_cost(self.contents.count(p))
        return (running_cost)


class Product():
    # define a product class, which product cost varying according to the offer
    def __init__ (self, price, offer = None, reduction_amount = None, reduction_min_quantity = None):
        self.price = price
        if offer in [None, 'BOGOF', 'Reduced']:
            self.offer = offer
        else:
            raise ValueError('invalid offer input')  
        self.reduction_amount = reduction_amount
        self.reduction_min_quantity = reduction_min_quantity
    
    def total_product_cost (self, quantity):
        if self.offer == None:
            return (self.price * quantity)
        
        if self.offer == "BOGOF":
            bogof_count = math.ceil(quantity / 2) 
            return (self.price * bogof_count)
        
        if self.offer == "Reduced":
            if quantity < self.reduction_min_quantity:
                actual_price = self.price
            if quantity >= self.reduction_min_quantity:
                actual_price = self.price - self.reduction_amount
            return (actual_price * quantity)
    

    