x = float(input("Enter Legnth of Race in Kilometers: "))
y = float(input("Enter Minutes: "))
sec = float(input("Enter Seconds: "))
miles = float(x * .621)
secinmin = float(y * 60)
hours = float(sec + secinmin / 3600)
greeting1 = "mph"
mph = float(miles / hours)
print(mph)
