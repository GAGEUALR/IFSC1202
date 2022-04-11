class employee ():
    def __init__(self, firstname, lastname, IDnumber, hoursworked, wage):

        self.firstname = firstname
        self.lastname = lastname
        self.IDnumber = IDnumber
        self.hoursworked = hoursworked
        self.wage = wage

    def weeklypay(self):
        hoursworked = float(employee1.hoursworked)
        wage = float(employee1.wage)
        if hoursworked <= 40:
            totalpay = (hoursworked * wage)
            return totalpay
        if hoursworked > 40:
            overhours = (hoursworked - 40)
            totalpay = (overhours * wage * 1.5) + ((hoursworked - overhours) * wage)
            return totalpay

print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("First Name", "Last Name", "ID Number", "Hours Worked", "Wage", "Weekly Pay"))

payfile = open("10.06payroll.txt", "r")
x = payfile.readline()

for i in range(len(x)):
    while x != "":
        paysplit = x.split(",")
        totalpay = 0 
        employee1 = employee(paysplit[0], paysplit[1], paysplit[2], paysplit[3], paysplit[4])
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20.2f}".format(employee1.firstname, employee1.lastname, employee1.IDnumber, employee1.hoursworked, employee1.wage.replace("\n", ""), employee1.weeklypay()))
        x = payfile.readline()
