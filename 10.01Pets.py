class pet():
    def __init__(self, Name, Type, Age):
        self.Name = Name
        self.Type = Type
        self.Age = Age


petfile = open("10.01Pets.txt", "r")
x = petfile.readline()
petline = x.split(",")
mypet1= pet(petline[0], petline[1], petline[2])

x = petfile.readline()
petline = x.split(",")
mypet2= pet(petline[0], petline[1], petline[2])

x = petfile.readline()
petline = x.split(",")
mypet3= pet(petline[0], petline[1], petline[2])

print("{:<10}{:<10}{:<10}".format("Name", "Type", "Age\n"))
print("{:<10}{:<10}{:<10}".format(mypet1.Name, mypet1.Type, mypet1.Age))
print("{:<10}{:<10}{:<10}".format(mypet2.Name, mypet2.Type, mypet2.Age))
print("{:<10}{:<10}{:<10}".format(mypet3.Name, mypet3.Type, mypet3.Age))
