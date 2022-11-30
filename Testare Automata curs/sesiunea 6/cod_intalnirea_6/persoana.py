

class Person():

    def __init__(self, name, first_name, age):
        self.name = name
        self.first_name = first_name
        self.age = age

    def prezentare(self):
        print(f"Salut, eu sunt {self.name} {self.first_name} si am {self.age} ani")

    def get_varsta_de_peste_10_ani(self):
        return self.age + 10
        # self.age += 10


iulia = Person("Albu", "Iulia", 50)
andrei = Person("Popescu", "Andrei", 30)

iulia.prezentare()
andrei.prezentare()
print(iulia.get_varsta_de_peste_10_ani())

print(iulia.age)