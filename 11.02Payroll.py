class Employee ():
    def __init__ (self, firstname = "", lastname = "", IDnumber = "", hoursworked = 0, wage = ""):

        self.firstname = firstname
        self.lastname = lastname
        self.IDnumber = IDnumber
        self.hoursworked = hoursworked
        self.wage = wage
        
    def weeklypay(self):
        hoursworked = float(self.hoursworked)
        wage = float(self.wage)
        if hoursworked <= 40:
           totalpay = (hoursworked * wage)
           return totalpay
        if hoursworked > 40:
            overhours = (hoursworked - 40)
            totalpay = (overhours * wage * 1.5) + ((hoursworked - overhours) * wage)
            return float(totalpay)

    def changehours(self, newhoursworked):
        self.hoursworked = float(0)
        self.hoursworked = newhoursworked
        return self.hoursworked

def find_employee(employeelist, employeetofind):
	for i in range(len(employeelist)):
		if employeelist[i].IDnumber == ysplit[0]:
			return i
            

def print_employeelist(employeelist):
	print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("First Name", "Last Name", "ID Number", "Hours Worked", "Hourly Wage", "Weekly Pay"))
	for i in range(len(employeelist)):
	    print ("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20.2f}".format(employeelist[i].firstname, employeelist[i].lastname, employeelist[i].IDnumber, employeelist[i].hoursworked.replace("\n", ""), employeelist[i].wage.replace("\n", ""), employeelist[i].weeklypay()))

employeelist = []

employeefile = open("11.02Employees.txt", "r")
x = employeefile.readline()
hoursupdate = open("11.02Hours.txt", "r")
y = hoursupdate.readline()

while x != "":
    xsplit = x.split(",")
    employee1 = Employee(xsplit[0], (xsplit[1]), (xsplit[2]), float(0), xsplit[3])
    employeelist.append(employee1)
    x = employeefile.readline()

while y != "":
    ysplit = y.split(",")
    newhoursworked = ysplit[1]
    employeelist[find_employee(employeelist, ysplit[0])].changehours(newhoursworked)
    y = hoursupdate.readline()


print_employeelist(employeelist)

employeefile.close()
hoursupdate.close()