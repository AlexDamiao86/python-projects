prices = {
    "banana" : 4, 
    "apple" : 2, 
    "orange" : 1.5, 
    "pear" : 3
}

stock = {
    "banana" : 6,
    "apple" : 0, 
    "orange" : 32, 
    "pear": 15
}

total = 0
for key in prices:
    print (key)
    print ("price: %s" % prices[key])
    print ("stock: %s" % stock[key])
    print ("value: %s\n" % (prices[key] * stock[key]))
    
    total = total + prices[key] * stock[key]
    
print ("total: %s\n" % total)

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices[item]
            stock[item] = stock[item] - 1
    return total

lista = ["orange", "orange", "pear", "apple", "banana"]
print("List: %s" % lista)
print("List price: %s" % compute_bill(lista))
print("Stock after sell: %s" % stock)

