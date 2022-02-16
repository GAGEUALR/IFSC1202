number = 1
x = 0 
y = 0
z = 0
while number != 0:
    number = int(input("Enter a Number (zero to quit): "))
    if number != 0:
        y = y + 1
        x = x + number 
        z = x / y

print(z)