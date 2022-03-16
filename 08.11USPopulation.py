
print("{:<15} {:<15} {:<15} {:<15}".format("Year", "Population", "Change", "Percent Change"))

b = []
popfile = open("08.11USPopulation.txt", "r")
x = popfile.readline()
while x != '':
        x = (int(x) * 1000)
        b.append(x)
        x = popfile.readline()
popfile.close()

year = 1950
print("{:<15d} {:<15d} {:<15s} {:<15s}".format(year, b[0], "N/A", "N/A")) 

minchange = b[1] - b[0]
minyear = year

maxchange = b[1] - b[0]
maxyear = year


year = year + 1

for i in range(1, len(b)):
        change = b[i] - b[i-1]
        percentchange = (((change)/b[i - 1])* 100)
        print("{:<15} {:<15} {:<15d} {:>15.2f}%".format(year, b[i], change, percentchange))
        if b[i] - b[i-1] < minchange:
                minchange = b[i]-b[i-1]
                minyear = year
        year = year + 1
        if b[i] - b[i - 1] > maxchange:
                maxchange = b[i]-b[i -1]
                maxyear = year
        #if i > 1:
                #avchange = ((percentchange) + (percentchange(b[i - 1])))/i

print("\nMinimum Change = ", minchange, "({})".format(minyear))

print("Maximum Change = ", maxchange,"({})".format(maxyear))

# couldn't figure out avchange, kept getting "can't call float" error.
