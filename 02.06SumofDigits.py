number = int(input("Enter a three digit number: "))

x = 10

y = 100

onesdigit = (number % x)

tensdigitwrong = (number // x)

hundigit = (number // y)

tensdigitright = (tensdigitwrong - (hundigit * x))

print(onesdigit + tensdigitright + hundigit)



