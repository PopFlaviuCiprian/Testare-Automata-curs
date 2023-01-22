from app.dreptunghi import Dreptunghi


class TestDreptunghi:

    def setup_method(self):
        print("Se executa la inceput")
        self.dreptunghi = Dreptunghi(4,3,'alb')

    def teardown_method(self):
        print('Se executa la final')

    def test_descrie(self):
        assert self.dreptunghi.descrie() == (4,3,'alb'), 'Descrierea nu este corecta'

    def test_aria(self):
        assert self.dreptunghi.aria() == 12,'Aria nu se calculează corect'

    def test_perimetru(self):
        assert self.dreptunghi.perimetru() == 14, 'Perimetrul nu se calculează corect'

    def test_schimba_culoarea(self):
        self.dreptunghi.schimba_culoarea('verde')
        assert self.dreptunghi.culoare == 'verde', 'eroare verificare culoare'

