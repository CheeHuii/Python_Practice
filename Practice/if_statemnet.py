age = int(input("Input your age: "))

if age > 18:
    print("Alright u gud to go.")
# For elif, pay attention to order.
# For this instance, below condition should be on top.
elif age > 20:
    print("No, u just a worm.")
else:
    print("Thats nono.")