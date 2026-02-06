# List Transformation:
# Given a list of prices [10, 25, 4.50, 8, 100],
# use a for loop to create a new list where every price is increased by 10% tax.

price=[10, 25, 4.50, 8, 100]

def increasePrice(price):
    newPrice = []
    for i in price:
        newPrice.append(i+(i*0.10))
    return newPrice

print(increasePrice(price))


