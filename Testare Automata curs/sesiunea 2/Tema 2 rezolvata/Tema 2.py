# Ex:1 - Explica cu cum functioneaza un if else

"""
daca conditie=True
    se executa acest bloc de cod
altfel
    se executa acest bloc de cod
"""


# Ex:2 -Verifică și afișează dacă x este număr natural sau nu.
x = float(input("Scrie un numar: "))
if x >= 0 and x == int(x):
    print(f"{x} este un numar natural.")
else:
    print(f"{x} nu este un numar natural.")


# Ex:3 - Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
x = int(input("Scrie un numar: "))
if x > 0:
    print('pozitiv')
elif x < 0:
    print('negativ')
else:
    print('neutru')

# Ex:4 - Verifica si afiseaza daca x este intre -2 si 13

x = int(input("Scrie un numar: "))
if x > -2 and x < 13:
    print('Acest numar este curpins intre -2 si 13. ')
else:
    print('Acest numar nu este cuprins intre -2 si 13')


# Ex:5 - Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x = int(input("Scrie un numar: "))
y = int(input("Scrie al doilea numar: "))

if x - y < 5:
    print('Diferenta este mai mica decat 5.')


# Ex:6 - Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
x = int(input("Scrie un numar: "))
if not (5 < x < 27):
    print('Numarul nu este intre 5 si 27.')


# Ex:7 - x si y (int). Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
x = int(input("Scrie un numar: "))
y = int(input("Scrie al doilea numar: "))
if x == y:
    print("Numere x si y sunt egale.")
elif x > y:
    print(f"{x} este valoarea lui x si este mai mare decat y.")
else:
    print(f"{y} este valoarea lui y si este mai mare decat x.")


# Ex:8 - x, y, z - laturile unui triunghi. Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
x = int(input("Introdu lungimea laturei A: "))
y = int(input("Introdu lungimea laturei B: "))
z = int(input("Introdu lungimea laturei C: "))

if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print('Triunghiul este isoscel.')
elif x == y == z:
    print('Triunghiul este echilateral.')
else:
    print('Triunghiul este oarecare.')


# Ex:9 - Citeste o litera de la tastatura.Verifica si afiseaza daca este vocala sau nu
letter = input('Introduceti o litera: ')
letter = letter.lower()
if letter.isdigit():
    print('Nu ai introdus o litera, ci altceva.')
elif letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print('Litera este vocala.')
else:
    print('Litera nu este vocala.')


# Ex:10 - Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

nota = float(input("Care este nota primita? "))

if 9 <= nota <= 10:
    nota = "A"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 8:
    nota = "B"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 7:
    nota = "C"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 6:
    nota = "D"
    print(f"Nota primita in sistemul american este {nota}")
elif nota >= 4:
    nota = "E"
    print(f"Nota primita in sistemul american este {nota}")
elif 4 > nota >= 0:
    nota = "F"
    print(f"Nota primita este {nota}")
else:
    print('Nu ati introdus o nota de la 0 la 10.')


# Ex:11 - Verifica daca x are minim 4 cifre. (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = int(input("Introduceti un numar:  "))

if -999 <= x <= 999:
    print('Nu are minim 4 cifre')
else:
    print('Are minim 4 cifre')


# Ex:12 - Verifica daca x are exact 6 cifre
x = int(input("Introduceti un numar:  "))

# metoda 1
x = str(x)
if(x[0] == "-"):
    x = x[1:]

if len(x) == 6:
    print('are 6 cifre')
else:
    print('nu are 6 cifre')

# sau metoda 2
if x >= 100000 and x <= 999999:
    print('numarul are exact 6 cifre')
elif x >= -999999 and x <= -100000:
    print('numarul are exact 6 cifre')
else:
    print('numarul nu are exact 6 cifre')


# Ex:13 - Verifica daca x este numar par sau impar
x = int(input("Introduceti un numar:  "))

if x % 2 == 0:
    print("Numarul este par.")
else:
    print("Numarul este impar.")


# Ex:14 - x, y, z (int). Afiseaza care este cel mai mare din ele.
x = int(input("Introduceti numarul pt x: "))
y = int(input("Introduceti numarul pt y: "))
z = int(input("Introduceti numarul pt z: "))


if x >= y and x >= z:
    print(f'{x} este cel mai mare numar')
elif y >= x and y >= z:
    print(f'{y} este cel mai mare numar')
else:
    print(f'{z} este cel mai mare numar')


# Ex:15 -  x, y, z - reprezinta unghiurile unui triunghi. Verifica si afiseaza daca triunghiul este valid sau nu
x = 5
y = 8
z = 3

if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print('Triunghiul este valid.')
else:
    print('Triunghiul nu este valid.')


# Ex:16
'''
Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
cititi de la tastatura un int x
afiseaza stringul fara ultimele x caractere
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Alege cate caractere vrei sa tai de la final'))
print(string[0:-x])


# Ex:17
'''
acelasi string
declara un string nou care sa fie format din primele 5 caractere + ultimele 5
'''
string = 'Coral is either the stupidest animal or the smartest rock'
string1 = string[0:5]
string2 = string[-5:]
print(f'{string1}{string2}')


# Ex:18
'''
acelasi string
salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o functie care te ajuta sa faci asta)
folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest ' 
'''
string = 'Coral is either the stupidest animal or the smartest rock'
index_rock = string.index('rock')
print(string[:index_rock])


# Ex:19
"""
un string de la tastatura,verificăm dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
"""
word = input('alege un str')
assert word[0].lower() == word[len(word)-1].lower(), 'Primul si ultimul caracter sunt diferite'


# Ex: 20
'''avand stringul '0123456789'
afisati doar numerele pare 
acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas)
'''
word = '0123456789'
print(word[0::2])
print(word[1::2])

# Ex: 21
import random
dice_roll = random.randint(0, 6)
guess = int(input('Ghiceste zarul'))
if guess < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {guess} dar a fost {dice_roll}')
elif guess > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {guess} dar a fost {dice_roll}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {guess} si zarul a fost {dice_roll}')