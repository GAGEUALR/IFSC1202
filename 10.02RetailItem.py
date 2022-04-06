class item ():
    def __init__(self, Description, UnitsonHand, Price):

        self.Description = Description
        self.UnitsonHand = UnitsonHand
        self.Price = Price

    def InventoryValue(self):
        InventoryValue = (float(self.Price) * float(self.UnitsonHand))

        return InventoryValue

print("{:<20}{:<20}{:<20}{:<20}".format("Description:", "Units on Hand:", "Price:", "Inventory Value:"))
retaillist = open("10.02.inventory.txt", "r")

x = retaillist.readline()
retailobjs = x.split(",")
myobj1 = item(retailobjs[0], retailobjs[1], retailobjs[2])
print("{:<20}{:<20}{:<20}{:<20.2f}".format(myobj1.Description, myobj1.UnitsonHand, myobj1.Price.replace("\n", ""), myobj1.InventoryValue()))

x = retaillist.readline()
retailobjs = x.split(",")
myobj2 = item(retailobjs[0], retailobjs[1], retailobjs[2])
print("{:<20}{:<20}{:<20}{:<20.2f}".format(myobj2.Description, myobj2.UnitsonHand, myobj2.Price.replace("\n", ""), myobj2.InventoryValue()))

x = retaillist.readline()
retailobjs = x.split(",")
myobj3 = item(retailobjs[0], retailobjs[1], retailobjs[2])
print("{:<20}{:<20}{:<20}{:<20.2f}".format(myobj3.Description, myobj3.UnitsonHand, myobj3.Price, myobj3.InventoryValue()))

retaillist.close()