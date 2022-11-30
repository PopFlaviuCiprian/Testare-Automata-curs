"""
Clasa Masina
Atribute: marca, culoare, motor_pornit, viteza
Metode: start, stop, accelereaza, incetineste, vopseste

"""

class Masina:

    def __init__(self, make, model_en, color):
        self.marca = make
        self.model = model_en
        self.culoare = color
        self.motor_pornit = False
        self.viteza = 0

    # metoda
    def prezinta_masina(self):
        print(f"Masina {self.marca} {self.model} {self.culoare} are motorul pornit: {self.motor_pornit} si are viteza {self.viteza}")

    def start(self):
        self.motor_pornit = True

    def stop(self):
        self.motor_pornit = False
        self.viteza = 0

    def accelereaza(self, accelereaza_cu):
        if self.motor_pornit:
            self.viteza += accelereaza_cu
            print(f"Masina a ajuns la {self.viteza} km")
        else:
            print("Nu se poate accelera, nu este pornit motorul")

    def incetineste(self, incetineste_cu):
        if self.motor_pornit and self.viteza > 0:
            if self.viteza > incetineste_cu:
                self.viteza -= incetineste_cu
            else:
                self.viteza = 0
            print(f"Masina a ajuns la {self.viteza} km")
        else:
            print("Nu putem incetini pentru ca nu e pornit motorul sau viteza este deja 0")

masina_test = Masina('VK', 'Test', 'gri')
masina_test.prezinta_masina()
print(masina_test.motor_pornit)

# aici nu va accelera masina pentru ca motor_pornit este False
masina_test.accelereaza(40)

# asa ca mai intai trebuie sa pornim masina
masina_test.start()
print(masina_test.motor_pornit)
masina_test.accelereaza(40)
print(masina_test.viteza)
masina_test.prezinta_masina()

masina_test.accelereaza(30)
masina_test.prezinta_masina()

masina_test.stop()
print(masina_test.viteza)
print(masina_test.motor_pornit)
# nu putem accelera pt ca masina e oprita
masina_test.accelereaza(20)
masina_test.prezinta_masina()

# nu putem incetini pt ca oricum masina e oprita
masina_test.incetineste(20)
masina_test.start()
# nu putem incetini pt ca oricum viteza este 0
masina_test.incetineste(20)

masina_test.accelereaza(100)
masina_test.incetineste(40)