def percentchange():
    a = stockfile.readline()
    x = stockfile.readline()
    while x and a != 0:
        temp1 = float(x) 
        temp2 = float(a)
        ctemp = (temp1 - temp2)/ temp1 * 100
        a = stockfile.readline()
        x = stockfile.readline()
        return ctemp




print("{:<10} {:<10}".format("Price", "Change"))
stockfile = open("06.02 Stock.txt", "r")
x = stockfile.readline()
a = stockfile.readline()

print(percentchange())

#while x != "":
    x = float(x)
    a = float(a)
    print("{:<10}{:<10}\n{:<10}".format(x, a, percentchange()))
    x = stockfile.readline()

    

stockfile.close