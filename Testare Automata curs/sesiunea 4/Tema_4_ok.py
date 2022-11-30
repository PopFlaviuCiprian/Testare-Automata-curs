
'''
    Exercitiul 1
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == 'Mercedes':
        print(f'Masina mea preferata este {i}')



masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
for i in masini:
    print(f'Masina mea preferata este {i} ')


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
i = 0
while i < len(mașini):
    print(f'Masina mea preferata este {masini[i]} ')
    i += 1


'''
    Exercitiul 2
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
for i in range(1,len(masini)-1):

    masini[i] = masini[i].upper()
else:
    print(masini)

'''
    Exercitiul 3
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for i in masini:
    print(i)
    if i == 'Mercedes':
        print(f'Am gasit masina dorita de dvs. care este:  {i} ')
        break
    else:
        print(f'Am gasit masina {i}, mai cautam ! ')



'''
    Exercitiul 4
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']

for i in masini:
    if i == 'Lastun' or i == 'Trabant':
        continue
    print(f'S-ar putea sa va placa masina: {i}')

'''
    Exercitiul 5
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
masini_vechi = []
masini_noi = []
new = 'Tesla'

for masina in masini:
    # print(masina)
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi= masina
        print(f'Masinile vechi sunt: {masini_vechi}')
masini[5]=masini[7]= new
print(f'Modelele noi sunt : {masini}')



'''
    Exercitiul 6
'''
pret_masini = {
    'Dacia': 6000,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
print(pret_masini.items())
suma_disponibila = 15000

for marca, suma in pret_masini.items():
    if suma < suma_disponibila:
        print(f'Pentru un buget sub 15000 euro puteti alege marca {marca} care costa {suma} euro')


'''
    Exercitiul 7
'''
numere = [5,7,3,9,3,3,1,0,-4,3]
var1 = 0
for i in numere:
    print(i)
    if i == 3:
        var1 += 1
print(f'cifra 3 apare de {var1} ori')


'''
    Exercitiul 8
'''
numere = [5,7,3,9,3,3,1,0,-4,3]
suma_nr = 0
for i in numere:
    print(i)
    suma_nr += i
print(f'Suma numerelor este {suma_nr}')

'''
    Exercitiul 9
'''
numere = [5,7,3,9,3,3,1,0,-4,3]
numar_maxim = 0
for i in numere:
    print(i)
    if i > numar_maxim:
        numar_maxim =  i
print(f'Cel mai mare numar este: {numar_maxim}')

'''
    Exercitiul 10
'''

numere = [5,7,3,9,3,3,1,0,-4,3]
for i in range(len(numere)):
    if numere[i] > 0 :
        numere[i] = -numere[i]
print(numere)

'''
Optional 1
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
    if i < 0 and i % 2==0  or  i % 2 == 0:
        numere_pare.append(i)
    if i < 0 and i % 2==1  or  i % 2 == 1:
        numere_impare.append(i)
    if i >= 0:
        numere_pozitive.append(i)
    if i < 0 :
        numere_negative.append(i)

print(f'Numerele pare sunt {numere_pare}')
print(f'Numerele impare sunt {numere_impare}')
print(f'Numerele pozitive sunt {numere_pozitive}')
print(f'Numerele negative sunt {numere_negative}')


'''
Exercitiul 2
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
i = 0
while i < len(alte_numere):
    for j in range(len(alte_numere)-1):
        if alte_numere[j] > alte_numere[j+1]:
            var1 = alte_numere[j]
            # print(var1)
            alte_numere[j]=alte_numere[j+1]
            # print(alte_numere)
            alte_numere[j+1] = var1
            # print(alte_numere)
    i +=1
print(alte_numere)

'''
Exercitiul 3
'''
import random
numar_secret = random.randint(1,30)
numar_ghicit = None
nr_introdus = int(input('Introduceti un numar intreg intre 1 si 30: '))

while numar_ghicit != numar_secret:
    if nr_introdus > numar_secret:
        print('Numarul introdus este mai mare, mai incearca! ')
    if nr_introdus < numar_secret:
        print('Numarul introdus este mai mic, mai incearca!! ')
    nr_introdus = int(input('Introduceti un numar intreg intre 1 si 30: '))
    if nr_introdus == numar_secret:
        print('Ai ghicit numarul, felicitari !!')
        break


'''
Exercitiul 4
'''
n = int(input('Introduceti un numar: '))
for i in range(n):
    for j in range(i,-1,-1):
        print(i+1, end=' ')
    print()

'''
Exercitiul 5
'''
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(tastatura_telefon[i][j], end=" ")
    print()