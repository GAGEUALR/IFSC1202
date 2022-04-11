class RetailItem ():
    def __init__(self, description = "", unitsonhand = 0, price = 0):

        self.description = description
        self.unitsonhand = unitsonhand
        self.price = price

    def InventoryValue(self):
        InventoryValue = (float(self.Price) * float(self.UnitsonHand))
        return InventoryValue

def print_itemlist(itemlist):
	print("{:>14s}{:>14s}{:>14s}{:>14s}".format("Type", "Diameter", "Pressure", "Circumference"))
	for i in range(len(itemlist)):
		print ("{:>14s}{:14.2f}{:14.2f}{:14.2f}".format(itemlist[i].itemType, itemlist[i].Diameter, itemlist[i].Pressure, itemlist[i].Circumference()))

def find_item(itemlist, itemtofind):
	for i in range(len(itemlist)):
		if itemlist[i].itemType == itemtofind:
			return i
