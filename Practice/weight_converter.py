weight = float(input("Input your weight: "))
unit = (input("Input your unit(L/Kg): "))

if unit == "Kg" or unit == "kg":
    weight = round(weight * 2.205,2)
    unit = "Pound(s)"
    print(f"Your converted weight is {weight} {unit}")
elif unit == "L" or unit == "l":
    weight = round(weight / 2.205,2)
    unit = "Kilograms"
    print(f"Your converted weight is {weight} {unit}")
else:
    print(f"{unit} is invalid input.")
