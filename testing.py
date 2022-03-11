s = input("Enter a value: ")

a = s.split(" ")

for i in range(len(a)):
	print(a[::2])