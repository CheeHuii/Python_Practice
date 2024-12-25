Operation = input("Please enter ur operation (+,-,*,/): ")
Number_1 = float(input("Please enter first number: "))
Number_2 = float(input("Please enter second number: "))

if Operation == "+":
    print(f"Result is: " , round(Number_1 + Number_2))
if Operation == "-":
    print(f"Result is: " , round(Number_1 - Number_2))
if Operation == "*":
    print(f"Result is: " , round(Number_1 * Number_2))
if Operation == "/":
    print(f"Result is: " , round(Number_1 / Number_2))
else:
    print("Not a valid operation. Or invalid number(s)")
