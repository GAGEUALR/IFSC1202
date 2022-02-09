a = int(input("Enter Point A: "))
b = int(input("Enter Point B: "))
c = int(input("Enter Point C: "))

var1 = (b - a)

var2 = (c - a)

if var1 < var2:
    print(var1)

elif var2 < var1:
    print(var2)