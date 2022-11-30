
"""
Exercitiu:
Scrie un program care citeste de la tastatura 3 numere: a, b, c
Verifica cate numere intre a si b sunt divizibile cu c
"""

a = int(input("Introduceti primul numar: "))
b = int(input("Introduceti al doilea numar: "))
c = int(input("Introduceti numarul la care trebuie impartit: "))
count = 0

# daca se da de la tastatura ca b e mai mic ca a, atunci le inversam
temp = 0
if(a > b):
    temp = b
    b = a
    a = temp

for i in range(a, b):
    if(i % c == 0):
        count += 1

print(f"{count} numere au fost gasite care sunt divizibile cu {c}")


"""
Exercitiu:
Scrieti un program prin care un user introduce de la tastatura o serie de numere integer, unul dupa altul folosind ENTER. Userul poate introduce cate numere vrea.
Cand userul introduce de la tastatura cuvantul "stop" in loc de un numar atunci programul ar trebui sa se opreasca si sa afiseze:
- toate numerele introduse sortate crescator
- cate numere pare au fost introduse si suma lor

Folositi continue si break
"""

saved_numbers = []

# vom crea un ciclu infinit dar care trebuie sa se opreasca la "stop"
while True:
    number = input("Introduceti un numar sau cuvantul 'stop': ")
    if number.lower() == "stop":
        break
    elif not number.lstrip('-').isdigit():                          # in cazul in care sunt numere negative scoatem - cu lstrip() si verificam cu isdigit
        if number.replace('.', '', 1).lstrip('-').isdigit():        # in cazul in care sunt numere float facem replace de . cu nimic si verificam cu isdigit
            print("Ati introdus un numar de tip float, trebuie sa introduceti doar integer, mai incercati!")
        else:
            print("Nu ati introdus un numar, mai incercati!")
        continue
    else:
        saved_numbers.append(int(number))

saved_numbers.sort()
count_even_no = 0
sum_even_no = 0
for number in saved_numbers:
    if number % 2 != 0:
        continue
    count_even_no += 1
    sum_even_no += number

print(f"Numerele introduse au fost: {saved_numbers}")
print(f"{count_even_no} numere pare au fost introduse si suma lor este {sum_even_no}")




"""
Exercitiu:
Scrabble este un joc în care jucătorii obțin puncte scriind cuvinte. 
Cuvintele sunt punctate prin adunarea valorilor punctuale ale fiecărei litere individuale. 
Scrieti un program care ia ca intrare un cuvânt șir și returnează scorul scrabble echivalent pentru acel cuvânt.
"""
score = {
    "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    "x": 8, "z": 10
}

word = input("Introduceti cuvantul: ").lower()
total = 0
for letter in word:
    total = score[letter] + total

print(f"Scorul total pentru cuvantul '{word}' este {total}")


"""
Exercitiu:
Scrieți un program Python care repetă numerele întregi de la 1 la 50. 
Pentru multiplii de trei tipăriți „Fizz” în loc de număr, iar pentru multiplii de cinci tipăriți „Buzz”. 
Pentru numerele care sunt multipli de trei și cinci, se afișează „FizzBuzz”
"""

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        continue
    elif number % 3 == 0:
        print("fizz")
        continue
    elif number % 5 == 0:
        print("buzz")
        continue
    print(number)

