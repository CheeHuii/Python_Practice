# or , not, and

temp = 30
is_raining = False

if temp > 20 and is_raining:
    print("Its humid")
elif temp == 20:
    print("Its 20 degree")
elif temp < 20 and not is_raining:
    print("Its chill")
elif temp < 15:
    print("Tis lower than 15 degree")
elif temp > 25 or is_raining:
    print("its hot or raining")