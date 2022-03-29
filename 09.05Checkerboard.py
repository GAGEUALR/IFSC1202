n = int(input("Enter the Size of the Checkerboard: "))

a = []

for i in range(n):
    a.append([" "] * n)

for i in range(n):
    a[0] = "+"
    a[i][0] = "-"
    a[i] = "|"
    a[n - 1] = "+"

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()