one = input("Enter First Number: ")
two = input("Enter Second Number: ")
three = input("Enter Third Number: ")


if one != two and two != three and one != three:
    print(0)

elif one == two and two == three and one == three: 
    print(3)

else:
    print(2)
