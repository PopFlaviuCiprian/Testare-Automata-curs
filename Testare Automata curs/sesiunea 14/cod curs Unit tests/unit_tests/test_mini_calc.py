
from app.mini_calc import MiniCalc

class TestMiniCalc:

    def setup_method(self):
        print("Se executa la inceput")
        self.calculator = MiniCalc(3, 2)

    def teardown_method(self):
        print("Se executa la final")


    def test_adunare(self):
        assert self.calculator.adunare() == 5, 'Error, Adunarea nu functioneaza corect'

    def test_scadere(self):
        assert self.calculator.scadere() == 1, 'Error, Scaderea nu functioneaza corect'

    def test_inmultire(self):
        assert self.calculator.inmultire() == 6, 'Error, Inmultirea nu functioneaza corect'

    def test_impartire(self):
        assert self.calculator.impartire() == 1.5, 'Error, Impartirea nu functioneaza corect'