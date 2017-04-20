shopping_list = ["banana", "orange", "apple"]

# stock count for items in dictionary 
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

# prices for items
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Checks stock count and adds price if product is in stock
# subtracts an item from stock after inclusion
def compute_bill(shopping_list):
    total = 0
    for food in shopping_list:
        if stock[food] > 0:
            total =  total + prices[food]
            stock[food] = stock[food] - 1
            
        
    return total
    
    
