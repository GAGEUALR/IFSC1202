x = input("Enter Values Seperated by Spaces: ")

b = x.split(" ")
count = int(0)
for i in range(len(b) -1):
    if b[i] != b[i-1]:
        count += int(1)

print(count)

