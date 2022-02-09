x = input("Enter a First Number: ")
y = input("Enter a Second Number: ")
z = input("Enter  Third Number: ")


if x < y and x < z and y < z:
    print(x, y, z,)

if y < x and y < z and x < z:
    print(y, x, z)

if z < x and z< y and x < y:
    print(z, y, x)

if x < y and x < z and z < y:
    print(x, z, y)

if y < x and y < z and z < x:
    print(y, z, x)

if z < x and z < y and y < x:
    print(z, y, x)