# EX 1: Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# a)	Afiseaz-o
# b)	Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# c)	Printeaza varianta actuala (inversata)
# d)	Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# e)	Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
#
# Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua.
# Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
#a
print(note_muzicale)
#b
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
#c
note_muzicale.reverse()
#d
print(note_muzicale)


# EX 2: De cate ori apare ‘do’?

print(note_muzicale.count('do'))


# EX 3: Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

# varianta 1
lista_noua_v1 = lista1 + lista2
print(lista_noua_v1)

# varianta 2
lista1.extend(lista2)
lista_noua_v2 = lista1
print(lista_noua_v2)


# EX 4: Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista

lista_noua_v1.sort()
print(lista_noua_v1)
lista_noua_v1.remove(0)
print(lista_noua_v1)


# EX 5: Folosind un if verificati lista generata la ex3 si afisati
# -	Lista este goala
# -	Lista nu este goala

if len(lista_noua_v1) >= 1:
    print('Lista nu este goala')
else:
    print('Lista este goala')


# EX 6: Folositi o functie care sa stearga lista de la ex3

lista_noua_v1.clear()

# EX 7: Copy paste la ex 5. Verificati inca o data.
# Acum ar trebui sa se afiseze ca lista e goala

if len(lista_noua_v1) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')


# EX 8: Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)

dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5}
print(dict1.keys())


# EX 9: Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie

print(f'Ana a luat nota: {dict1["Ana"]}')
print(f'Gigel a luat nota: {dict1["Gigel"]}')
print(f'Gigel a luat nota: {dict1.get("Dorel")}')


# EX 10: Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare

# metoda 1
dict1['Dorel'] = 6
print(dict1.get('Dorel'))

# metoda 2
dict1.update({"Dorel": 6})
print(dict1.get('Dorel'))


# EX 11: Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi

dict1.pop('Gigel')
print(dict1)
dict1['Ionica'] = 9
print(dict1)


# EX 12: Set
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.add('luni')
print(zile_sapt)


# EX 13: Folositi un if si verificati daca
# -	Weekend este un subset al zilelor din sapt
# -	Weekend nu este un subset al zilelor din sapt

if weekend.issubset(zile_sapt):
    print('weekend este un subset al zilelor sapt')
else:
    print('weekend NU este un subset al zilelor sapt')


# EX 14: Afisati diferentele dintre aceste 2 seturi

diferenta = zile_sapt.difference(weekend)
print(diferenta)


# EX 15: Afisati intersectia elementelor din aceste 2 seturi

intersectia = zile_sapt.intersection(weekend)
print(intersectia)


# EX 16: Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# -	Efectuam schimbarea
# -	Stergem jucatorul scos din lista
# -	Adaugam jucatorul intrat
# -	Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# -	Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# -	Afisati ‘mai aveti z schimbari’
#
# Testati codul cu diferite valori
#
# Google search hint
# “how to check if item is in list python”

SCHIMBARI_MAXIME = 3
schimbari_efectuate = 2
# calculam si initializam schimbari ramase
schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
echipa_in_teren = ['j1', 'j2', 'j3', 'j4', 'j5']
jucator_in = 'j6'
jucator_out = 'j1'

# daca jucatorul e in teren SI daca mai am schimbari
if jucator_out in echipa_in_teren and schimbari_ramase > 0:
    if jucator_in in echipa_in_teren:            # eliminam cazul cand jucatorul este deja in teren
        print('Nu putem face schimbarea deoarece jucatorul introdus este deja in teren')
    else:                               # cazul valid, facem tot ce trebuie facut
        echipa_in_teren.remove(jucator_out)      # scoatem jucatorul
        echipa_in_teren.add(jucator_in)          # adaugam jucatorul nou
        schimbari_ramase = schimbari_ramase - 1     # contorizam schimbarea
        print(f'Schimbare efectuata cu succes!')
        print(f'A intrat {jucator_in}, a iesit {jucator_out}, mai aveti {schimbari_ramase} schimbari')
else:
    if schimbari_ramase <= 0:
        print('Nu mai ai schimbari')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren')
print(f'Actuala echipa este {echipa_in_teren}')

# caz1 jucator adaugat deja in teren => nu se face sch {'j1', 'j5', 'j3', 'j4', 'j2'}
# caz2 jucator scos nu este in teren => nu se face sch {'j1', 'j5', 'j3', 'j4', 'j2'}
# caz3 happy flow, cand putem face sch, jucator in nu e in teren, jucator out e in teren {'j4', 'j6', 'j2', 'j5', 'j3'}
# caz4 nu mai am schimbari => nu mai am schimbari {'j1', 'j5', 'j3', 'j4', 'j2'}