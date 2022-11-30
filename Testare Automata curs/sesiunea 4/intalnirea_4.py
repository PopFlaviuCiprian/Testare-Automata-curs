"""
Structuri repetitive  = blocuri de cod care se vor executa in mod repetitiv
                        pana cand o anumita conditie nu mai este repectata

Iteratie = procesul prin care un bloc de cod este executat in cadrul structurii repetitive
"""

# -----------------------------------------------------------------------------------------------------
######  WHILE/WHILE ELSE  ######

"""
while = “cat timp” =  ne permite executarea unui bloc de cod in mod repetat cat timp o conditie este satisfacuta (cat timp este adevarata)

- Contorul de control al structurii repetitive trebuie declarat in afara structurii repetitive si modificat in interiorul blocului de cod

- !!! Daca nu modificam valoarea contorului in interiorul blocului de cod, atunci vom intra intr-un ciclu infinit
"""

i = 0
while i <= 3:
    print(f"Valoarea lui i inainte sa fie incrementat este {i}")
    i += 1

print("done")


"""
While-ul de mai sus se itereaza asa:
i = 0 => i <= 3 ? DA => se executa codul dinauntru blocului while -> print(i)
i = 1 => i <= 3 ? DA => se executa codul dinauntru blocului while -> print(i)
i = 2 => i <= 3 ? DA => se executa codul dinauntru blocului while -> print(i)
i = 3 => i <= 3 ? DA => se executa codul dinauntru blocului while -> print(i)
i = 4 => i <= 3 ? NU => se iese din ciclu
print("done") 
"""

# Exemplu ciclu infinit
i = 0
while i <= 3:
    print(f"Valoarea lui i inainte sa fie incrementat este {i}")
    i -= 1

print("done")


# Exemplu cu break
i = 0
while i <= 3:
    print(f"Valoarea lui i inainte sa fie incrementat este {i}")
    i -= 1
    if i < -10:
        break

print("done")


"""
Folosim WHILE ELSE

WHILE = tipul structurii repetitive
i<=3: = conditia care se evalueaza
else = setul de instructiuni care se va executa dupa ce se iese din structura repetitiva
"""

i = 0
while i <= 3:
    print(f"Valoarea lui i inainte sa fie incrementat este {i}")
    i += 1
else:
    print(f"i nu mai este mai mic sau egal cu 3, este {i}")

print("done")


"""
Debugging = Depanare = procesul prin care gasim si rezolvam probleme in cod (bugs)
                     = punem pauza in cod ca sa vedem cum se parcurge codul pas cu pas
"""



# Parcurgerea listelor cu while
lista_fructe = ["mere", "pere", "banane", "kiwi", "struguri"]

i = 0
while i < len(lista_fructe):
    print(f"fructul este {lista_fructe[i]}")
    i += 1
print("am iesit din while")



"""
Exercitiu:
Type a one-letter command and hit enter:
A to add a name to your list
R to remove a name from your list
S to show the names in your list
Q to quit 
"""


names = []
ALLOWED_COMMANDS = ['a', 'r', 's', 'q']
continue_loop = True

while continue_loop:     # se va iesi din acest while doar cand continue_loop = False

    command = input("Introduceti comanda [A, R, S, Q]: ").lower()

    if command in ALLOWED_COMMANDS:
        if command == 'a':
            name = input("Introduceti un nume pentru a-l adauga: ")
            names.append(name)
        elif command == 'r':
            name = input("Introduceti numele pe care vreti sa il scoateti: ")
            names.remove(name)
        elif command == 's':
            print(f"Lista actuala este: {names}")
        else:   # acest else este pentru cand comanda data de la tastatura nu poate sa fie decat Q
            continue_loop = False     # variabila continue_loop ajunge sa fie FALSA si atunci se iese din while
    else:
        print(f"Introduceti o comanda valida, alegeti dintre [A, R, S, Q]")

print("Ati iesit din while")



# -----------------------------------------------------------------------------------------------------
######  FOR/FOR ELSE  ######

""""
range -> range este o functie care defineste un interval
      range(A, B, C)
      A = de unde incepem. daca nu punem atunci default e 0
      B = pana unde mergem. daca nu punem atunci va fi limita superioara -1
      C = pasul - optional
"""

for i in range(3, 9):
    print(i)

print("--------------")

for i in [3, 4, 5, 6, 7, 8]:
    print(i)

print("am iesit din for")



# am folosit sa iteram cu pas din 2 in 2
for i in range(3, 20, 2):
    print(i)


# 20 este punctul de finish, by default incepe de la 0
for i in range(20):
    print(i)



# --------------------------
# Calculeaza primele numere pare pana la 101

count = 0
for i in range(0, 102, 2):
    print(i)
    count += 1

print(count)



# ----- Inverseaza textul folosind for --------------------------

text = "ana are mere"
text_inversat = ""

for i in range(len(text) - 1, -1, -1):
    text_inversat += text[i]
else:
    print("s-a terminat range-ul")

for i in [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:   # la fel cu range(len(text) - 1, 0, -1)
    text_inversat += text[i]

for litera in [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:   # la fel cu range(len(text) - 1, -1, -1)
    text_inversat += text[litera]

print(f"Textul inversat este: {text_inversat}")




# putem sa iteram structuri de date si daca au tipuri de date diferite ca elemente
mai_multe_tipuri_de_date = [123, True, "text", {"RO": "bucharest"}, 24.67]

for elem in mai_multe_tipuri_de_date:
    print(elem)


"""
Exercitiu: 
Vrem sa parcurgem o lista de culori si sa verificam daca in lista exista valoarea "alb"
Daca exista, vrem sa o stergem din lista, si sa printam urmatorul text:
'Aceasta este o nonculoare, si va fi eliminata din lista'
"""


lista_culori = ["roz", "verde", "albastru", "rosu", "alb", "galben", "mov"]

for culoare in lista_culori:
    if culoare == "alb":
        lista_culori.remove("alb")
        print('Aceasta este o nonculoare, si va fi eliminata din lista')

print(f"Lista finala este {lista_culori}")


# #                 0       1         2         3       4        5       6            7
# lista_culori = ["roz", "verde", "albastru", "rosu", "alb", "galben", "mov"]   # elemnt pentru index 7 nu exista
#
# print(len(lista_culori))
#
# # range(7)   => merge de la 0 la 6
#
# # nu e ok daca iteram o lista folosind index si apoi stergem sau adaugam elemente intr-o lista
# # deoarece lungimea listei se modifica si vor aparea erori ca incearca sa identifice elementul accesandu-l cu un index care nu mai exista
# for i in range(len(lista_culori)):
#     print(f"Culoarea {lista_culori[i]} are index-ul {i}")
#     if lista_culori[i] == "alb":
#         lista_culori.pop(i)
#         print('Aceasta este o nonculoare, si va fi eliminata din lista')
#     print(f"Lista actuala: {lista_culori}")

# print(f"Lista finala este {lista_culori}")


"""
Exercitiu:

Avem o lista de note si vrem sa calculam media aritmetica a clasei

"""


# varianta cu iteratie cu foreach, trecand prin fiecare element
lista_note = [ 10, 5, 6, 7, 2, 4, 1]
suma = 0
for nota in lista_note:
    suma = suma + nota   # mai simplu suma += nota

print(suma)
print(f"Media este {suma/len(lista_note)}")


# varianta cu iteratie cu index
#              0   1  2  3  4  5  6
lista_note = [10, 5, 6, 7, 2, 4, 1]
suma = 0
for i in range(len(lista_note)):
    suma = suma + lista_note[i]

print(suma)
print(f"Media este {suma/len(lista_note)}")



"""
Exercitiu:

Am o lista de masini, si vreau sa ii prezint unui potential client masinile mele, pentru ca el sa poata alege ce ii place.
Criteriile lui sunt sa nu fie masini dacia sau peugeot
Noi vom scrie o instructiune care sa itereze prin toate masinile, si sa sara peste cele de mai sus
"""


lista_masini = ["BMW", "Chevrolet", "Trabant", "Dacia", "Audi", "Peugeot", "Mercedes", "Volkswagen"]

for masina in lista_masini:
    if masina == "Dacia" or masina == "Peugeot":
        continue
    print(f"Va recomandam masina: {masina}")




# Cum iteram cheie, valoare intr-un dictionar?

note_elevi = {
    "Andrei": 10,
    "Elena": 8,
    "Stefan": 9,
    "Maria": 5
}

print(note_elevi.items())
for elev, nota in note_elevi.items():
    print(f"{elev} a luat nota {nota}")





# cum putem sa iteram printr-un dictionar in dictionar in dictionar etc etc

dict1 = {
    "HR" : {
        "1":{
            "Andrei": 43545,
            "Matei": 43243,
            "florin": 3333
        },
        "2": {
            "Iulia": 3333,
            "Georgiana": 67888,
            "Luca": 9997,
            "Andrei": 11111
        }
    },
}

# print(dict1.items())

for cheia, valoarea in dict1.items():
    print(cheia)     # => "HR"
    print(valoarea.items())    #   => tot dict-ul valoare pentru HR
    for cheia_din_hr, valori_hr in valoarea.items():
        print(cheia_din_hr)                 # printeaza 1 si 2
        print(f"Valorile pentru {cheia_din_hr} sunt {valori_hr.values()}")       # valorile pentru cheile 1 si 2
        print(f"Perechile cheie valoare pentru {cheia_din_hr} sunt  {valori_hr.items()}")        # perechile de cheie-valoare din interiorul dict-urilor 1 si 2
        print(f"Tot dict-ul pentru {cheia_din_hr} este {valori_hr}")
        print(f"Accesam valoarea lui Andrei este {valori_hr['Andrei']}")
        print(f"Cheile din interiorul dict-ului {cheia_din_hr} sunt {valori_hr.keys()}")
        print("---------")
