from math import pi

def diameter(x):
        b = (x * 2)
        return b

def circumference(x):
    c = (2 * pi * x)
    return c

def area(x):
    d = (pi * x ** 2)
    return d 

print("{:>15s} {:>15s} {:>15s} {:>15s}".format("Radius","Diameter","Circumference","Area"))
radiusfile = open("06.01radius.txt", "r")
x = radiusfile.readline()

while x != "":
    x = float(x)
    print("{:15.5f} {:15.5f} {:15.5f} {:15.5f}".format(x, diameter(x), circumference(x), area(x)))
    x = radiusfile.readline()
radiusfile.close()


