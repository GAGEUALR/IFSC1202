s = input(str("Enter a String with two H: "))

a = (s.find("h"))
b = s.rfind("h")
a -= 1

c = (s[b:a:-1])

print(c)