year = int(input("Enter a Year: "))

if year % 4 == 0 and year % 100 != 0:
    print("LEAP YEAAAARRR")

elif year % 4000 == 0:
    print("LEAP YEAAAARRR")


else:
    print("not a leap year :(")