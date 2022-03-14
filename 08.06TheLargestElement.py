x = input("Enter Values Seperated by Spaces: ")

b = x.split(" ")
index = 0
count = 0
greaterthan = str(0)
for i in range(len(b[:-1:])):
    if b[i] > b[i + 1]:
        count = (b[i])
    if count > greaterthan:
        greaterthan = count
    if b[i] > count:
        count = b[i]
    if b[i] < b[i + 1]:
        count = b[i + 1]
    if count > greaterthan:
        greaterthan = count
    if greaterthan > count and greaterthan > b[i] and greaterthan > b[i + 1]:
        index = b[i] 
        

print("The greatest number is {}, The index is {}".format(greaterthan, index))


