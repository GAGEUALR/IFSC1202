popfile = open("08.11USPopulation.txt", "r")

def percentchange (x):
        for i in range(x):
                popfile.readline(x)
                
x = []
x = popfile.readline()
x = (int(x) * 1000)

year = 1950
b = []
print("{:<15} {:<15} {:<15} {:<15}".format("Year", "Population", "Change", "Percent Change"))

while year != 1991:
    for i in range(0, 41):
        b.append(year)
        year += 1

for i in range(0, 41):
        print("{:<15} {:<15} {:<15}".format(b[i], x, percentchange(x)))
        x = []
        x = popfile.readline()
        if x == "":
                break
        x = (int(x))
        x *= 1000

popfile.close()

        