class student ():
    def __init__(self, firstname, lastname, tnumber, scores):

        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.scores = scores

    def RunAverage(self):
        runningav = (totalscore / scorecount)
        return (runningav)

    def SemesterAverage(self):
        semav = (totalscore / fscorecount)
        return semav

    def LetterGrade(self):
        semav = int(totalscore / fscorecount)
        letgrade = ""
        if semav >= 90:
            letgrade += "A"
        if semav >= 80 and semav < 90:
            letgrade += "B"
        if semav >= 70 and semav < 80:
            letgrade += "C"
        if semav >= 60 and semav < 70:
            letgrade += "D"
        if semav < 60:
            letgrade += "F"
        return letgrade

print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}\n{}".format("First Name", "Last Name", "ID Number", "Running Average", "Semester Average", "Letter Grade", "------" * 19))

Scorefile = open("10.04StudentScores.txt", "r")

for i in range(3):
    x = Scorefile.readline()
    xsplit = x.split(",")
    student1 = student(xsplit[0], xsplit[1], xsplit[2], [xsplit[3], xsplit[4], xsplit[-1]])
    numofzeros = 0
    totalscore = int(0)
    scorecount = 0
    for i in range(len(student1.scores)):
            if student1.scores[i] != "":
                student1.scores[i] == int(student1.scores[i])
                totalscore += int(student1.scores[i])
                scorecount += 1
    numofzero = (len(student1.scores) - scorecount) 
    fscorecount = (numofzero + scorecount)
    print("{:<20}{:<20}{:<20}{:<20.2f}{:<20.2f}{:<20}".format(student1.firstname, student1.lastname, student1.tnumber, student1.RunAverage(), student1.SemesterAverage(),student1.LetterGrade()))
