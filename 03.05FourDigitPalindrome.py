spooky = int(input("Enter a Four Digit Number: "))

a = (spooky % 10)
b = (spooky % 100)
c = (spooky % 1000 )
f = (spooky % 10000)

d = float(b //10)
e = float(c // 100)
g = float(f // 1000)

 #print(a, d, e, g)

if a == g and d == e:
    print("YES!")

else:
    print("NOOOOO")