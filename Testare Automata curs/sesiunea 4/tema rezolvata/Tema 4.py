# EX 1 : Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# a)	Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# b)	Faceti acelasi lucru cu un for each
# c)	Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# cazul cu for
for i in range(len(masini)):
    print(f'FOR: Masina mea preferata este: {masini[i]}')

# cazul cu for each
for masina in masini:
    print(f'FOR EAACH: Masina mea preferata este: {masina}')

# cazul cu while
i = 0
while i < len(masini):
    print(f'WHIE: Masina mea preferata este: {masini[i]}')
    i = i + 1

# EX 2: Aceeasi lista
# Folositi un for else
# In for: Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# Pe else: Printati varianta finala a listei

for i in range(1, len(masini)-1):       # ne deplasam de la a doua poz pana la penultima
    masini[i] = masini[i].upper()
else:
    print(masini)

# EX 3: Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Itereaza prin ea prin modalitatea aleasă de tine
# Daca masina e mercedes:
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print(f'Am gasit masina dorita de dvs {masina}')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')

# EX 4: Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza (nu trebuie else)
# Printati "S-ar putea sa va placa masina x"

for masina in masini:
    if masina == "Trabant" or masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

# EX 5: Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# -	Salvati aceste masini in masini_vechi
# -	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x si Modele noi: x

masini_vechi = []

for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi.append(masina)
        index = masini.index(masina)
        masini[index] = 'Tesla'
print('Modele vechi:', masini_vechi)
print('Modele noi:', masini)

# EX 6: Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati "Pentru un buget de sub 15000 euro puteti alege masina x"
# Iterati prin lista

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
BUGET = 15000
for masina, pret in pret_masini.items():
    if pret <= BUGET:
        print(f'Pentru un buget de pana in {BUGET} euro puteti alege masina: {masina}')

# EX 7: Avand lista
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

total = 0
for numar in numere:
    if numar == 3:
        total = total + 1
print(f'Numarul 3 apare de {total} ori in lista de numere')

# EX 8: Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma = suma + numar
print(f'Suma numerelor din lista este: {suma}')

# EX 9: Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#numere = [-3, -2, -1] # de test, din aceasta cauza max nu poate fi 0, ci trebuie sa fie un elem din lista
max = numere[0]
for numar in numere:
    if numar > max:
        max = numar
print(f'Cel mai mare numar din lista este: {max}')

# EX 10: Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_neg = []
for numar in numere:
    if numar > 0:
        numar = numar - numar*2
        #numar = -(abs(numar)) # alta solutie
    lista_neg.append(numar)
print(f'Lista a devenit: {lista_neg}')

# EX 11: alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista cu numere pare este: {numere_pare}')
print(f'Lista cu numere impare este: {numere_impare}')
print(f'Lista cu numere pozitive este: {numere_pozitive}')
print(f'Lista cu numere negative este: {numere_negative}')

# EX 12: Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
print(alte_numere)

# EX 13: Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# -	Nr secret e mai mare
# -	Nr secret e mai mic
# -	Felicitari! Ai ghicit!

import random

numar_secret = random.randint(1, 30)
numar_ghicit = None
while numar_ghicit is None:
    nr = int(input('Introdu un numar: '))
    if nr > numar_secret:
        print('Numarul secret este mai mic')
    elif nr < numar_secret:
        print('Numarul secret este mai mare')
    else:
        print('Felicitari, ai gasit numarul!')
        break


# EX 14: Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333

nr = int(input("Scrie un numar: "))
i = 1
while i <= nr:
    print(' ')
    for j in range(i):
        j = i
        print(j, end='')
        j = j + 1
    i = i + 1


# EX 15: tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}')

# sau cu for each
for row in tastatura_telefon:
    for column in row:
        print(f'FOR EACH: Cifra curenta este {column}')
