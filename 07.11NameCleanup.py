def propercase(s):
    if len(s) == 0:
        return s
    s = s.lower()
    s = s[0].upper() + s[1:]
    return s

def RemoveNewLine(s):
     s = s.replace("\n", "")
     return s

def trim(s):
    s = s.strip()
    return s

def Firstname(s):
    s = trim(s)
    x = (s.find(" "))
    y = (s[0:x])
    return propercase(y[0:x])

def Lastname(s):
    s = trim(s)
    y = s.rfind(" ")
    z = (s[y+1:])
    return propercase(z)

def Middlename(s):
    s = trim(s)
    x = s.find(" ")
    y = s.rfind(" ")
    z = (s[x:y])
    a = trim(z)
    b = propercase(a)
    if len(b) == 1:
        b = b + "."
    return b


a = open("Names.txt", "r")
s = a.readline()


print("{:10} {:10} {:10} {}".format("First", "Middle", "Last", "\n----------------------------"))

while s != "":
    s = str(s)
    print("{:10s} {:10s} {:10s}".format(Firstname(s), Middlename(s), Lastname(s)))
    s = a.readline()