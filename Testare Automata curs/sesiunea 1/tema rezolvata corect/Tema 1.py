# Tema 1

#EX 1: In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# o variabila este o zona din memorie care stocheaza o valoare

#EX 2: Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool
text = 'Eu sunt un string'
scor = 9
nota = 7.9
is_suspended = False


#EX 3: Utilizat functia type pentru a verifica daca au tipul de date asteptat
print('Tipul variabilei scor este ', type(scor))
print('Tipul variabilei text este ', type(text))
print('Tipul variabilei nota este ', type(nota))
print('Tipul variabilei is_suspended este ', type(is_suspended))

#EX 4: Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere). Verificati tipul acesteia
aprint('Variabila nota inainte de round are valoarea', nota, 'si tipul de date', type(nota))
nota = round(nota)
print('Variabila nota dupa round are valoarea', nota, 'si tipul de date', type(nota))

#EX 5: folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
print(f'Am afisat in consola urmatorul text: "{text}"')
print(f'Tipul scorului', scor, 'este', type(scor))

#EX 6: citeste de la tastatura numele. citeste de la tastatura prenumele. afiseaza 'Numele complet are x caractere'
nume = input('Introduce numele:')
prenume = input('Introduce prenumele:')
nr_caractere = len(nume) + len(prenume)
print(f'Numele complet {nume} {prenume} are {nr_caractere} caractere')

#EX 7: citeste de la tastatura lungimea. citeste de la tastatura latimea. afiseaza 'Aria dreptunghiului este x'
lungime = input('Introduce lungimea:')
latime = input('Introduce latimea:')
aria = int(lungime) * int(latime)
print(f'Aria dreptunghiului este {aria}')

#EX 8: Avand stringul: 'Coral is either the stupidest animal or the smartest rock'. afisati de cate ori apare cuvantul 'the'
prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop.count('the'))

#EX 9: acelasi string. inlocuieste the cu THE peste tot. printeaza rezultatul
print(prop.replace("the", "THE"))

#EX 10: acelasi string de mai sus. folositi un assert ca sa verificati daca acest string contine doar numere
assert prop.isdigit() is True, 'Propozitia nu contine doar cifre'

#EX 11: citeste de la tastatura un string de dimensiune impara. afiseaza caracterul din mijloc
string11 = input("Introduce un string cu dimensiune impara:")
mijloc = string11[int(len(string11)/2)]
print(f'caracterul din mijloc este {mijloc}')

#EX 12: Folosind assert, verificati daca un string este palindrom
string12_1 = 'abccba'  # true
string12_2 = 'Sunt un palindrom?' # false

assert string12_1 == string12_1[::-1]
assert string12_2 == string12_2[::-1]

# EX 13: folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala') si salveaza fiecare cuvant intr-o variabila. acum printeaza ambele variabile pentru verificare
text = input('Scrie un string: ')
x, y = text.split(' ')
print(f'Primul cuvant este: {x}')
print(f'Ultimul cuvant este: {y}')

#Ex_14 -citeste un string de la tastatura (eg: alabala portocala).salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
#capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
text = str(input('Scrie un string: '))
x = text[0]
y = text.replace(x, x.upper())
print(y[0].replace(y[0], y[0].lower()) + y[1:-1] + y[-1].replace(y[-1], y[-1].lower()))

#Ex_15 - citeste un user de la tastatura, citeste o parola. Afiseaza: 'Parola pt user x este ***** si are x caractere'
user = str(input('User-ul este: '))
parola = str(input('Tastraza parola: '))
parola_ascunsa = '*' * len(parola)
print(f'Parola pentru userul {user} este {parola_ascunsa} si are {len(parola)} caractere')

