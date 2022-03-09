def propercase(s):
    s.upper(s[0])
    s.lower(s[1:-1])

def RemoveNewLine(s):
     s.replace("\n", "")

def trim(s):
    s.strip(s)

def Firstname(s, x):
    x = (s.find(" "))
    y = str(s[0:x])
    y.propercase(y[0:x])
    return y

def Lastname(s):
    y = s.rfind(" ")
    s.propercase(s[y:-1])

def Middlename(s):
    x = s.find(" ")
    y = s.rfind(" ")
    s.propercase()


a = open("Names.txt", "r")
s = a.readline()
x = s.find(" ")
y = s.rfind(" ")
while s != "":
    s = str(s)
    print("{} {} {} {}".format(s, Firstname(s, x), Middlename(s), Lastname(s)))
    s = a.readline()