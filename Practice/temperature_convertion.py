temp = float(input("Input your temperature: "))
unit = (input("Input your unit: "))

if unit == "c" or unit == "C":
    temp = round((temp *9) /5 + 32,2)
    unit = "Farenheit"
    print(f"Your temp is {temp} {unit}")
elif unit == "f" or unit == "F":
    temp = round((temp - 32) * 5/9 ,2)
    unit = "Celcius"
    print(f"Your temp is {temp} {unit}")
else:
    print(f"{unit} is invalid, please input c or f.")