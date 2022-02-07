x = float(input("Enter a number: "))

tensdigit = (x % 1)

y = round(tensdigit, 1)

z = (tensdigit * 10)

print("The Tens Digit is {}".format(int(z)))