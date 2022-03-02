ftemps = open("06.03 FTemps.txt", "w")


for i in range(1, 10):
    c = (int(i) - int(32)) * 5 / 9
    c = str(c)
    ftemps.write(c + "\n")


ftemps.close()