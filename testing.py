x = input(":")

for a, b in zip(x, x[1:]):
    if a * b > 0:
        print(f"Found pair {a} {b}")
        break
else:
    print("NONE")