print("Hello world")

# -----------------------------------------------------------------------------------------------------
######  COMENTARII  ######

# Comentarii = linii din codul sursa care nu sunt executate, ele sunt menite pentru diverse adnotari/explicatii
# O singura linia poate fi comentata in Python cu simbolul #
# Pentru comentarii multi-line se folosesc trie ghilimele succesive """ sau ''' le inceputul si respectiv la sfarsitul zonei de comentat

# x = 2     // comentam codul folosind #

"""        // comentam codul folosind 3 ghilimele duble succesive 
y = 3
z = 5
"""

'''       // comentam codul folosind 3 ghilimele simple succesive 
y = 3
z = 5
print("Hello world2")
'''



# -----------------------------------------------------------------------------------------------------
######  VARIABILE  ######

# 1. O variabila este un spatiu rezervat in memoria sistemului care poate stoca informatii, iar acestea pot fi modificate in timp
# 2. O variabila trebuie sa fie definita de un nume
# 3. Variabila este creata doar dupa ce i se asigneaza si o valoare care este stocata in memoria rezervata
# 4. Reguli de denumire a unei variabile:
#     - nu pot sa contina spatii
#     - nu pot sa fie denumite cu denumiri rezervate (de exemplu nu putem denumi o variabila print)
#     - trebuie sa fie unice
#     - nu pot incepe cu un numar (pot sa contina numere atata timp cat nu incep cu un numar)
#     - denumirea unei variabile este case sensitive (adica o variabila numita camelCase nu este aceeasi cu camelcase)
# 5. Convenții de denumire generale in python:
#      - Pentru nume de clase: pascalCase
#      - Pentru nume de variabile / metode: snake_case
#      - Pentru constante: NUME_CONSTANTA

# Constantele sunt spatii de memorie care nu ar trebui sa isi schimbe valoarea.
# In Python exista doar conceptul de constanta, care de obicei se noteaza cu litere mari si nu ar trebui modificata in cod, dar in realitatea ea se poate modifica


# Declararea si initializarea unei variabile
model_masina = "v60"
model_Masina = "v10"
print(model_masina)
print(model_Masina)

# exemplu constante in python >> este ceva conceptual, se modifica valoarea. Dar daca folosim o constanta in cod ar trebui sa nu o modificam
NUME_MASINA = "Dacia"
print(NUME_MASINA)
NUME_MASINA = "Golf"
print(NUME_MASINA)

# Modificarea tipului de date al unei variabile
model_masina = 330
print(model_masina)

x, y, z = "Banana", "Mar", "Portocala"
print(y, z)
x = y = z = "Struguri"
print(x, y, z)


# -----------------------------------------------------------------------------------------------------
######  TIPURI DE DATE (DATA TYPES)  ######

# Un tip de date este o informatie care ii spune sistemului ce tip de informatie putem stoca intr-o variabila

# Cele mai folosite tipuri de date in Python:
# - int (short for integer) -> Poate stoca doar valori intregi (1,2,9,99,167834534 etc)
# - float -> Poate stoca valori cu zecimale (16 decimal points)
# - bool (short for boolean) -> Poate stoca True sau False
# - string -> Poate stoca text


a = 3         # de tip int
b = 5.5       # de tip float
c = False     # de tip boolean
d = "masina"  # de tip string




# -----------------------------------------------------------------------------------------------------
######  FUNCTIA PRINT  ######

# print () = este o functie python care ne ajuta sa afiseze ce ii dam pe ecran (in consola)

print("Hello World")  # aici i-am dat functiei print sa ne afiseze string-ul "Hello World", notat intre ""
                      # Asa recunoaste python ca avem un text daca il scriem intre "" sau intre ''


# -----------------------------------------------------------------------------------------------------
######  STRING-URI  ######

print("Mc Donald's")
print('Mc Donald"s')
# SAU putem folosi escape mechanism
# Caracterul "escape" =  este backslashul \ care folosit intr-un string va face escape la caraterul ilegal
print('Mc Donald\'s')

# String-urile pot fi concatenate folosind simbolul + si adaugata valoarea intr-o alta variabila
nume = "Popescu"
prenume = "Elena"
prezentare = "Numele meu este " + nume + " " + prenume
print(prezentare)

# formated string literals
prezentare_2 = f"Numele meu este {nume} {prenume}"
print(prezentare_2)

varsta = 30
prezentare_3 = f"Numele meu este {nume} {prenume} si am varsta de {varsta}"
print(prezentare_3)


#
produs = "Geaca"   # string
pret = 300         # int

# print("Produsul cu numele " + produs + " are pretul de " + pret + " lei")  # - va retuna o eroare pentru ca nu putem concatena string-uri cu int-uri
print("Produsul cu numele " + produs + " are pretul de " + str(pret) + " lei")    # aceasta varianta va merge
print(f"Produsul cu numele {produs} are pretul de {pret} lei")                    # aceasta este cea mai recomandata optiune pentru a fi folosita
                                                    #f forteaza variabilele gasite intre {} sa fie tratate ca si string-uri
                                                    #f is short for - format string
# plus pentru int-uri si float-uri aduna
a = 5
b = 6.7
print(a + b)



# -----------------------------------------------------------------------------------------------------
######  TYPE si TYPE CASTING  ######

# type casting inseamna modificarea tipului de date a unei valori

example = 33
print(example)
print(type(example))   # functia type ne returneaza tipul de date curent al variabilei

example = "text0"
print(type(example))

example = True
print(type(example))


example = "33"
print(example)
print(int(example))
print(type(example))
print(type(int(example)))
print(float(example))
print(type(float(example)))
print(str(float(example)))
print(type(str(float(example))))

number_1 = 1.999
print(f"Noua valoare este {int(number_1)}")


# -----------------------------------------------------------------------------------------------------
######  FUNCTIA INPUT  ######

# input() =
# - ne ajuta sa extragem valori date de la tastatura
# - valorile luate de la tastatura au by default tipul de date string
# - putem salava valorile de la tastatura in variabile pentru a le folosi ulterior


# a = 3
# b = int(input("Alege un numar: "))
# print(type(b))

print(a + b)

# name, age, gender = input("Enter the name|age|gender: ").split("|")  # in acest caz cand inseram trebuie sa introducem | intre cuvinte
# print(name, age , gender)


# name, age, gender = input("Enter the name age gender: ").split()  # in acest caz separatorul este automat spatiu
# print(name, age , gender)



# -----------------------------------------------------------------------------------------------------
######  ASSERT  ######

a = 1
# il intreb pe python: hey, a este egal cu 1?
# assert a == 1
# print('trec pe aici')
# assert a == 2
# print('nu mai trec pe aici')

#
# user_pass = input("Introduce parola: ")
# parola_existenta = "pass1234"
# assert parola_existenta == user_pass
# print("Autentificare reusita")




# -----------------------------------------------------------------------------------------------------
######  String (index, len(), slicing, metode)  ######


###### a) despre index, slicing
# - fiecare caracter intr-un string are un index care ii identifica pozitia
# - pozitia primului caracter este 0, adica primul index
# - putem sa taiem (slice) un string folosind urmatoarea sintaxta: my_str[start_pos:end_pos:step]
#  https://stackoverflow.com/questions/509211/understanding-slice-notation/46614773 -> More info about slice notation
# https://stackoverflow.com/questions/509211/understanding-slicing


string_ex = "adevar"
print(string_ex[2])
print(string_ex[4])
print(string_ex[-1])
print(string_ex[-5])

# stringul:         a   d   e   v   a   r
# index:            0   1   2   3   4   5
# index negativ:   -6  -5  -4  -3  -2  -1

# Exemple slicing
print("-------------------------------------------------")


sentence = "Mybname is python and i am a snake"
print(sentence[0])               # primul caracter
print(sentence[0:3])             # afiseaza caracterele din pozitia 0, 1, 2
print(sentence[:])               # cat timp nu e specificat pozitia de inceput si de finish se ia tot string-ul
print(sentence[:6])              # Mybnam >> se afiseaza de la inceput (0) pana la pozitia 5 (fara a se include index-ul 6)
print(sentence[6:])              # se afiseaza de la pozitia 6 pan ala sfarsit
print(sentence[::-1])            # trece prin string in sens invers
print(sentence[0:10:2])          # ia caracterele de la inceput pana la sfarsit cu un pas de 2, trece peste orice alte caratere
print(sentence[-5:])             # se iau ultimele 5 caractere
print(sentence[-5::-1])          # a eliminat ultimele 4 caractere si a scris restul string-ului in sens invers
print(sentence[::3])             # se ia fiecare carater din 3 in 3

part1 = sentence[1:8]
print(part1)


###### b) despre len(), alte metode
# - len(x) = ne returneaza numarul de caractere/elemente gasite pentru x
# - x.count(y) = aduna de cate ori se regaseste y intr-un string dat x si returneaza valoarea
# - upper() = converteste toate caraterele in litere mari
# - x.replace(y, z) = va inlocui unde gaseste pe y cu z in string-ul dat x



sentence_2 = "aAzi e cursaai gfd iii"
print(len(sentence_2))
print(sentence_2.count("a"))
print(sentence_2.upper())
print(sentence_2.replace("i", "y"))
print(sentence_2.replace("i", "y", 2))
print(sentence_2.capitalize())
