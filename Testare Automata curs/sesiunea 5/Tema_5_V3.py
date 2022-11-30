'''
1.Funcție care să calculeze și să returneze suma a două numere
'''
def suma2(a,b):
    print(f'Suma numerelor este {a + b}')

suma2(3,6)
suma2(5,7)

'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''

def nr_impar(x):

    if x % 2 == 0:
        return True
    else:
        return False
a= nr_impar(6)
print(nr_impar(5))
b = nr_impar(8)
print(b)

'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''
def nume_intreg(nume,prenume1,prenume2):
    print(f'Numele meu complet este format din {len(nume + prenume1 + prenume2)} caractere')

nume_intreg('Pop','Flaviu','Ciprian')
nume_intreg('Pop', 'Eduard', 'Mihai')

'''
4. Funcție care returnează aria dreptunghiului
'''

def aria_dreptunghi(L,l):
    aria = L * l
    print(f'Aria dreptungiului este {aria}')

    return aria

aria_dreptunghi(2,6)
aria_dreptunghi(5,8)
aria_dreptunghi(12,65)


'''
5. Funcție care returnează aria cercului
'''
def aria_cerc(r, PI= 3.14):
    aria = PI * r**2
    print(f'Aria cercului este {aria}')

    return aria
aria_cerc(12)
aria_cerc(2)

'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
'''
text = 'ana are mere'
def cautator_caracter(text):
    for i in text:
        if text.count('a'):
            return True
        else:
            return False
text_intro = text
print(cautator_caracter(text_intro))


'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''
def numarator_caracter(text):

    numarator = {
        "litere_mari": 0,
        "litere_mici": 0
    }
    for litera in text:
        if litera.isupper():
            numarator["litere_mari"] += 1
        elif litera.islower():
            numarator["litere_mici"] += 1

    print(f'Textul introdus este: {text}')
    print(f'Numarul caracterelor mari este {numarator["litere_mari"]}')
    print(f'Numarul caracterelor mici este {numarator["litere_mici"]}')
text = str(input('Introduceti un text: '))
numarator_caracter(text)


'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''

lista_numere = [-5, -4, -3,-2,1,4,6,8,9]
def numere_pozitive(lista_numere):
    for n in lista_numere:
        if n > 0:
            print(f'Numerele pozitive sunt: {n}')
    return lista_numere

numere_pozitive(lista_numere)

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''

def nimic(x,y):
    for i in x,y:
        if x > y:
            print(f'{x} este mai mare ca {y}')
        elif x < y :
            print(f'{y} este mai mare ca {x}')
        elif x==y :
            print('Numerele sunt egale')

        return i

nimic(14,34)
nimic(56,23)
nimic(2,6)


'''
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''
lista_numere = {1,2,3,4,6,9,}
numar_introdus = int(input('Introduceti un numar pentru a verifica daca este in lista de numere: '))

def adaugare_numar(numar_introdus,lista_numere ):
    if numar_introdus in lista_numere:
        print(f'Nu am adaugat numarul {numar_introdus}, acesta este deja in lista')
        return False
    else:
        print(f'Am adugat numarul {numar_introdus}')
        lista_numere.add(numar_introdus)
        print(f'Lista noua este {lista_numere}')
        return True

adaugare_numar(numar_introdus,lista_numere )
'''
1 optional 
'''
y = int(input('Introduceti luna: '))

def calendar(x):
    lista_luni= {
        1: 'Ianuarie',
        2: 'Februarie',
        3: 'Martie',
        4: 'Aprilie',
        5: 'Mai',
        6: 'Iunie',
        7: 'Iulie',
        8: 'August',
        9: 'Septembrie',
        10: 'Octombrie',
        11: 'Noiembrie',
        12: 'Decembrie'
    }
    if x in lista_luni:
        print(f'Luna introdusa este {lista_luni[x]} si luna {lista_luni[x]} are numarul de zile:')
        if x in {1,3,5,7,8,10,12}:
            return 31
        elif x == 2:
            return 28
        else:
            return 30

a = calendar(y)
print(a)


"""
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
"""
def adunare(x,y):
    return x+y

def scadere(x,y):
    return x-y

def inmultire(x,y):
    return x * y

def impartire(x,y):
    return x / y

def calculator(x,y):
    a = adunare(x,y)
    b = scadere(x,y)
    c = inmultire(x,y)
    d = impartire(x,y)
    print(f'Suma: {a}')
    print(f'Scadere: {b}')
    print(f'Inmultire: {c}')
    print(f'Impartire: {d}')
calculator(10,2)


'''
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''

def contor_cifre(cifra):

    contor_cifre = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0
    }
    for i in lista_cifre:
        if i == 0:
            contor_cifre['0'] += 1
        elif i == 1:
            contor_cifre['1'] += 1
        elif i == 2:
            contor_cifre['2'] += 1
        elif i == 3:
            contor_cifre['3'] += 1
        elif i == 4:
            contor_cifre['4'] += 1
        elif i == 5:
            contor_cifre['5'] += 1
        elif i == 6:
            contor_cifre['6'] += 1
        elif i == 7:
            contor_cifre['7'] += 1
        elif i == 8:
            contor_cifre['8'] += 1
        elif i == 9:
            contor_cifre['9'] += 1

    print(f'Cifrele introduse au fost {cifra}')
    print(f'Cifra 0 a fost introdusa de: {contor_cifre["0"]} ori')
    print(f'Cifra 1 a fost introdusa de: {contor_cifre["1"]} ori')
    print(f'Cifra 2 a fost introdusa de: {contor_cifre["2"]} ori')
    print(f'Cifra 3 a fost introdusa de: {contor_cifre["3"]} ori')
    print(f'Cifra 4 a fost introdusa de: {contor_cifre["4"]} ori')
    print(f'Cifra 5 a fost introdusa de: {contor_cifre["5"]} ori')
    print(f'Cifra 6 a fost introdusa de: {contor_cifre["6"]} ori')
    print(f'Cifra 7 a fost introdusa de: {contor_cifre["7"]} ori')
    print(f'Cifra 8 a fost introdusa de: {contor_cifre["8"]} ori')
    print(f'Cifra 9 a fost introdusa de: {contor_cifre["9"]} ori')

lista_cifre = [0,1,2,3,4,5,6,7,8,9,6,5,2,3,5,6,7,1,2,3,6,8,9,]
contor_cifre(lista_cifre)



'''
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
'''

def numere(a,b,c):
    suma = 0                        # suma = a + b + c
    for i in a,b,c:
        if i == a:
            suma += i
        elif i == b:
            suma += i
        elif i == c:
            suma += i

    return suma

a = numere(2,5,9)
print(a)

'''
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
 de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
'''

def suma_totala(x):
    suma = 0
    for i in range(x+1):
        suma += i
    return suma

a = suma_totala(10)
print(a)


'''
Exerciții Opționale - Bonus
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''

def numere_comune():
    lista1 = [1, 1, 2, 3, 4]
    lista2 = [2, 2, 3, 4, 4]
    raspuns = []
    for i in lista1:
        if i in lista2:
            raspuns.append(i)
    print(f'Numerele comune sunt {raspuns}')

numere_comune()

'''
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
'''

pret_intreg = 100
discount = []
pret_final = pret_intreg * 0.9

def reducere_procentuala():
    if pret_final == pret_intreg * 0.9:
        print(f'Reducerea finala de 10 % este la {pret_final} lei')
    else:
        print('Reducere invalida')

reducere_procentuala()

'''
3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
'''

from datetime import datetime
data = datetime.now()

def time_line_Romania(data):
    print(f'Data si ora curenta sunt: {data}')
    return data

time_line_Romania(data)


from datetime import datetime
import pytz

print(pytz.all_timezones)
def time_China(x):
    return datetime.now(pytz.timezone(x))

print(time_China('Asia/Shanghai'))
print(time_China('Asia/Hong_Kong'))
print(time_China('Africa/Bamako'))

'''
4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
'''

import datetime
today = datetime.date.today()
future = datetime.date(2023,8,6)
birthday = future - today
print(f'Mai aveti {birthday.days} zile pana la ziua de nastere !!! ')