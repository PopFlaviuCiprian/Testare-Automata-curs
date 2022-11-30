<<<<<<< HEAD

'''
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’

'''

'''
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui

Actualizează proiectul pe github facand un push la noul cod
În Folderul de teme ajunge să pui doar linkul cu proiectul tău public
'''

from abc import ABC, abstractmethod
class FormaGeometrica(ABC):

    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):

    def __init__(self, valoare):
        self.__latura = valoare

    def aria(self):
        return self.__latura * self.__latura


    def latura(self):
        return self.__latura


    def get_latura(self):
        return self.latura


    def set_latura(self,valoare):
        self.__latura = valoare


    def delete_latura(self):
        self.__latura = None
        print(f'Deleter: Am sters latura')



class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        return (self.__raza)**2 * super().PI

    def raza_getter(self):
        return self.__raza

    def raza_setter(self, val_raza):
        self.__raza = val_raza

    def raza_deleter(self):
        self.__raza = None

    def descrie(self):
        super().descrie()
        print(f'Eu nu am colturi')

cercul = Cerc(5)
print(cercul.aria())
cercul.descrie()
cercul.raza_deleter()
print(cercul.raza_setter(7))

print(100 *'*')

patrat = Patrat(4)
print(patrat.aria())
patrat.descrie()
patrat.delete_latura()
=======

'''
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’

'''

'''
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui

Actualizează proiectul pe github facand un push la noul cod
În Folderul de teme ajunge să pui doar linkul cu proiectul tău public
'''

from abc import ABC, abstractmethod
class FormaGeometrica(ABC):

    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):

    def __init__(self, valoare):
        self.__latura = valoare

    def aria(self):
        return self.__latura * self.__latura


    def latura(self):
        return self.__latura


    def get_latura(self):
        return self.latura


    def set_latura(self,valoare):
        self.__latura = valoare


    def delete_latura(self):
        self.__latura = None
        print(f'Deleter: Am sters latura')



class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        return (self.__raza)**2 * super().PI

    def raza_getter(self):
        return self.__raza

    def raza_setter(self, val_raza):
        self.__raza = val_raza

    def raza_deleter(self):
        self.__raza = None

    def descrie(self):
        super().descrie()
        print(f'Eu nu am colturi')

cercul = Cerc(5)
print(cercul.aria())
cercul.descrie()
cercul.raza_deleter()
print(cercul.raza_setter(7))

print(100 *'*')

patrat = Patrat(4)
print(patrat.aria())
patrat.descrie()
patrat.delete_latura()
>>>>>>> d6d39c1a91c0ceabbd91d2c3c68cca9fbec669f2
patrat.get_latura()