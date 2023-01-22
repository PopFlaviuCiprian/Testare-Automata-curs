
class Dreptunghi:

    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        return self.lungime, self.latime, self.culoare

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return (self.lungime * 2) + (self.latime * 2)

    def schimba_culoarea(self,verde):
        self.culoare = verde
        return self.culoare

