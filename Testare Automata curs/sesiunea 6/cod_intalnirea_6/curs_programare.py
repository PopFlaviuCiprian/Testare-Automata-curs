
from persoana import Person

"""
clasa CursProgramare
atribute: companie, nume, durata, nr_locuri_max, studenti
metode: inscriere_student, descriere_curs, get_locuri_disponibile,
"""

class CursProgramare:

    def __init__(self, compania, nume, durata, nr_locuri_max):
        self.compania = compania
        self.nume_curs = nume
        self.durata = durata
        self.nr_locuri_max = nr_locuri_max
        self.studenti = []

    def descriere_curs(self):
        print(f"{self.compania} - {self.nume_curs} - {self.durata} zile")
        print("-"*30)
        if len(self.studenti) > 0:
            for student in self.studenti:
                print(f" {student.name}  {student.first_name}")
        else:
            print(f"Nu sunt studenti inscrisi")

    def inscriere_student(self, student):
        if self.get_locuri_disponibile() != 0:
            self.studenti.append(student)
        else:
            print(f"Nu mai sunt locuri disponibile pentru inscriere")

    def get_locuri_disponibile(self):
        return self.nr_locuri_max - len(self.studenti)



curs_python = CursProgramare("IT Factory", "Introducere in Python", 120, 5)
curs_python.descriere_curs()

viorel = Person("Matei", "Viorel", 34)
viorel.prezentare()

print("*"*30)
curs_python.inscriere_student(viorel)
curs_python.descriere_curs()
print(curs_python.studenti)
print(curs_python.studenti[0].name)
print(curs_python.studenti[0].first_name)


gabriela = Person("Andreescu", "Gabriela", 22)
stefan = Person("Ionescu", "Stefan", 33)
curs_python.inscriere_student(gabriela)
curs_python.inscriere_student(stefan)
curs_python.descriere_curs()

print(curs_python.get_locuri_disponibile())

test_gabriela = Person("Test1", "Gabriela", 22)
test_stefan = Person("Test2", "Stefan", 33)
curs_python.inscriere_student(test_gabriela)
curs_python.inscriere_student(test_stefan)

print(curs_python.get_locuri_disponibile())

curs_python.descriere_curs()

cezar = Person("Antonie", "Cezar", 36)
curs_python.inscriere_student(cezar)

curs_python.nr_locuri_max = 10
print(curs_python.nr_locuri_max)

