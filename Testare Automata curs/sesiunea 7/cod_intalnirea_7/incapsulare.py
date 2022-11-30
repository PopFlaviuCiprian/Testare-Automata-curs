"""

Incapsulare = posibilitatea de a PROTEJA atributele/metodele unei clase, folosind modificatorii de vizibilitate

- private (privat, adica atributul/metoda poate fi accesat doar din interiorul clasei in care a fost definit)
        se defineste cu dublu underscore in fata (__example)
- protected (protejat, atributul/metoda poate fi accesata din clasa in care a fost definita,
            dar si in clasele copil ale acestia, INSA NU din exterior)
        se defineste cu un singur underscore (_exemplu)

Atunci cand avem un atribut ascuns putem folosi metode speciale pentru a interactiona cu el:
numite getter (pentru a-l vedea/accesa), setter (pentru a-i schimba valoarea), deleter (pentru a-i sterge valoarea)
In general aceste metode trebuie denumite cu set_, delete_ si get_ + numele variabilei
"""


class Car:

    # atribute de clasa
    __variabila_privata = "test1"
    _variabila_protected = "test2"

    def __init__(self, var_protected):
        # atribut de obiect
        self._variabila_protected = var_protected

    # getter
    def get_variabila_privata(self):
        return self.__variabila_privata

    # setter
    def set_variabila_privata(self, valoarea):
        self.__variabila_privata = valoarea

    # deleter
    def delete_variabila_privata(self):
        self.__variabila_privata = None




masina = Car("am_updatat")
print(masina._variabila_protected)    # nu ar fi trebuit totusi sa poti accessa dinafara, doar in clasele copi
                                      # de verificat ca este doar o regula nescrisa

# print(masina.__variabila_privata)   # -> eroare, pentru cele private nu putem sa le vedem


print(masina.get_variabila_privata())
masina.set_variabila_privata("Am updatat prin setter")
print(masina.get_variabila_privata())
masina.delete_variabila_privata()
print(masina.get_variabila_privata())



"--------------------------------------------------------------"
"""Folosim getter, setter si deleter intr-un mod Pythonic"""


class CarPy:

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.color

    @color.getter
    def color(self):
        print(f"Getter: Culoarea este {self.__color}")
        return self.__color

    @color.setter
    def color(self, color):
        print(f"Setter: Am updatat culoarea cu {color}")
        self.__color = color

    @color.deleter
    def color(self):
        print(f"Deleter: Am sters culoarea")
        self.__color = None


car_py = CarPy("negru")
car_py.color             # se apeleaza getter-ul
car_py.color = "verde"   # se apeleaza setter-ul
car_py.color
del car_py.color         # se apeleaza deleter-ul
car_py.color


