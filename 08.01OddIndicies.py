s = input("Enter a value: ")

x = s.split(" ")

for i in range(len(x)):
	print(x[::2])