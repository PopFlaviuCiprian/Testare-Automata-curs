# -----------------------------------------------------------------------------------------------------
######  ASSIGNMENT OPERATORS  ######



"""

Atribuire/Asignare = proces prin care salvam informatii la adresa de memorie identificata cu un nume al variabilei

Operatorii de atribuire sunt: =, +=, -=, *=, /=

"""


x = 3    # valoarea initiala: 3
print(x)

x = x + 3   # valoarea curenta: 6
print(x)

x += 3    # am facut acelasi lucru ca si x = x + 3, valoarea curenta: 9
print(x)


x = x - 3   # valoarea curenta: 6
print(x)

x -= 3    # am facut acelasi lucru ca si x = x - 3, valoarea curenta: 3
print(x)


x = x * 3  # valoarea curenta: 9
print(x)

x *= 3    # am facut acelasi lucru ca si x = x * 3, valoarea curenta: 27
print(x)


x = x / 3   # valoarea curenta: 9, dupa impartire valoarea va fi un float
print(x)

x /= 3
print(x)   # valoarea curenta: 9



# -----------------------------------------------------------------------------------------------------
######  ARITHMETICAL OPERATORS  ######

"""
Operatorii aritmetici sunt operatori care permit operatii matematice

Acestia sunt: +, -, *, /, % (operatorul modulo), ** (operatorul putere), // (floor division)
"""

print( 5 % 3 )   # ne returneaza restul impartirii. de cate ori incape 3 in 5? R: 1, restul impartirii = 5 - 3 = 2
print( 4 % 2 )   # rezultatul returnat va fi 0 > ne putem da seama ca este un numar par
print( 5 % 2 )  # rezultatul returnat va fi 1 > ne putem da seama ca este un numar impar


# print( x ** y)  # va ridica pe x la puterea y
print( 5 ** 4 )
print( (5 + 2) ** 2 )
print( 5 + 10 - 2 / 7 ** 2  )
print((5 + 10) - (2 / 7) ** 2  )

print( 7 / 2.5 )
print( 7 // 2.5 )  # operatorul floor division rotunjeste rezultatul la cel mai apropriat numar intreg inferior



# -----------------------------------------------------------------------------------------------------
######  COMPARISON OPERATORS  ######

"""
Operatori prin intermediul carora putem compara doua valori (vor fi uili in cadrul assert-urilor)
Compararea lor va retuna o valoare de tip boolean (True sau False)

Operatorii sunt: ==, !=, >, < , >=, <=
"""


x = 3
y = 2
print( x == y )  # atentie, sa nu confundati operatorul de atribuire (=) cu operatorul de comparatie (==)

print(x != y )  # se verifica daca valoarea variabilei din stanga este diferita de valoarea variabilei din dreapta
                # daca sunt diferite, se va returna True
                # daca sunt egale, se va returna False


print( x > y )  # se evalueaza daca valoarea variabilei din stanga este mai mare decat valoarea variabilei din dreapta

print( x < y )  # se evalueaza daca valoarea variabilei din stanga este mai mica decat valoarea variabilei din dreapta


print( x >= y )  # se evalueaza daca valoarea variabilei din stanga este mai mare sau egal cu valoarea variabilei din dreapta
print( x <= y )  # se evalueaza daca valoarea variabilei din stanga este mai mica sau egal cu valoarea variabilei din dreapta


x = 5
y = 5

print( x >= y )
print( x <= y )

# -----------------------------------------------------------------------------------------------------
######  LOGICAL OPERATORS  ######

"""
Operatorii logici sunt operatori folositi pentru a defini evaluari ceva mai complexe

Ei sunt: and, or not


Ordinea prioritatii: NOT > AND > OR

"""

x = 5
y = 10

#       F    and   T  =>  F
print( x < 2 and x < y )
#       F    or   T   =>  T
print( x < 2 or x < y )
#      not    F    => T
print( not x == y )


#       F     and    F    or   T    =>
#              F          or   T    =>  T
print( x >= y and x == 20 or y < 30 )


#        F    and   F     and   T    =>  F
print( x >= y and x == 20 and y < 30 )

#        F    or   F     or   T      => T
print( x >= y or x == 20 or y < 30 )

#      not( F     or     F  ) and   T
#      not F                   and   T
#      T                       and   T   => T
print( not(x >= y or x == 20) and y < 30 )

#      F     or  not(  T    and    F )
#      F     or  not(  F          )
#      F     or  T                    => T
print( x < 2 or not( x < y and x == y ))


# NOT > AND > OR

a = 10
b = 20
c = 30

#       F    or  F   and    T   => F
print( a > b or b > c and c == 30 )   # inseamna  a > b or ( b > c and c == 30 )

#       F    and   F   or  F     and    T
#             F        or         F      => F
print( a > b and b > c or a == 15 and c == 30 )   # inseamna (a > b and b > c) or (a == 15 and c == 30)

#     not   F    and   F    or    T
#       T       and    F    or     T
#                F          or     T     => T
print( not a > b and a == 15 or c == 30 )  # inseamna ((not a > b) and a == 15) or c == 30


# -----------------------------------------------------------------------------------------------------
######  FLOW CONTROL  ######




# if simplu
x = 5
if x > 10:
    print("valorea este mai mare ca 10")
    print("test etc etc ")
    x += 10
    print("test etc etc 2222 ")
print("Am iesit din if")


x = 15
if x > 10:
    print("valorea este mai mare ca 10")
    print("test etc etc ")
    x += 10
    print(x)
    print("test etc etc 2222 ")
print("Am iesit din if")


# if else

# numar = int(input("Introduce un numar: "))
#
# if numar % 2 == 0:
#     print("Numarul este par")
# else:
#     print("Numarul este impar")
# print("Codul curge in continuare")



# if elif else
print("-" * 20)


# optiunea = int(input("Alege o optiune [0, 1, 2]: "))
#
# if optiunea == 0:
#     print("ai ales 0")
# elif optiunea == 1:
#     print("ai ales 1")
# elif optiunea == 2:
#     print("ai ales 2")
# else:
#     print("ai ales orice altceva inafara de 0, 1, 2")



# EXERCITII

"""
Exercitiu: 
vrem sa implementam un nou sistem de tip bilete de avion. 
copiii sub 10 ani vor avea gratuitate la cumpararea biletului
adolescentii intre 10 si 18 ani vor avea 50% reducere
adultii vor plati pret intreg
seniorii peste 65 de ani vor avea reducere 30%
"""


# pret_intreg = 30
# pret_final = 0
# varsta = int(input("Va rugam introduceti varsta pasagerului: "))
#
# if varsta < 0:
#     print("Introduceti o varsta valida")
# elif varsta < 10:
#     print("biletul este gratuit")
# elif varsta >= 10 and varsta <= 18:
#     pret_final = pret_intreg / 2
# elif varsta > 18 and varsta < 65:
#     pret_final = pret_intreg
# else:
#     pret_final = pret_intreg - (pret_intreg * (30 / 100))
#
#
# print(f"Pretul final este {pret_final}")


"""
Company X sells merchandise to wholesale and retail outlets. Wholesale customers receive a two percent discount on all orders. 
The company also encourages both wholesale and retail customers to pay cash on delivery by offering a two percent discount 
for this method of payment. 
Another two percent discount is given on orders of 50 or more units. Each column represents a certain type of order.
What is the total discount?
"""

#
# discount = 0
# client_type = input("Enter the client type [ wholesale or retail ]: ")
# type_of_payment = input("Enter the type of payment [ card or cash ]: ")
# no_of_unit = int(input("Enter the number of units bought: "))
#
#
# # IF-uri pe acelasi nivel
# if type_of_payment == "cash":
#     discount += 0.2
#
# if client_type == "wholesale":
#         discount += 0.2
#
# if no_of_unit >= 50:
#         discount += 0.2
#
# print(discount)


"""
Bilete meci de fotbal
Persoanele cu varsta cuprinsa intre 12 si 16 ani pot intra gratis, iar cei sub 12 nu au voie. 
Persoanele cu varsta mai mica decat 18 sau mai mare decat 60 pot cumpara biletul cu 12$. 
Toate celelalte persoane pot cumpara biletul cu 20$
"""

age = int(input("Introduceti varsta: "))


if age < 0:
    print("Introdu o varsta valida")
elif age >= 12:
    print("Ai varsta necesara pentru a participa la meci")
    if age <= 16:
        print("Biletul este gratis")
    elif age == 17 or age > 60:
        print("Pretul biletului este 12$")
    else:
        print("Biletul este 20$")
else:
    print("Nu ai varsta necesara")



if age < 0:
    print("Introdu o varsta valida")
elif age >= 12 and age <= 16:
    print("Ai varsta necesara pentru a participa la meci")
    print("Biletul este gratis")
elif age == 17 and age > 60:
    print("Ai varsta necesara pentru a participa la meci")
    print("Pretul biletului este 12$")
elif age >= 18 and age <= 60:
    print("Ai varsta necesara pentru a participa la meci")
    print("Biletul este 20$")
else:
    print("Nu ai varsta necesara")

