"""

Abstractizarea este un proces prin care putem sa ascundem o anumita functionalitate specifica fata de utilizator
si de asemenea de a putea forta un anumit comportament in clasele copil
Utilizatorul stie ce face functionalitatea, dar nu si cum

Clasa parinte este o clasa abstracta, deci nu putem sa cream obiecte din ea, ci doar o sa o folosim ca un template
pentru clasele copii

In abstractizare exista doua concepte:
- Interfata - contine doar metode abstracte
- Clasa abstracta - contine atat metode abstracte cat si metode proprii, cu logica

Clasa abstracta trebuie sa mosteneasca clasa ABC (Abstract Class Method)
Fiecare metoda a clasei abstracte trebuie sa arunce exceptia NotImplementedError sau pass
Clasa abstracta NU are constructor pentru ca nu cream obiecte din ea

O metoda abstracta e o metoda care nu are corp (fara logica)
"""


"""
Polimorfism = poli (mai multe) morfis (forma/forme) => ceva care poate lua mai multe forme
In cazul nostru, in POO, o metoda podate sa aibe acelasi nume in clase diferite dar implemnetari/logica diferita in interior
EX: Metodele de mai jos nr_roti si nr_locuri din diferitele clase
"""

from abc import ABC, abstractmethod

# punem (ABC) pentru a-i zice lui Python ca este o clasa abstracta
class Vehicule(ABC):

    @abstractmethod                # am folosit un decorator sa marca aceasta metoda ca abstracta
    def nr_roti(self):
        raise NotImplementedError

    @abstractmethod
    def nr_locuri(self):
        pass                        # in general metodele abstracte nu trebuie sa aibe logica
                                    # si pentru a nu avea errori, avem doua optiuni:
                                    # scriem pass
                                    # raise NotImplementedErrror - ridicam exceptie

    @classmethod                    # am folosit un decorator ca sa marcam metoda ca fiind unca de clasa, cu logica proprie
    def metoda_logica_proprie(self):
        print(f"Aici este o metoda cu logica proprie, nu trebuie implementata obligatoriu si in clasele copil")


class Masina(Vehicule):

    def __init__(self, culoare):
        self.culoare = culoare

    def get_culoare(self):
        return self.culoare

    def nr_roti(self):
        return 4

    def nr_locuri(self):
        return 5


class Bicicleta(Vehicule):

    def __init__(self, culoare, roti_ajutatoare = False):
        self.culoare = culoare
        self.roti_ajutatoare = roti_ajutatoare

    def nr_roti(self):
        if self.roti_ajutatoare:
            return 4
        else:
            return 2

    def nr_locuri(self):
        return 1


# test_abstract_class = Vehicule()  # -> nu putem crea obiecte din clasele abstracte

masina_gri = Masina("gri")
print(masina_gri.get_culoare())
print(masina_gri.nr_roti())
print(masina_gri.nr_locuri())
masina_gri.metoda_logica_proprie()


bicicleta_rosie = Bicicleta("rosu")
print(bicicleta_rosie.nr_roti())
print(bicicleta_rosie.nr_locuri())

bicicleta_verde = Bicicleta("verde", True)
print(bicicleta_verde.nr_roti())
print(bicicleta_verde.nr_locuri())


lista_vehicule = [Bicicleta("rosu"), Bicicleta("verde", True), Masina("gri"), Masina("negru")]
for vehicul in lista_vehicule:
    print("-"*30)
    print(f"nr locuri: {vehicul.nr_locuri()}")
    print(f"nr roti: {vehicul.nr_roti()}")