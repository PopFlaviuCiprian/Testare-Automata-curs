# -----------------------------------------------------------------------------------------------------
######  LISTE  ######
# mai multe despre liste aici: https://www.w3schools.com/python/python_lists.asp

nume = "Michael"
len(nume)  #Va returna 7, pentru ca nume are 7 caractere
print(nume[0:2])  #Va acoperi primele doua caractere din string, pentru ca la slicing capatul superior de interval nu se ia in considerare

"""
1. Identificarea elementelor in liste si slicing pe liste
"""
# Definirea listelor = se face prin intermediul unui nume (care respecta aceleasi conventii ca la variabile)
                     # si prin plasarea elementelor care se doresc a fi adaugate in lista intre paranteze patrate, separate prin virgula

exemplu_lista = ["alb", "galben", "verde", "roz", "rosu"]
#                  0        1         2      3      4
print(len(exemplu_lista))

# Accesarea unui element dintr-o lista
print(exemplu_lista[2])
print(exemplu_lista[-1])
print(exemplu_lista[len(exemplu_lista) - 1])

print(exemplu_lista[0:2])
print(type(exemplu_lista[0:2]))     # cand folosim slicing pe o lista ne va returna tot o lista cu elementele selectate
print(type(exemplu_lista[2]))       # cand ii dam doar index-ul ne va returna exact element-ul respectiv

print(exemplu_lista[0:4:2])         # merge slicing si cu pas

# putem sa avem intr-o lista elemente cu diferite tipuri de date
diferite_date = [True, 4, 78.96, "test"]
print(diferite_date)

"""
2. Identificarea indexului la care se afla un element in lista
Cerinta: vreau sa printez pe ecran: "Vreau sa accesez masina Trabant si o voi gasi la indexul 0"
indexul se va extrage prin functie.
"""
masini = ["Limuzina", "BMW", "Volkswagen", "Opel", "Trabant", "Skoda", "Chevrolet", "Cadillac", "Trabant", "Skoda"]
print(masini[4])

# in cazul in care nu stiu la ce index se afla elementul pe care il caut, folosesc functia index pentru a afla
print(masini.index("Trabant"))       # gaseste primul element din lista si returneaza index-ul
                                     # daca exista mai multe elemente identice, ca returna doar index-ul primului gasit
# print(masini.index("Audi"))        # daca folosim functia index iar elementul cautat nu exista, returneaza eroare


print(masini.count("Trabant"))      # intoarce de cate ori apare valoarea cautata

# masini.clear()           # putem sa golim un list si va ramane []
# print(masini)


"""
3. Cum scoatem un element dintr-o lista? 
Raspuns: Ne putem folosi de functia remove sau pop
"""


print(f'Lista curenta este {masini}')
dif_remove = masini.remove("Opel")
print(f'Lista curenta este {masini}')
dif_pop = masini.pop(1)
print(f'Lista curenta este {masini}')

print(dif_remove)          # va printa None pentru ca functia remove al carei rezultat a fost salvat in variabila nu returneaza nimic
print(dif_pop)             # va prima elementul pe care l-a eliminat

masini.remove("Trabant")   # elimina primul element gasit
print(masini)

# masini.pop(2, 4)         # nu putem folosi pop cu mai mult de 1 singur argument >> va da eroare
# print(masini)


# Ce se intampla daca nu furnizam un index pentru functia pop() ?
print(masini.pop())
print(masini)


"""
4.  Cum suprascriem?

suprascrierea reprezinta inlocuirea unui element la o anumita pozitie cu un alt element
suprascrierea se poate face prin intermediul identificarii elementului pe baza de index si prin intermediul operatorului de atribuire
"""

masini[1] = "Ferarri"
print(masini)

# masini["Cadillac"] = "test"   >> nu putem sa accesam elemente pe baza valorii intre [], ci doar pe index

# daca nu stim index-ul la care se afla elementul, o gasim cu functia index()
masini[masini.index("Cadillac")] = "Dacia"
print(masini)


print("-------------------")
"""
5. Cum adaugam elemente intr-o lista folosind index-ul?

     1. Cerinta: Vrem sa inseram un nou element la inceputul listei 
     2. Cerinta: Vrem sa inseram un nou element in pozitia 3 a listei
"""

# prin functia insert ii spunem index-ul la care vrem sa adaugam elementul si elementul de adaugat
# restul elementelor din lista nu se sterg sau nu se suprascriu, doar isi decaleaza pozitia
masini.insert(0, "Hyundai")
print(masini)

masini.insert(3, "Citroen")
print(masini)


"""
6. Cum adaugam la final de lista?

     Cerinta: Vrem sa adaugam un nou element la finalul listei
"""

# prin functia append ii dam valoarea pe care vrem sa o introducem si o pune la final
masini.append("Fiat")
print(masini)

masini.insert(-1, "Pegeout")   # nu putem adauga la final cu -1 si insert pentru ca se adauga elementul inainte de index-ul -1
print(masini)

masini[-1] = "Ford"     # doar suprascrie ultimul element, nu adauga la final
print(masini)

print("------")

# masini[len(masini)] = "Volvo"   # nu functioneaza pentru ca da eroare de index out of range
# print(masini)

"""
7. Exercitiu:
Cum pot sa fac sa elimin din lista caracterul h si caracterul e?
Cum pot sa fac sa adaug litera i dupa elementele j si u?
"""

lista_exercitiu = ["m", 'h', 'e', 'Iana', "prajituri", 'floricele', 'j', 'u', True, 15]

lista_exercitiu.remove("h")
print(lista_exercitiu)
lista_exercitiu.pop(1)
print(lista_exercitiu)


lista_exercitiu.insert(6, "i")
print(lista_exercitiu)


"""
8. Putem pune o lista in alta lista?
Raspuns:  Da. Putem prin intermediul conceptului de matrice, sau lista bidimensionala (conceptul de matrice este putin impropriu spus)
"""

lista_in_lista = [
    # 0  1  2  -> index-urile listelor din interior
     [1, 2, 3],    # index 0
     [4, 5, 6],    # index 1
     [7, 8, 9],    # index 2
     [0]           # index 3
]

print(lista_in_lista[1])        # va printa [4, 5, 6]
print(lista_in_lista[1][2])     # va printa 6  (pentru ca ia elementul [4, 5, 6] de pe index-ul 1 si in interiorul lui cauta elementul cu index-ul 2)


"""
9. Putem sa unim 2 liste?
Raspuns:  Da. Prin intermediul functiei extend()
"""


lista_1 = ["alb", 1, True, "TEST"]
lista_2 = ["neguru", 6.78, False, "TEST"]


lista_1.extend(lista_2)
print(lista_1)

lista_1.extend(["albastru", 3.45])
print(lista_1)

print("-------")


print(masini)
masini.sort()   # implicit ascendent, putem sa sortam o lista, daca toate elementele sunt de acelasi tip de date
print(masini)
masini.sort(reverse=True)   # folosind reverse=True, sortam descendent
print(masini)



print("----------------------------------------")



# -----------------------------------------------------------------------------------------------------
######  SET-URI  ######
# mai multe despre set-uri aici: https://www.w3schools.com/python/python_sets.asp

"""
Setul reprezinta un set de date in care nu sunt permise valori duplicate, deci avem doar valori unice
Setul se reprezinta, spre deosebire de liste, intre doua acolade {}
Setul NU este o structura de date ordonata, deci nu va putea fi identificat prin index
"""


"""
1. Cum definim un set?
"""

culori_set = {"alb", "rosu", "verde"}
print(culori_set)
print(type(culori_set))

"""
2. Cum accesam elementele unui set? 
Raspuns: Nu se pot accesa deoarece seturile nu sunt structuri de date ordonate
"""
# print(culori_set[0])      # Imi va da eroare -  TypeError: 'set' object is not subscriptable
#                           #  Eroarea apare pentru ca seturile nu reprezinta o structura de date ordonata
#                           #  Asta inseamna ca elementele nu pot fi identificabile pe baza de index

# print(culori_set["alb"])


"""
3. Cum putem sa adaugam elemente intr-un set?
Raspuns: prin functia add()
 ATENTIE! La adaugarea unui duplicat NU NE DA EROARE
"""

culori_set.add("negru")
print(culori_set)

culori_set.add("alb")
print(culori_set)


"""
4. Cum putem sterge elemente dintr-un set?
Raspuns: prin functia remove() / discard() / sau pop() doar pentru ultimul element
"""

culori_set.remove("alb")
print(culori_set)

culori_set.discard("verde")
print(culori_set)

print("-----------")

# culori_set.remove("galben")    # daca incercam sa facem remove de un element care nu exista in set => eroare
# print(culori_set)

culori_set.discard("galben")          # daca incercam sa stergem un element care nu exista in set folosind discard() nu va da eroareprint(culori_set.discard("rosu"))
print(culori_set)

culori_set.pop()             # nu putem folosi index cu functia pop pentru un set
print(culori_set)



print("----------------------------------------")

# -----------------------------------------------------------------------------------------------------
######  TUPLE  ######
# mai multe detalii despre tuple aici: https://www.w3schools.com/python/python_tuples.asp
""""
tuplu 
     - este o structura de date ordonata (adica o structura de date in care pot sa accesez elementele pe baza de index)
     - are proprietatea de a fi imutabil (immutable), adica o data definit nu se mai poate schimba (adauga sau sterge valori)
     - permite duplicate

ex: un tuplu cu o echipa de campionat de sah pentru care au fost alesi trei elevi,
     si e posibil ca doi din ei sa aiba acelasi nume

Tuplurile se definesc prin intermediul parantezelor rotunde
"""

"""
1. Cum definim un tuplu?
"""

camere_hotel = (20, 21, 22, 23, 24, 25, 20, 20, 20)


"""
2. Cum accesam elementele unui tuplu? 
"""

print(camere_hotel[2])
print(camere_hotel[-1])


"""
3. Functii disponibile pentru tupluri: index, count
"""

print(camere_hotel.index(23))
print(camere_hotel.count(20))

print(len(camere_hotel))


# camere_hotel[2] = 454365         # >> nu functioneaza, va da eroare pentru ca un tuplu este imutabil
# print(camere_hotel)


test_tuplu = ("Iulia", 124, True, ["test", "test2"])   # si pentru un tuplu putem sa avem mai multe tipuri de date ca elemente
print(test_tuplu)
print(test_tuplu[-1])


print("----------------------------------------")

# -----------------------------------------------------------------------------------------------------
######  DICTIONARY  ######
# mai multe detalii despre dictionare aici: https://www.w3schools.com/python/python_dictionaries.asp

"""
dictionar - este o structura de date definita sub formatul cheie-valoare
In general cheile sunt definite in mod unic si nu se pot schimba sau duplica
Incercarea schimbarii numelui unei chei va duce de fapt la adaugarea unei noi perechi cheie-valoare
Se pot modifica in schimb valorile cheilor
Dictionarele se pot defini prin intermediul acoladelor
"""

# Mai jos am definit un dictionar in care am incercat sa mapam fiecare tara cu capitala proprie
capitale = {
     'Romania': 'Bucuresti',
     'Ungaria': 'Budapesta',
     'Italia': 'Roma',
     'Bulgaria': 'Sofia',
    # 'Romania': 'test'    >> nu se recomandat sa puneti mai multe chei cu aceeasi denumire intr-un dictionar
                    # DO NOT DO IT
}


orase = {
     "Romania": ["Bucuresti", "Timisoara", "Oradea"],
     "Japonia": True
}

"""
1. Cum putem sa accesam date?
Raspuns: DA, se pot accesa datele prin intermediul cheilor sau prin intermediul functiei get
"""

print(capitale["Romania"])
print(capitale.get("Romania"))


"""
2. Cum putem sa actualizam o informatie?
Raspuns: Da, se pot actualiza prin intermediul cheilor si al operatorului de atribuire
   sau prin intermediul functiei update
"""


capitale["Romania"] = "Sibiu"
print(capitale)


capitale.update({"Romania": "Constanta"})
print(capitale)


"""
3. putem sa adaugam o informatie?
Raspuns: Da, prin intermediul cheilor si al operatorului de atribuire
"""

capitale["Cehia"] = "Praga"
print(capitale)


"""
4. putem sa stergem o informatie?
Raspuns: Da, prin intermediul functiei pop
"""


elem_scos = capitale.pop("Italia")
print(elem_scos)
print(capitale)


# capitale.pop()   # pentru a folosi pop cu dictionare trebuie neaparat sa ii dam cheia, nu putem folosi pop simplu
# print(capitale)


"""
5. Putem sa concatentam doua dictionare? 
Raspuns: Da, prin intermediul functiei update
"""

capitale_2 = {
     "Elvetia": "Berna",
     "Franta": "Paris",
     "Romania": "Cluj"
}

capitale.update(capitale_2)  # da, deci daca folosim update putem sa unim 2 dictionare,
                             # iar daca exista chei din al doilea dictionar care sunt la fel ca in primul
                             # se ia valoarea din al doilea, ultimul
print(capitale)



"""
6. Putem sa afisam doar CHEILE unui dictionar? 
Raspuns: Da, prin intermediul functiei 'keys'
"""

print(capitale.keys())
print(type(capitale.keys()))


"""
7. Putem sa afisam doar VALORILE unui dictionar? 
Raspuns: Da, prin intermediul functiei 'values'
"""


print(capitale.values())


"""
8.Putem sa afisam perechile CHEIE-VALOARE ale unui dictionar?
 Raspuns: Da, prin intermediul functiei 'items'
 """


print(capitale.items())




"""
9. Putem sa avem dictionare in dictionare? 
Raspuns: Da, putem sa avem orice alte tipuri de date
"""

exemplu_dictionar = {
     "orase_capitale": {
          "Romania": "bucuresti",
          "italia": "roma"
     },
     "is_seen": True,
     "score": 3.455
}

print(exemplu_dictionar)
print(exemplu_dictionar["orase_capitale"]["Romania"])
