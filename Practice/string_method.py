name = input("Enter your name: ")

name_length = len(name)
first_i_in_name = name.find("i")
# r mean reverse
last_i_in_name = name.rfind("i")
cap_name = name.capitalize()
upper_name = name.upper()
lower_name = name.lower()
# Check if ONLY numbers
check_num = name.isdigit()
# Check if ONLY alphabet, space is NOT alphabet
check_alpha = name.isalpha()

Helpline = "012-3450 6789"
check_zeros = Helpline.count("0")

updated_helpline = Helpline.replace("0", "5")

print(f"Your name {name} is {len(name)} long.")
print(f"First i in your name is the number {first_i_in_name + 1} character")
print(f"Last i in your name is the number {last_i_in_name + 1} character")
print("0 position means there is none")
print(f"Bye {cap_name}") 
print(f"Bye {upper_name}")
print(f"Bye {lower_name}")
print(check_num)
print(check_alpha)
print(f"There is {check_zeros} 0 in helpline number!")
print(f"This is an updated helpline {updated_helpline}")
