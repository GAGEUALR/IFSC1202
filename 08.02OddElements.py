x = input("Enter Values Seperated by Spaces: ")

b = x.split()

for i in range(len(b)):
    b[i] = int(b[i])
    if b[i] % 2 != 0:
        print(b[i])