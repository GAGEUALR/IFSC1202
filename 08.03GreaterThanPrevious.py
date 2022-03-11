x = input("Enter Values Seperated by Spaces: ")

b = x.split(" ")

for i in range(len(b)):
    if b[i] < b[i + 1]:
        print(b[i + 1])