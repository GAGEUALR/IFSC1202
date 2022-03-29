x = int(input("Enter the number of Rows: "))
y = int(input("Enter the number of Columns: "))

a = []

for i in range(y):
    w = input("Enter a line of Data: ")
    a.append([w])



maxnumber = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        if (a[i]) > maxnumber:
            maxnumber = j
            coord = i

print(maxnumber)
    
