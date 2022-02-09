spooky = int(input("Enter a Three Digit Number: "))

a = (spooky % 10)
b = (spooky % 100)
c = (spooky % 1000 )

d = float(b //10)
e = float(c // 100)



print(a, d, e)

if e < d and d < a:
    print("YES!")

else:
    print("NOOOOOOOO")