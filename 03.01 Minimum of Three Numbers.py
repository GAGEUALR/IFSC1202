x = input("Enter First Number: ")
y = input("Enter Second Number: ")
z = input("Enter Third Number: ")

if x < y and x < z:
    print("First Number, " + x )
if y < x and y < z:
    print("Second Number, " + y )
if z < x and z < y:
    print("Third Number, " + z )