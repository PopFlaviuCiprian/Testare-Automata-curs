"""
Clasa Masina
Atribute: marca, culoare, motor_pornit, viteza
Metode: start, stop, accelereaza, incetineste, vopseste

"""


class Masina:

    # atribute default
    marca = None
    model = None
    culoare = "alb"
    motor_pornit = False
    viteza = 0

    # constructor - o metoda care ne obliga sa dam ca valori parametrii mentionati intre () atunci cand cream obiectul
    def __init__(self, make, model_en):
        self.marca = make     # self.marca este atributul obiectului instantiat
                              # make este parametrul functiei, prin el va veni valoarea pe care o dam
                              # cand vom crea obiectul
        self.model = model_en

    # metoda
    def prezinta_masina(self):
        print(f"Masina {self.marca} {self.model} {self.culoare} are motorul pornit: {self.motor_pornit} si are viteza {self.viteza}")




# masina1 = Masina()   # am instantiat obiectul masina1 de tip Masina (de tip clasa Masina)
# print(masina1)
# # am accesat metoda prezinta_masina din interiorul clasei Masina
# masina1.prezinta_masina()
#
# # putem sa si modificam atributele prin .
# masina1.marca = "Audi"
# print(masina1.marca)
# masina1.prezinta_masina()
#
# masina2 = Masina()
# masina2.marca = "BMW"
# masina2.prezinta_masina()

# ne va da eroare pentru ca suntem obligati sa dam marca si modelul prin pricina constructorului
# masina0 = Masina()

masina3 = Masina("Skoda", "Octavia")
masina3.prezinta_masina()
masina3.model = "Test"
masina3.prezinta_masina()

masina4 = Masina("Vokswagen", "Golf")
masina4.prezinta_masina()