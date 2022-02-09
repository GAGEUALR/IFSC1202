old = float(input("Enter From Value: "))
unit = (input("Enter From Unit: (in, ft, yd, mi): "))
new = (input("Enter To Unit: (in, ft, yd, mi): "))



if (unit != "in") or (unit != "ft") or (unit != "yd") or (unit != "mi"):
    print("FromUnit is not Valid.")

if (new != "in") or (new !=  "ft") or (new != "yd") or (new != "mi"):
    print("ToUnit is not Valid.")



if unit == "in" and new == "in":
    print(old * 1)

if unit ==  "ft" and new == "in":
    print(old // 12)

if unit == "yd" and new == "in":
    print(old // 36)

if unit == "mi" and new == "in":
    print(old // 63360)



if unit == "in" and new ==  "ft":
    print(old //12)

if unit ==  "ft"' and new ==  "ft"':
    print(old * 1)

if unit == "yd" and new ==  "ft":
    print(old // 3)

if unit == "mi" and new ==  "ft":
    print(old // 5280)



if unit == "in" and new == "yd":
    print(old // 36)

if unit ==  "ft" and new == "yd":
    print(old // 3)

if unit == "yd" and new == "yd":
    print(old * 1)

if unit == "mi" and new == "yd":
    print(old // 1760)



if unit == "in" and new == "mi":
    print(old // 36)

if unit ==  "ft" and new == "mi":
    print(old // 3)

if unit == "yd" and new == "mi":
    print(old * 1)

if unit == "mi" and new == "mi":
    print(old // 1760)