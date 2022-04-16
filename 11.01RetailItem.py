class RetailItem ():
    def __init__(self, description = "", unitsonhand = 0, price = 0):

        self.description = description
        self.unitsonhand = unitsonhand
        self.price = price

    def InventoryValue(self):
        InventoryValue = (float(self.price) * float(self.unitsonhand))
        return InventoryValue

    def ChangePrice (self, pricechange):
        

def print_itemlist(itemlist):
	print("{:<30}{:<30}{:<30}{:<30}\n".format("Description", "Units on Hand", "Price", "Inventory Value"))
	for i in range(len(itemlist)):
		print ("{:<30}{:<30}{:<30.2f}{:<30.2f}".format(itemlist[i].description, itemlist[i].unitsonhand, itemlist[i].price, itemlist[i].InventoryValue()))

def find_item(itemlist, itemtofind):
	for i in range(len(itemlist)):
		if itemlist[i].description == itemtofind:
			return i


itemlist = []

itemfile = open("inventory.txt", "r")
x = itemfile.readline()

while x != "":
    xsplit = x.split(",")
    item1 = RetailItem(xsplit[0], xsplit[1], float(xsplit[2]))
    itemlist.append(item1)
    x = itemfile.readline()
    
print_itemlist(itemlist)

upfile = open("inventoryupdate.py", "r")
y = upfile.readline()

while y != "":
    ysplit = y.split(",")
    itemlist[find_item(itemlist, ysplit[0])].ChangePrice() $$$$$$$$$$$$$$$$$$$
    y = upfile.readline()


print()