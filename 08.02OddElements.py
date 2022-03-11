x = input("Enter Values Seperated by Spaces: ")

b = x.split()

for i in range(len(b)):
    b[i] = int(b[i])

print(b[::2])