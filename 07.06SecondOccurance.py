s = input(str("Enter a String: "))

b = s.rfind("f")
a = s.count("f")

if a == 0:
    print("Zero f")

if a == 1:
    print("One f,", b)