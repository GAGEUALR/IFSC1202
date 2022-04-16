class Employee ():
    def __init__ (self, firstname = "", lastname = "", IDnumber = "", hoursworked = 0, wage = ""):

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

def find_employee(employeelist, employeetofind):
	for i in range(len(employeelist)):
		if employeelist[i].firstname == employeetofind:
			return i
            

def print_employeelist(employeelist):
	print("{:<30}{:<30}{:<30}{:<30}".format("First Name", "Last Name", "ID Number", "Hours Worked"))
	for i in range(len(employeelist)):
		print ("{:<30}{:<30}{:<30.2f}{:<30.2f}{:<30.2f}".format(employeelist[i].firstname, employeelist[i].lastname, employeelist[i].IDnumber, employeelist[i].wage, weeklypay()))

employeelist = []

employeefile = open("11.02Employees.txt", "r")
x = employeefile.readline()

while x != "":
    xsplit = x.split(",")
    employee1 = Employee(xsplit[0], (xsplit[1]), (xsplit[2]), xsplit[3])
    employeelist.append(employee1)
    x = employeefile.readline()


print_employeelist(employeelist)
    