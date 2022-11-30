# o variabila este o zona de memorie in care se stocheaza date, care mai tarziu va fi accesata  / # Problema 1
nume = 'Ciprian'      # Problema 2.
b = 38
c = 100.00
d = True
print(nume)
print(b+c)
print(d)

print(type(nume))               # Problema 3.
print(type(b))
print(type(c))
print(type(d))

print(type(c))                      # Problema 4
c = round(100.00)
print(type(c))

print('Salut, ce faci ' + nume + ' ?')           # problema 5
print(f'Varsta mea este de {b} de ani')
print(f'Apa fierbe la temperatura de {c} grade celsius')
print(f'Afirmatia ca 100 este mai mare decat 38 este {d}')

nume2 = input('Introduceti numele: ')            # Problema 6
prenume = input('Introduceti prenumele: ')
print(f'Numele complet are {len(nume2+prenume)} caractere')

lungimea = int(input('Introduceti lungimea: '))   # Problema 7
latimea = int(input('Introduceti latimea: '))
print(f'Aria dreptunghiului este {int(lungimea*latimea)}')

sir_caractere = 'Coral is either the stupidest animal or the smartest rock'  # Problema 8
print(f'Cuvantul "the" apare de {sir_caractere.count("the")} ori')

sir_caractere2 = 'Coral is either the stupidest animal or the smartest rock'
print(sir_caractere2.replace("the","THE"))

contine_cifre = False
sir_caractere3 = 'Coral is either the stupidest animal or the smartest  rock'   # Problema 10
for character in sir_caractere3:
    if character.isdigit():
        contine_cifre = True
print(contine_cifre)

# optionale
# Exercitiul 1

str = input('Introduceti textul: ')
x = len(str)
y = x//2
print("Caracterul din mijlocul stingului este: ", str[y])

# Exercitiul 2

is_palindrom = input("Introduceti cuvantul: ")
reverse = is_palindrom[::-1]
assert reverse == is_palindrom
print('Da este palindrom')

# Exercitiul 3

a1,b1,c1 = input("Introduceti 3 cuvinte ").split(" ")
print(a1)
print(b1)
print(c1)

# Exercitiul 4

sentence = input("Introduceti textul: ")
var1= sentence[0]
print(var1)
wrd1 = input('Introduceti primul cuvant: ')
wrd2 = input('Introduceti al II-lea cuvant: ')
f = wrd1[0]
g = wrd2[0]
print(f)
print(g)


#Exercitiul 5

user_name = input("Intoduceti utilizatorul: ")
password = input("Introduceti parola: ")
lungime_parola = "*" * len(password)
print(f'Parola pentru user {user_name} este {lungime_parola} si are {len(password)} caractere')













