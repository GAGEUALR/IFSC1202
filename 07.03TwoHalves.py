s = input(str("Enter a phrase: "))

a = int(len(s))

x = int(a / 2)

y = int(a / 2)
y += int(a % 2)

firstpart = (s[y:])
secondpart = (s[:-x])

print("{}{}".format(firstpart,secondpart))