class cars():
    def __init__(self, Year, Make, Speed):
        self.Year = Year
        self.Make = Make
        self.Speed = 0

    def Accelerate(self):
        mycar1.Speed += newspeed
        return mycar1.Speed

    def Brake(self):
        mycar1.Speed += newspeed
        return mycar1.Speed

carlist = open("10.03cars.txt", "r")
x = carlist.readline()
carsplit = x.split(",")

mycar1 = cars(carsplit[0], carsplit[1], 0)

print("Make:{}Year:{}".format(mycar1.Make, mycar1.Year))
print("\n{:<10}{:<10}".format("Change","Speed"))

for i in range(0, 4):
        x = carlist.readline()
        x = int(x)
        newspeed = x
        if newspeed > 0:
            mycar1.Accelerate()
        if newspeed < 0:
            mycar1.Brake()
        print("{:<10}{:<10}".format(newspeed, mycar1.Speed))
