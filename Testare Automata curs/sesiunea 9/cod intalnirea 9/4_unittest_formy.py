import unittest         # importarea librariei unittest care va face programul grupat in bucati rulabile individual
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class Test(TestCase):

    # elementele din pagina pe care o testam
    # in loc sa le repetam in fiecare test, le trecem aici o singura data si dupa le refolosim
    FORM_LINK = (By.LINK_TEXT, "Form")          # -> tuple, vezi liniile 19-20
    SUBMIT_BUTTON = (By.XPATH, "//a[@role='button']")
    MIDDLE_NAME = (By.XPATH, 'middle-name')

    # se ruleaza inainte de fiecare test si are rolul de a face un setup pt teste
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://formy-project.herokuapp.com/")
        # * tuple unpacking - se ia valoarea din tuple si se da ca argument functiei
        self.chrome.find_element(*self.FORM_LINK).click()
        # daca nu facem unpacking functia probabil ar arata asa find_element((By.LINK_TEXT, "Form"))
        # cand facem unpacking functie arata asa find_element(By.LINK_TEXT, "Form")

    # se ruleaza dupa fiecare test si are rolul de a face un cleanup dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    # metodele pentru teste, trebuie neaparat sa inceapa cu test
    # altfel unittest nu va sti sa recunoasca ca e un test si va crede ca e o simpla metoda
    def test_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://formy-project.herokuapp.com/form"
        assert actual_url == expected_url, f"Url este incorect"

    @unittest.skip      # unittest.skip este un decorator care instruieste sistemul sa sara peste testul respectiv
    def test_page_title(self):
        actual_title = self.chrome.title
        expected_title = "Formy"
        self.assertEqual(actual_title, expected_title, "Title incorrect")

    def test_submit_button_text(self):
        actual_button = self.chrome.find_element(*self.SUBMIT_BUTTON).text
        expected_button = "Submit"
        self.assertEqual(actual_button, expected_button, "Text button is incorrect")

    def test_button_displayed(self):
        btn = self.chrome.find_element(*self.SUBMIT_BUTTON)
        self.assertTrue(btn.is_displayed(), 'Butonul nu este displayed')

    def test_button_attribute(self):
        actual = self.chrome.find_element(*self.SUBMIT_BUTTON).get_attribute('class')
        expected = 'btn btn-lg btn-primary'
        self.assertEqual(actual, expected, 'The attribute value is not correct')

    # varianta incorecta
    def test_elem_not_displayed_v1(self):
        # ai zice ca merge ca verificam asa, dar nu
        # pentru ca intoarce eroare ca oricum nu gaseste elementul pe find, nu e corect
        elem = self.chrome.find_element(*self.MIDDLE_NAME)
        self.assertFalse(elem.is_displayed(), 'Este displayed')

    # varianta corecta, facem cu find_elements care va returna o lista
    # in cazul in care elementul chiar nu exista se va returna o lista goala
    # si atunci verificam ca lungimea listei este 0
    def test_elem_not_displayed_v2(self):
        middle_names = self.chrome.find_elements(*self.MIDDLE_NAME)
        print(f'Lista returnata este {middle_names}')
        self.assertTrue(len(middle_names) == 0, 'Cel putin un element a fost gasit')

    # varianta corecta
    # caputram eroarea de NoSuchElementException
    def test_elem_not_displayed_v3(self):
        try:
            self.chrome.find_element(*self.MIDDLE_NAME)
        except NoSuchElementException:
            # print("Nu s-a gasit elementul, e ok")
            pass

        # waits pe url
    def test_url_waits(self):
        self.chrome.find_element(*self.SUBMIT_BTN).click()
        # asteptam ca fostul url sa se schimbe
        WebDriverWait(self.chrome, 5).until(EC.url_changes('https://formy-project.herokuapp.com/form'))
        # asteptam ca noul url sa contina
        WebDriverWait(self.chrome, 5).until(EC.url_contains('/thanks'))
        # asteptam ca noul url sa fie exact
        WebDriverWait(self.chrome, 5).until(EC.url_to_be('https://formy-project.herokuapp.com/thanks'))

        # daca in 5 secunde nu ajungem pe url corect putem
        try:
            WebDriverWait(self.chrome, 5).until(EC.url_contains('/thanks'))
        except TimeoutException:
            self.assertTrue(False, 'Am asteptat 5 secunde dar url nu se incarca sau nu e corect')


