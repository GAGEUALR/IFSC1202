x = int(input("Enter a Number: "))
y = 10

tens = (x // y)

ones = (x % y)

print(tens)

print(ones)

newnumber = ((ones * y) + tens)

print(newnumber)