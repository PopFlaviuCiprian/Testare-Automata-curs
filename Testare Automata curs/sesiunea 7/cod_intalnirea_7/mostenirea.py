"""
Mostenirea: uneori avem clase care impartasesc atribute sau metode. In cazul acesta putem face o clasa parinte
si apoi clase copil, care sa mosteneasca parintele si implicit toate atributele si metodele sale

Mostenirea permite sa avem o ierarhie a claselor, cu oricate nivele dorim
Clasa copil poate avea in plus oricate atribute si metode doreste

In cazul metodelor, atunci cand avem in clasa copil o metoda cu exact aceeasi denumire ca una din
clasa parinte, se zice ca o suprascriem cu cea din clasa copil (se apeleaza defapt cea din clasa copil)

clasa parinte o putem apela in clasele copii cu super()
"""


class Person:

    def __init__(self, nume, varsta, adresa):
        self.nume = nume
        self.varsta = varsta
        self.adresa = adresa

    def descrie(self):
        print("-"*50)
        print(f"Nume: {self.nume}")
        print(f"Varsta: {self.varsta}")
        print(f"Adresa: {self.adresa}")

    def anul_nasterii(self):
        return 2022 - self.varsta

class Student(Person):

    def __init__(self, nume, varsta, adresa, facultate, an_studiu):
        # super() reprezinta clasa parinte, in cazul nostru Person
        # deci practic aici apelam constructorul clasei parinte
        super().__init__(nume, varsta, adresa)
        # putem apela metodele din clasa parinte si in felul urmator
        # nume_clasa.metoda(self,...)
        # Person.__init__(self, nume, varsta, adresa)
        self.facultate = facultate
        self.an_studiu = an_studiu

    def descrie(self):
        super().descrie()
        print(f"Facultatea: {self.facultate}")
        print(f"An studiu: {self.an_studiu}")

class Angajat(Person):

    def __init__(self, nume, varsta, adresa, companie, salariu):
        super().__init__(nume, varsta, adresa)
        self.companie = companie
        self.salariu = salariu

    def descrie(self):
        super().descrie()
        print(f"Companie: {self.companie}")
        print(f"Salariu: {self.salariu}")

    def salariu_anual(self):
        return self.salariu * 12

# clasa Profesor mosteneste clasa Anagajat, iar clasa Angajat la randul ei moesteneste clasa Person
# => clasa Profesor poate accessa proprietatile clasei Angajat cat si a clasei Person
class Profesor(Angajat):

    def __init__(self, nume, varsta, adresa, companie, salariu, curs, nr_ore):
        super().__init__(nume, varsta, adresa, companie, salariu)
        self.curs = curs
        self.nr_ore = nr_ore

    def descrie(self):
        super().descrie()
        print(f"Curs: {self.curs}")
        print(f"Nr ore: {self.nr_ore}")




andrei = Person("Andrei", 33, "Timisoara")
andrei.descrie()

maria = Student("Maria", 23, "Bucuresti", "Litere", 2)
maria.descrie()
print(maria.nume)

pavel = Angajat("Pavel", 39, "Oradea", "Emag", 67000)
pavel.descrie()
print(pavel.salariu_anual())
# print(andrei.salariu_anual())   # -> ca si parinte nu putem apela atributele/metodele claselor copil


matei = Profesor("Matei", 41, "Cluj", "Luxoft", 4500, "Introducere in Python", 120)
matei.descrie()
# metoda aceasta este mostenita din clasa parinte (Angajat)
print(matei.salariu_anual())

# metoda aceasta este mostenita din clasa parinte (Person)
print(andrei.anul_nasterii())
print(maria.anul_nasterii())
print(pavel.anul_nasterii())
print(matei.anul_nasterii())
