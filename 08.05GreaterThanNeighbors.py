x = input("Enter Values Seperated by Spaces: ")

b = x.split(" ")
count = 0

for i in range(1, len(b)-1):
    if b[i] > b[i + 1] and b[i] > b[i -1]:
            count += 1
    
print(count)