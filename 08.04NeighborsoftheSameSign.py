x = input("Enter Values Seperated by Spaces: ")

b = x.split(" ")
count = 0

for i in range(len(b)-1):
    if b[i] <= str(0) and b[i +1] <= str(0):
        print(b[i], b[i +1])
    if b[i] >= str(0) and b[i + 1] > str(0):
        print([b[i], b[i + 1]])