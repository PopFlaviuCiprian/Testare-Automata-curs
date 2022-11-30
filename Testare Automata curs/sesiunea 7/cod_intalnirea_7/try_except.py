"""
Exceptiile: clase speciale Python folosite atunci cand ceva nu meerge bine in cod
Folosim mecanismul try-except pentru a gestiona posibilele exceptii aruncate in codul nostru,
astfel incat programul sa NU se opreasca
"""


lista_numere = [12, 3, 5, 6]

# print(lista_numere[4])    # -> va sari eroare pentru ca in lista nu exista element la pozitia 4


try:
  print(lista_numere[4])
except:
  print("A sarit o eroare")


try:
  print(lista_numere[4])
except Exception as e:
  print(f"A sarit o eroare: {e}")

try:
  print(lista_numere[4])
except IndexError as e:
  print(f"A sarit o eroare: {e}")


# try:
#   print(lista_numere[4])
# except AssertionError as e:       # -> tot va sari eroare pentru ca nu a gasit o eroare de tip Assertion
#   print(f"A sarit o eroare: {e}")

# assert 5 == 6   # -> sare o eroare de tip Assertion

try:
  assert 5 == 6 , "valorile nu sunt egale"
except AssertionError as e:
  print(f"A sarit o eroare: {e}")

print(lista_numere[0])


numar_studenti = int(input("Introduceti numarul de studenti: "))
lista_studenti = []

for student in range(numar_studenti):
  if student > 5:
    print(lista_studenti)
    raise IndexError("Nr de studenti sa nu fie peste 5")
  lista_studenti.append("Andrei")
  print(student)

print(f"Lista de studenti: {lista_studenti}")
