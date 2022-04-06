car = open("CarSales.txt")


carlist = []

totalcars = 0 
totspend = 0

for i in range(1, 1001):
    x = car.readline()
    x = x.replace(",", " ")
    x = x.replace("\n", "")
    x = x.split(" ")
    x = str(x)
    x = x.replace("[", "")
    x = x.replace("'", "")
    x = x.replace(",", "")
    x = x.replace("]", "")
    carlist.append(x)
    totalcars += 1

print(carlist)

print("The total number of cars is: ", totalcars)

carmake = input("Enter a Car Make: ")

if carmake == " ":
    print("Invalid")

carmake = carmake.lower()
carmake = carmake.capitalize()
count = 0

for i in range(len(carlist)):
    carcount = carlist.find(carmake)
    if carcount != "" or " ":
        count += 1


print