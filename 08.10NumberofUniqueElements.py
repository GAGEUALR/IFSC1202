x = input("Enter Values Seperated by Spaces: ")

b = x.split(" ")

count = (len(b))

x = 0

for i in range(len(b[1::])):
    if x == 2:
            print(i)
    for j in range(len(b[1::])):
        if j == i:
            x += 1
            
