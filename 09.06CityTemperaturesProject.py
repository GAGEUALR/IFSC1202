tempfile = open("09.06CityTemps.txt", "r")
x = tempfile.readline()

a = []

while x != "":
    a.append([x])
    x = tempfile.readline()

tempfile.close()

print("{:>5}{:>5}{:>5}{:>5} {:>5} {:>5}{:>5}{:>5}{:>5}".format("City", "Sun", "Mon", "Tues", "Wed","Thurs","Fri","Sat","Sun","Av."))

for i in range(len(a)):
    if a[i] == int: