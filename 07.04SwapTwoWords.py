s = str(input("Enter a string: "))

x = s.find(" ")

print(s[x:] + " " + s[:x])