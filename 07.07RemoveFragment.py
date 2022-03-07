s = input(str("Enter a String with two H: "))

a = (s.find("h"))
b = s.rfind("h")
b += 1

c = str(s.replace(s[a:b:1], ""))

print("{}".format(c))





