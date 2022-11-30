'''
    Exercitiul 1

'''
note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
print(note_muzicale[::-1])
note_muzicale = note_muzicale[::-1]   # suprascrie si salveaza lista de la coada la cap
print(note_muzicale)    # tipareste lista de la coada la cap
note_muzicale.reverse()  # inverseaza si suprascrie lista salvata anterior in note_mzicale_suprascris
print(note_muzicale)     # tipareste lista suprascrisa mai sus (varianta originala a listei de inceput)

'''
    Exercitiul 2
'''
note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print('Nota "do" apare de', note_muzicale.count('do') ,'ori')

'''
    Exercitiul 3
'''
lista1 = [3,1,0,2]
lista2 = [6,5,4]
lista1.extend(lista2) # prima variata folosim extend
print(lista1)
print(lista1+lista2) # varianta 2 folosim +

'''
    Exercitiul 4
'''
lista1 = [3,1,0,2]
lista1.sort()
print(lista1)
lista1.remove(0)
print(lista1)

'''
    Exercitiul 5
'''
lista1 = [3,1,0,2]   # o lista goala va afisa intodeauna afirmatia booleana fals
if lista1:                   # if lista afirma true
    print('Lista are date')
else:
    print('Lista este goala') # else afirma false cand nu are date si este goala

'''
    Exercitiul 6
'''
lista1 = ['3','1','0','2']
lista1.clear()
print(lista1)

'''
    Exercitiul 7
'''
lista1 = ['3','1','0','2']
lista1.clear()
if lista1:
    print('Lista are date')
else:
    print('Lista este goala')

'''
    Exercitiul 8
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

'''
    Exercitiul 9
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print('Ana a luat nota: ', dict1['Ana'])
print('Gigel a luat nota: ', dict1['Gigel'])
print('Dorel a luat nota: ', dict1['Dorel'])

'''
    Exercitiul 10
'''

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1['Dorel'] = 6
print('Dorel a luat nota: ', dict1['Dorel'])

'''
    Exercitiul 11
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1.pop('Dorel')
dict1['Ionel'] = 9
print(dict1)

'''
    Exercitiul 12
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

'''
    Exercitiul 13
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
if weekend.issubset(zile_sapt):
    print('Weekend este un subset ')
else:
    print('Weekend nu este subset')

'''
    Exercitiul 14
'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt.difference(weekend))

'''
    Exercitiul 15
'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt.intersection(weekend))

'''
    Exercitii optionale

'''

jucatori = ['Andrei','Alin','Alex','Calin','Daniel']
SCHIMBARI_MAX = 3
schimbari_efectuate = (SCHIMBARI_MAX-1)
jucator_schimbat = jucatori[2]
jucator_nou = 'Iliescu'
jucator_nou2 = 'Vasile' # am creat variabila pentru a testa codul cand jucatorul nu se afla in teren
in_teren = jucatori
print(in_teren)

if jucator_schimbat in in_teren and schimbari_efectuate<= SCHIMBARI_MAX:
    print(f'Jucatorul este in teren, si nu se poate efectua schimbarea, mai ai {SCHIMBARI_MAX} schimbari ')
else:
    print('Jucatorul nu este in teren si se poate efectua schimbarea, ')

print('Jucatorul',jucatori.pop(2),'a iesit din teren')

jucatori[2] = jucator_nou
print('A iesit', jucator_schimbat, 'si a intrat', jucatori[2],'mai ai',schimbari_efectuate, 'schimbari')

if jucator_nou2 in in_teren and schimbari_efectuate<= SCHIMBARI_MAX:
    print('Jucatorul',jucator_nou2,'este in teren, si se poate efectua schimbarea')
else:
    print('Jucatorul',jucator_nou2,' nu este in teren nu se poate efectua schimbarea  ')
    print('Mai ai',schimbari_efectuate,'schimbari')
