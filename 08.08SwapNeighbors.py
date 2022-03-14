x = input("Enter Values Seperated by Spaces, in Ascending Order: ")

b = x.split(" ")
count = int(0)
c = 0
for i in range(0, len(b)-1, int(2)):
    c = b[i]
    b[i] = b[i + 1]
    b[i + 1] = c

print(b)