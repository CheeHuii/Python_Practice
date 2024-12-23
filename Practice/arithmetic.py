i = 1
i += 1
print(i)

i = 1
i -= 1
print(i)

i = 2
i *= 2
print(i)

i = 2
i /= 2
print(i)

i = 2
i **= 2

j = 2**4
print(i)
print(j)

i = 10 % 3
print(i)

i = 3.142
print(round(i))

#absolute value away from 0
i = -4
j = 3
print(abs(i), abs(j))

i = pow(2,3)
print(i)

i = 1
j = 50
k = -1
print(max(i,j,k))
print(min(i,j,k))

import math
print(math.pi)
print(math.e)
print(math.sqrt(4))
print(math.ceil(9.2))
print(math.floor(9.2))

radius = float(input(f"Input radius of circle: "))
print(f"Circumference = ", 2*(math.pi)*radius)
print(f"Rounded Circumference = ", round(2*(math.pi)*radius,2))
print(f"Area = ", [(math.pi)*(pow(radius,2))])

a = float(input(f"Input a:"))
b = float(input(f"Input b:"))
c = math.sqrt(pow(a,2)+pow(b,2))
print(c)