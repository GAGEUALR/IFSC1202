firstnumber = int(input("Enter the first two digit number: "))
secondnumber= int(input("Enter the second two digit number: "))

a = (firstnumber % 10)
c = (secondnumber % 10)

b = (firstnumber //10)
d = (secondnumber // 10)

print("Merged Number is {}{}{}{}".format(b,d,a,c))

