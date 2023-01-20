from app.dreptunghi import Dreptunghi


class TestDreptunghi:

    def setup_method(self):
        print("Se executa la inceput")
        self.dreptunghi = Dreptunghi(4,3,'alb')

    def teardown_method(self):
        print('Se executa la final')

    def test_descrie_lungime(self):
        assert self.dreptunghi.descrie(),'Lungimea nu este corecta '

    def test_descrie_latime(self):
        assert self.dreptunghi.descrie(), 'Latimea nu este corecta'

    def test_descrie_culoare(self):
        assert self.dreptunghi.descrie(), 'Culoarea nu este buna'

    def test_aria(self):
        assert self.dreptunghi.aria() == 12,'Aria nu se calculează corect'

    def test_perimetru(self):
        assert self.dreptunghi.perimetru() == 14, 'Perimetrul nu se calculează corect'

    def test_schimba_culoarea(self):
        assert self.dreptunghi.descrie(), 'eroare verificare culoare'

