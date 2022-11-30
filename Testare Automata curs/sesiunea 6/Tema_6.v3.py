'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()    diametrul: d =	2 × r,       circumferinta: C =	π × d = 2 × π × r
'''
from math import pi
class Cerc():


    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Culoarea cercului este {self.culoare} si are raza {self.raza} ')

    def aria(self):
        return pi * (self.raza ** 2)

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 2 * pi * self.raza

cercul1 = Cerc(4, 'Albastru ')
cercul1.descrie_cerc()
print(f'Aria cercului  este {cercul1.aria()}')
print(f'Diametrul cercului  este {cercul1.diametru()}')
print(f'Circumferinta cercului  este: {cercul1.circumferinta() }')

print(150*'*')

cercul2 = Cerc(10, 'Rosu ')
cercul2.descrie_cerc()
print(f'Aria cercului este {cercul2.aria()}')
print(f'Diametrul cercului este {cercul2.diametru()}')
print(f'Circumferinta cercului este: {cercul2.circumferinta() }')

print(150*'*')

'''2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
aria = lungime * latime
perimetrul = suma tuturor laturilor ab+bc+cd+da
'''

class Dreptunghi():


    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are lungimea laturilor {self.lungime}, latimea laturilor {self.latime} si culoarea {self.culoare}')

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return (self.lungime * 2) + (self.latime * 2)

    def schimba_culoarea(self,culoare):
        self.culoare = culoare
        print(f'Culoarea dreptunghiului a fost schimbata in {self.culoare}')


dr1 = Dreptunghi(4,3,'Alb')
dr1.descrie()
print(f'Dreptunghiul are aria {dr1.aria()}')
print(f'Dreptunghiul are  perimetrul {dr1.perimetru()}')
dr1.schimba_culoarea('Verde')
dr1.descrie()

print(150 *'*')

dr2 = Dreptunghi(9,12,'Gri')
dr2.descrie()
print(f'Dreptunghiul are aria {dr2.aria()}')
print(f'Dreptunghiul are  perimetrul {dr2.perimetru()}')
dr2.schimba_culoarea('Negru')
dr2.descrie()

print(100* '*')
'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''

class Angajat:


    def __init__(self, nume, prenume, salariu):

        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul are numele {self.nume}  {self.prenume}')

    def nume_complet(self):
        return self.nume + " " + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        return self.salariu + (self.salariu * (procent / 100))


angajat1 = Angajat('Muresan','George',2500 )
angajat1.descrie()
print(angajat1.nume_complet(),'are un salariu lunar de',angajat1.salariu_lunar(), 'lei','si un salariu anual de', angajat1.salariu_anual(), 'lei')
print('Fiind cel mai vechi din firma, i se va mari salariul de la ' ,angajat1.salariu_lunar(), 'lei la ', angajat1.marire_salariu(50),'lei')

print(150 *'*')

angajat2 = Angajat('Vancea','Madalina',1500 )
angajat2.descrie()
print(angajat2.nume_complet(),'are un salariu lunar de',angajat2.salariu_lunar(), 'lei','si un salariu anual de', angajat2.salariu_anual(), 'lei')
print('Fiind un angajat mai nou i se va mari salariul de la ' ,angajat2.salariu_lunar(), 'lei la ', angajat2.marire_salariu(25),'lei')


print(100* '*')
'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)  debitare = extragere bani din cont
● creditare_cont(suma)  creditare = virare bani in cont
'''

class Cont:

    def __init__(self, iban, titular_cont, sold):

        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold


    def afisare_sold(self):
        print(f'Numele proprietarului este {self.titular_cont}, numarul contului este {self.iban} si are soldul {self.sold} lei')

    def creditare_cont(self, suma):
            self.sold += suma
            return suma

    def debitare_cont(self, suma):
        self.sold -= suma
        return suma

cont1 = Cont('RO12345', 'Pop Ciprian', 10500)
cont1.afisare_sold()
print(f'Contul a fost alimentat cu suma de {cont1.creditare_cont(30000)} lei')
cont1.afisare_sold()
print(f'Din cont au fost extrasi {cont1.debitare_cont(15000)}  lei')
cont1.afisare_sold()

print(150 * '*')

cont2 = Cont('RO987654', 'John Smith', 50000)
cont2.afisare_sold()
print(f'Contul a fost alimentat cu suma de {cont2.creditare_cont(160000)} lei')
print(f'Din cont au fost extrasi {cont2.debitare_cont(25000)}  lei')
cont2.afisare_sold()

'''
clasa cont dar cu if si else la debitare

class Cont:

    def __init__(self, iban, titular_cont, sold):

        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold


    def afisare_sold(self):
        print(f'Numele proprietarului este {self.titular_cont}, numarul contului este {self.iban} si are soldul {self.sold} lei')

    def creditare_cont(self, suma):
        self.sold += suma
        return suma


    def debitare_cont(self, suma):
        if suma > self.sold:
            print('Fonduri insuficiente')
        else:
            self.sold -= suma
            print(f'Din cont au fost retrasi {suma}')


cont1 = Cont('RO12345', 'Pop Ciprian', 10500)
cont1.afisare_sold()
cont1.creditare_cont(17000)
print(f'Contul a fost alimentat cu suma de {cont1.creditare_cont(30000)} lei')
cont1.afisare_sold()
cont1.debitare_cont(75000)
cont1.afisare_sold()

print(150 * '*')

cont2 = Cont('RO987654', 'John Smith', 50000)
cont2.afisare_sold()
print(f'Contul a fost alimentat cu suma de {cont2.creditare_cont(160000)} lei')
cont2.debitare_cont(25000)
cont2.afisare_sold()
cont2.debitare_cont(560000)
'''
print(100* '*')

#  Optionale
'''1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
'''

from datetime import datetime
class Factura():
    SERIA = 'SNO'

    def __init__(self,numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        return cantitate

    def schimba_pretul(self, pret):
        self.pret = pret
        return pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        return nume

    def genereaza_factura(self):
        print(f'Factura cu seria {self.SERIA} nr: {self.numar}')
        data_curenta = datetime.today()
        print(f'Data: {data_curenta}')
        print(f'Nume: {self.nume_produs}, cantitate: {self.cantitate}, pret: {self.pret_buc}')
        total = self.pret_buc * self.cantitate
        print(f'Total: {total}')



factura1 = Factura(1234, 'Factura curent', 1, 145)
factura1.genereaza_factura()
factura1.schimba_cantitatea(3)
factura1.genereaza_factura()

print(100* '*')

factura2 = Factura(10001, 'Factura Gaz', 1, 369)
factura2.genereaza_factura()

print(100* '*')
'''
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
'''
class Masina:

    culori_disponibile = {'Albastru','Rosu','Verde','Negru' }
    culoare = 'Gri'
    viteza_actuala = 0
    marca = 'Skoda'
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Masina {self.marca}, are rmatoarele caracteristici:')
        print(f'Marca: {self.model}, Culoare : {self.culoare}, Viteza: {self.viteza_actuala}')
        print(f'Inmatriculata: {self.inmatriculata}, Viteza maxima: {self.viteza_maxima} km/h')

    def inmatriculare(self):
        self.inmatriculata = True
        return self.inmatriculata

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f'Culoarea masinii a fost schimbata in {self.culoare}')
        else:
            print('Culoare indisponibila')

    def accelereaza(self, viteza):
        if viteza <=  0 :
            print('Eroare')
        elif viteza >= self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            print(f'Masina a atins viteza maxima')
        elif viteza < self.viteza_maxima:
            self.viteza_actuala += viteza
            print(f'Viteza a crescut la {self.viteza_actuala} km/h')

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Masina a franat si are viteza {self.viteza_actuala} km/h')

masina = Masina('Octavia',220)
masina.descrie()
print(f'Masina este inmaticulata: {masina.inmatriculare()}')
masina.vopseste('Albastru')
masina.descrie()
masina.accelereaza(219)
print(100*'*')
masina2 = Masina('Fabia',200)
masina2.descrie()
print(f'Masina este inmaticulata: {masina2.inmatriculare()}')
masina2.vopseste('Rosu')
masina2.descrie()
masina2.accelereaza(190)
masina2.franeaza()

print(100* '*')
'''
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
'''

class TodoList:
    todo = {

    }

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        self.todo.pop(nume)

    def afiseaza_todo_list(self):
        print(self.todo.keys())

    def afiseaza_detalii_suplimentare(self,nume_task):
            if nume_task in self.todo:
                print(f'Detaliile suplimentare sunt {self.todo.items()}')
            if nume_task not in self.todo:
                intro_text = input(f'Doriti adaugarea taskului in lista ? Da/Nu ')
                if intro_text == 'Da':
                    intro2_text = input(f'Introduceti detaliile taskului, (Ex: Numele, Descriere): ')
                    self.adauga_task(nume_task,intro2_text)
                    print(self.todo)
                else:
                    print('La revedere')


task1 = TodoList()
task1.adauga_task('Cumparaturi', 'paine, lapte ,oua, cascaval')
print(task1.todo)
task1.afiseaza_detalii_suplimentare('Reteta prajitura')
