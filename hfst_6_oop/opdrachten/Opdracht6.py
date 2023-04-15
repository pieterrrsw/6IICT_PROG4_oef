import random

class Student:
    def __init__(self, naam, nummer):
        self.naam = naam
        self.studentennummer = nummer
        self.ingeschreven_cursussen = []

    def info(self):
        print(f"{self.naam}: {self.studentennummer}")
        for cursus in self.ingeschreven_cursussen:
            print(f"    {cursus}")

    def inschrijven(self, cursus):
        if cursus.naam in self.ingeschreven_cursussen:
            print(self.naam, "reeds ingeschreven voor", cursus.naam)
            return
        self.ingeschreven_cursussen.append(cursus.naam)

class Cursus:
    def __init__(self, naam, nummer):
        self.naam = naam
        self.cursusnummer = nummer

    def info(self):
        print(f"{self.naam}: {self.studentennummer}")
        

student_getallen = random.sample(range(1, 10000), 5)
cursus_getallen = random.sample(range(1, 10000), 5)

student_namen = ["Jan", "Piet", "Joris", "Korneel"]
cursus_namen = ["Wisk", "Prog", "Netw", "Frans"]

studenten = []
cursussen = []
for i in range(4):
    # Maak object van Student aan + voeg toe aan lijst studenten
    # Maak object van Cursus aan + voeg toe aan lijst studenten
    studenten.append(Student(student_namen[i], f"S{student_getallen[i]}"))
    cursussen.append(Student(cursus_namen[i], f"C{cursus_getallen[i]}"))

# Cursussen toevoegen
for i in range(4):
    studenten[i].inschrijven(cursussen[i])
studenten[1].inschrijven(cursussen[2])
studenten[3].inschrijven(cursussen[3]) # Korneel reeds ingeschreven voor Frans

# Info printen
for student in studenten:
    student.info()
for cursus in cursussen:
    cursus.info()