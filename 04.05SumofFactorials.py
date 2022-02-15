N = int(input("Enter N: "))
result = 0
x = 1
for f in range (1, N+1):
    x = 1
    for i in range (1, f+1):
        x = i * x
    result = result + x
print(result)