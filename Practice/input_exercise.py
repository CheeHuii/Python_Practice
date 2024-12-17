# To calculate are
length = float(input("Enter your length: "))
width = float(input("Enter your width: "))
area = length * width
print(f"Your area is {area}")

# Shopping system
item = str(input("What would you like to buy?: "))
quantity = int(input("How many are you buying?: "))
price = float(input("Do you know the price?: "))

total = quantity * price

print(f"So you bought {quantity} {item} with the price of {price} each. \nTotal is: RM {total}")