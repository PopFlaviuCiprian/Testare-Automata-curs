from helper.utile import say_hi_name, say_hi_name_and_age

"""
O functie este o modalitate prin care putem sa economisim cod.
O functie putem sa o definim o singura data si apoi sa facem ceea ce se numeste apelare a functiei

Apelarea functiei inseamna trimiterea sistemului catre adresa de memorie care poarta
    numele functiei si la care este stocat codul pe care vrem sa il executam

Definirea unei functii se poate face pe baza keyword-ului def

O functie POATE sa aiba parametri, dar nu este obligatoriu sa aiba
Chiar daca functia NU are parametri, parantezele de dupa numele functiei sunt
    obligatorii atat la definire cat si la apelare

Un parametru reprezinta o informatie de care functia are nevoie din exterior
    pentru a putea executa toate instructiunile
Putem alege sa parametrizam o functie atunci cand vrem ca functia noastra
    sa poata sa fie rulata pentru o plaja mai mare de valori
    ex: suma intre doua numere, putem avea alte doua numere la fiecare rulare

O functie POATE sa aiba optiune de return, dar nu este obligatoriu sa aiba
Vom alege sa punem optiune de return pe functie atunci cand vrem sa salvam rezultatul
    acelei functii intr-o variabila sau sa trimitem acel rezultat catre un sistem extern
"""

# definirea functiei (exemplu fara parametrii si fara return)
def say_hi():
    print("Hi!")


# apelarea functiei - va executa codul din interior-ul functiei
say_hi()
say_hi()
say_hi   # -> daca nu punem parantezele nu se va executa corpul functiei, pentru ca nu este vazuta ca o functie

# !!! Daca o functie nu este apelata, codul din interiorul ei nu va fi executat
# de aceea se spune ca functiile ruleaza independent, sunt niste programe in miniatura


"""
def - keyword ul care anunta inceputul definirii unei functii
say_hi - numele functiei, care este dat de catre user si care poate sa fie orice  (free text)
            in general, numele functiei trebuie sa fie sugestiv pentru actiunea pe care o face
() - reprezentant al zonei in care PUTEM sa specificam parametri. In cazul functiei say_hi
            nu avem parametri, motiv pentru care parantezele sunt goale
: - reprezentant al inceputului corpului functiei, adica locul in care vom incepe sa descriem
            actiunea pe care trebuie sa o faca functia
Corpul unei functii va fi definit la fel ca la structurile alternative (if) si repetitive  (while, for)
            prin intermediul indentarii (adica spatiul lasat liber de la marginea fisierul python
            pana la inceputul liniei de cod)     
"""

print("----------")
x = say_hi()           # aici se va executa functia say_hi (adica se printeaza Hi) chiar daca se va "salva" in variabila x
                       # defapt pentru ca functia nu are return, x va lua valoarea None
print(f"x este {x}")
print(f"x este {say_hi()}")


print("----------------------------")


# say_hi_name()   # daca functia a fost definita cu parametru (si nu are o valoare default) iar noi o apelam fara
                  # atunci va da eroare

# functiile apelate aici sunt definite intr-un alt fisier
# vezi importul de la inceputul acestui fisier
say_hi_name("Iulia")
say_hi_name("Andrei")
say_hi_name_and_age("Mario", 33)

# putem sa apelam functia si doar cu un singur parametru, vezi cum a fost definita in helper > utile
say_hi_name_and_age("Aurel")
say_hi_name_and_age([56, "test"])

"""
definim functia = parametrii
apelam functia = argumente
"""


print("----------------")
lista_nume = ["Iulia", "Andrei", "Ion", " Anastasia", "Gabriel", "Matei"]
for nume in lista_nume:
    say_hi_name(nume)




print("---------------")
# am definit functia
# def is_even():
#     number = int(input("introduceti nr: "))
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# # apelez functia
# x = is_even()
# print(x)



print("---------")
# Exercitiu: Vrem sa calculam suma tututor numerelor pare dintr-un anumit interval

def suma_numere_pare(limita_superioara):
    suma = 0
    for numar in range(limita_superioara + 1):
        if numar % 2 == 0:
            suma += numar

    return suma


s = suma_numere_pare(10)
print(s)


"""
Exercitiu:
Scrieti o functie care primeste ca parametru un string si calculeaza numarul de litere mari si litere mici din el si printeaza asta
"""

print("-------------------------")
def calculator_de_litere(text):
    count = {
        "upper_case": 0,
        "lower_case": 0
    }
    for litera in text:
        if litera.isupper():
            count["upper_case"] += 1
        elif litera.islower():
            count["lower_case"] += 1

    print(f"Textul a fost: {text}")
    print(f"Numarul de litere mici este {count['lower_case']}")
    print(f"Numarul de litere mari este {count['upper_case']}")


txt_tastatura = input("Introduceti un text: ")
calculator_de_litere(txt_tastatura)

