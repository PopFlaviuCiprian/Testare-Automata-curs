# Exercitiul 1
'''
Instructiunile conditionale determina programele sa testeze diferite conditii si in functie de acestea
sa decida executia anumitor comenzi.
'''
"""
    Exercitiul 2
    Verifică și afișează dacă x este număr natural sau nu.
"""

numar_natural = int(input('Introduceti numarul: '))
if numar_natural>0:
    print("numarul introdus este un numar natural ")
elif numar_natural<0:
    print("Numarul introdus este un numar negativ ")
else:
    print("numarul introdus nu este un numar natural ")

'''
    Exercitiul 3
    Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''

numar2 = int(input("Introduceti numarul: "))

if numar2 >= 1:
    print('Numarul este pozitiv')
elif numar2 == 0:
    print('Numarul este neutru')
else:
    print('Numarul este negativ')

'''
    Exercitiul 4
    Verifică și afișează dacă x este între -2 și 13.
'''

x = int(input('Introduceti numarul: '))

if x < -2:
    print("Asteptati, se verifica daca numarul introdus se afla in intervalul -2 si 13")
    print('Numarul introdus este mai mic decat -2')
elif x > 13:
    print("Asteptati, se verifica daca numarul introdus se afla in intervalul -2 si 13")
    print('Numarul introdus este mai mare decat 13')
else:
    print('Numarul introdus se afla in intervalul -2 si 13')

'''
    Exercitiul 5
    Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
'''

x = int(input('Introduceti valoarea lui x: '))
y = int(input('Introduceti valoarea lui y: '))
if x-y <5:
    print('Diferenta dintre x si y este mai mica decat 5')
elif x-y == 5:
    print('Diferenta dintre x si y este 5')
else:
    print('Diferenta este mai mare')

'''
    Exercitiul 6
    Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
'''
x = int(input('Introduceti numarul: '))
print(x>=5 and not x<=27 or x<5)

'''
    Exercitiul 7
    x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare. 
'''

x = 5
y = 10
print(x==y)
print(y>x)

'''
    Exercitiul 8
    X, y, z - laturile unui triunghi.
    Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
    Dacă un triunghi este isoscel, atunci unghiurile de la bază sunt congruente.
    Triunghiul echilateral reprezintă triunghiul cu toate laturile de lungime egală (congruente). 
    Triunghi oarecare (oricare două laturi nu sunt congruente).
'''
print('Introduceti valorile laturilor triunghiului pentru a afla ce tip de triungi este: ')
x = int(input('Introduceti valoarea lui x: '))
y = int(input('Introduceti valoarea lui y: '))
z = int(input('Introduceti valoarea lui z: '))
if x==y==z:
    print('Triunghiul este echilateral avand toate laturile egale !')
elif x==y!=z:
    print('Triunghiul este isoscel avand 2 laturi echilaterale !')
elif x==z!=y:
    print('Triunghiul este isoscel avand 2 laturi echilaterale !')
elif y==z!=x:
    print('Triunghiul este isoscel avand 2 laturi echilaterale !')
else:
    print('Este un triunghi oarecare avand 3 laturi diferite')

'''
    Exercitiul 9
    Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
'''
litera = str(input('Introduceti litera: '))
vocale = ('a','e','i','o','u')
if litera == vocale[0]:
    print('Litera introdusa este o vocala')
elif litera == vocale[1]:
    print('Litera introdusa este o vocala')
elif litera == vocale[2]:
    print('Litera introdusa este o vocala')
elif litera == vocale[3]:
    print('Litera introdusa este o vocala')
elif litera == vocale[4]:
    print('Litera introdusa este o vocala')
else:
    print('Nu este vocala ! ')

'''
    Exercitiu 10
    Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
print('Convertor note !!!')
print('Introduceti nota obtinuta pentru a afla echivalentul notei in USA')
nota_obtinuta = float(input("Introduceti nota...."))
if nota_obtinuta >= 9:
    print('Ai luat un "A"')
elif nota_obtinuta >= 8:
    print('Ai luat un "B"')
elif nota_obtinuta >= 7:
    print('Ai luat un "C"')
elif nota_obtinuta >= 6:
    print('Ai luat un "D"')
elif nota_obtinuta > 4:
    print('Ai luat un "E"')
else:
    print('Ai luat un "F"')


#Exercitii optionale

'''
    Exercitiul 1
    Verifică dacă x are minim 4 cifre (x e int).
    (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
x = int(input('Introduceti numarul pentru a afla din cate cifre este format: '))
if x <= 999:
    print('Numarul nu are minim 4 cifre')
elif x >= 1000 and x<= 9999:
    print('Numarul introdus este format din 4 cifre')
else:
    print('Numarul are mai mult de 4 cifre')


'''
Exercitiul 2
Verifică dacă x are exact 6 cifre.
'''
x = int(input("Introduceti un numar: "))
if x>=1000000:
    print('Numarul introdus nu este format din 6 cifre')
elif x<= 999999 and x>=100000:
    print('Numarul introdus are exact 6 cifre')
else:
    print('Numarul nu este format din 6 cifre')

'''
    Exercitiul 3
    Verifică dacă x este număr par sau impar (x e int).
'''
x = int(input('Introduceti numarul pentru a verifica daca este par sau impar: '))
if x%2==0:
    print('Ati introdus un numar par')
else:
    print('Ati introdus un numar impar')

'''
    Exercitiul 4
    x, y, z (int)
Afișează care este cel mai mare dintre ele?
'''
x = int(input('Introduceti valoarea lui X: '))
y = int(input('Introduceti valoarea lui Y: '))
z = int(input('Introduceti valoarea lui Z: '))

if x>y and x>z:
    print(f'X este cel mai mare numar si are valoarea {x}')
elif y>z and y>x:
    print(f'Y este cel mai mare numar si are valoarea {y}')
elif z>x and z>y:
    print(f'Z este cel mai mare numar si are valoarea {z}')

'''
    Exercitiul 5
    X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
    Aflați stellingul inegalității triunghiului. 
    Această afirmație arata că suma a două laturi ale unui triunghi trebuie să fie mai mare decât a treia parte. 
    Dacă aceasta se aplică tuturor celor trei combinații, atunci aveți un triunghi adevărat.

'''
print('-------------Verificarea validitatii unui triunghi--------------------------------')
print('Introduceti 3 valori ale lui "X,Y si Z, pentru a afla daca triunghiul este valid ')
x = int(input('Introduceti valoarea lui X: '))
y = int(input('Introduceti valoarea lui Y: '))
z = int(input('Introduceti valoarea lui Z: '))

if x+y>z and x+z>y and y+z>x:
    print('Triunghiul este valid! ')
else:
    print('Triunghi invalid!!!, mai inearca ')

'''
    Exercitiul 6
    Având stringul: 'Coral is either the stupidest animal or the smartest rock'
    Citiți de la tastatură un int x
    Afișează stringul fără ultimele x caractere
    Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
x = int(input("Introduceti un numar: "))
var1 = ('Coral is either the stupidest animal or the smartest rock')
print(var1[:-x])

'''
    Exercitiul 7
    Având stringul: 'Coral is either the stupidest animal or the smartest rock'
    Declară un string nou care să fie format din primele 5 caractere
+ ultimele 5
'''
string_str = ('Coral is either the stupidest animal or the smartest rock')
string_nou = string_str[0:6] + string_str[-5:]
print(string_nou)

'''
    Exercitiul 8
Același string. 'Coral is either the stupidest animal or the smartest rock'
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest '
'''

string2 = ('Coral is either the stupidest animal or the smartest rock')
print(len(string2))
var5 = string2
print('Indexul de start al cuvantului rock este: ', var5[-4])
print(var5.split()[:-1]) # varianta 1
print(var5[0:52])        # varianta 2

'''
    Exercitiul 9
    Citește de la tastatura un string
    Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
    Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
'''
fraza = str(input('Introduceti un text: '))
fraza = fraza.upper()
assert fraza[0]==fraza[-1];
print('Primul si ultimul caracter sunt la fel ')

'''
Exercitiul 10
Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)    
'''
sir1 = '0123456789'
print('Se afiseaza doar numere pare   ',sir1[0:9:2])
print('Se afiseaza doar numere impare ',sir1[1:10:2])

'''
    Exercitiul 11
    Joc ghicit zarul
'''
import random
random = random.randint(1,6)
dice_roll = int(input('Zarurile au fost aruncate, ghiceste numarul, intre 1 si 6: '))
while random != dice_roll:
    if dice_roll > random:
        print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {dice_roll}  dar a fost {random}')
    else:
        print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {dice_roll} dar a fost {random}')
    dice_roll = int(input('Zarurile au fost aruncate, ghiceste numarul, intre 1 si 6: '))
print(f'Ai ghicit. Felicitari! Ai ales {dice_roll} si zarul a fost {random}')