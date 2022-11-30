
# cum putem sa importam toate functiile dintr-un fisier
# from helper.utile import say_hi_name, say_hi_name_and_age
from helper.utile import *   # * inseamna ca importam tot

say_hi_name()
say_hi_name_and_age()


# 1. cum sa denumim variabile si functii (nu trebuie sa folosim denumiri rezervate)

# ne subliniaza cu rosu si nu ne lasa, va da eroare
# def = 5

# pentru denumirile de functii, cel mai bine este sa denumim o functie in
# asa fel incat sa se deduca din denumire ce face acea functie

# def is_even
# def calculate_sum

# nu e ok asa, pentru ca nu imi pot da seama ce face functia respectiva
# def void()

# recomandat ar fi si pentru variabile sa le denumim tot la fel, cat mai descriptiv
a = 0       # nu putem sa ne dam seama usor pentru ce este variabila
count = 0   # ne dam seama pentru ce este aceasta variabila


# 2. cum folosim *var intr-o functie si ce face
# Exercitiu: Vrem sa calculam suma mai multor numere date

# variabila globala
var_globala = 89
print(f"Variabila globala poate fi accesata in fisierul principal {var_globala}")
# de revenit la urmatorul curs sa vedem de ce da eroare aici
suma = 0

def calculeaza_suma(*numere):
    print(f"Variabila globala poate fi accesata si in functie {var_globala}")
    print(numere)   # le pune pe toate intr-un tuple
    for numar in numere:
        suma = suma + numar
    # in momentul in care returnam mai multe valori, ele defapt sunt returnate intr-un tuple
    return suma, 8, 9

x = calculeaza_suma(5)
print(x)
print(calculeaza_suma(5))
print(calculeaza_suma(5, 10, 15))

# 3. variabilele care sunt definite intr-o functie nu pot fi accesate inafara ei

#print(suma)

# 4. variabilele care sunt definite in fisierul principal, inafara functiilor
# sunt variabile globale
