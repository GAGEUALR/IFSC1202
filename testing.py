petfile = open("10.01Pets.txt", "r")
x = petfile.readline()

class pet ():
	def __init__(self, name=" ", type =" ", age = 0):

		self.name = name
		self.type = type
		self.age = age

mypet1 = pet(x)
x = petfile.readline
mypet2 = pet(x)
x = petfile.readline
mypet3 = pet(x)

print (mypet1.Name, mypet1.type, mypet1.age, mypet1.age)
print (mypet2.Name, mypet2.type, mypet2.age, mypet2.age)
print (mypet3.Name, mypet3.type, mypet3.age, mypet3.age)
print (mypet4.Name, mypet4.type, mypet4.age, mypet4.age)