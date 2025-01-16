# [start:end:step]
# [inclusive:exclusive:step]

CC_number = "1234-4567-8912-3456"

print(CC_number[0])
print(CC_number[0:4])
print(CC_number[:4])
print(CC_number[5:9])
print(CC_number[5:])
print(CC_number[-1])
print(CC_number[::2])
print(CC_number[::3])

Last_CC = input("Enter your number: ")[-4:]

print("Last four is: ",Last_CC)
