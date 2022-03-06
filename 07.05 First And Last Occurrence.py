s = input(str("Enter a String: "))

a = s.find("f")
b = s.rfind("f")

if b == a:
    b = -1

if a != -1:
    print(a)

if b != -1:
    print(b)

if a == -1:
    print("")

if b == -1:
    print("")