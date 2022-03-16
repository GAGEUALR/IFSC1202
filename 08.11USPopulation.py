popfile = open("08.11USPopulation.txt", "r")

def change(x):   #not sure how to get the readfile function to go backwards or save the last readline in a variable ?,
        for i in range(x):
                if x =="":
                        j = print("N/A")
                if x != "":
                        j = x - x[i - 1]
                if x[i - 1] == "": 
                 j = print("N/A")
        return j

print("{:<15} {:<15} {:<15} {:<15}".format("Year", "Population", "Change", "Percent Change"))

year = 1950
b = []

while year != 1991:
    for i in range(0, 41):
        b.append(year)
        year += 1

x = popfile.readline()
x = (int(x) * 1000)

for i in range(0, 41):
        print("{:<15} {:<15}".format(b[i], x,)) #{:<15} ,change(x) 
        x = []
        x = popfile.readline()
        if x == "":
                break
        x = (int(x))
        x *= 1000