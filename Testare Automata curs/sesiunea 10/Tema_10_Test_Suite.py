import unittest
import HtmlTestRunner
from Tema9 import Login
from Test_Emag_Site import Emag


class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_to_run = unittest.TestSuite()

        test_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Emag)
            # aici putem adauga mai multe teste
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Primul meu raport',
            report_name= 'Raportul Suita teste'
        )
        runner.run(test_to_run)