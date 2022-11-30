import unittest
from time import sleep
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login(unittest.TestCase):
    H2_ELEMENT = (By.XPATH,'//h2')
    LOGIN_BUTTON = (By.XPATH,"//*[@id='login']/button/i")
    HREF_LINK = (By.XPATH, '//a[@href="http://elementalselenium.com/"]')
    ERROR_MESSAGE = (By.ID, "flash")
    PASSWORD = (By.ID, 'password')
    USER_NAME = (By.ID, 'username')
    CLOSE_ERROR_LOGHIN = (By.CLASS_NAME, 'close')
    LABEL_LIST = (By.XPATH, '//label')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
    SUCCES_MESSAGE = (By.XPATH, '//div[@class="flash succes"]')
    H4_ELEMENT = (By.XPATH, '//h4[@class="subheader"]' )

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(15)
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.find_element(By.LINK_TEXT, "Form Authentication").click()

    def tearDown(self):
        self.chrome.quit()

    #@unittest.skip
    def test_url(self):  # test 1
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        assert  actual_url == expected_url, f"Url incorect"

    #@unittest.skip
    def test_page_title(self):  # test 2
        actual_title = self.chrome.title
        expected_title = "The Internet"
        self.assertEqual(actual_title,expected_title, 'Titlul paginii este incorect')

    #@unittest.skip
    def test_element(self): # test 3
        actual_element = self.chrome.find_element(*self.H2_ELEMENT).text
        expected_element = "Login Page"
        self.assertEqual(actual_element,expected_element, f"Denumirea elementului este {actual_element}")

    #@unittest.skip
    def test_login_displayed(self):  # test 4
        actual = self.chrome.find_element(*self.LOGIN_BUTTON).text
        expected_button = "Login"
        self.assertEqual(actual,expected_button,"Text incorect pentru butonul Login")

    #@unittest.skip
    def test_href_link(self): # test 5
        actual_link = self.chrome.find_element(*self.HREF_LINK).get_attribute('href')
        assert actual_link == 'http://elementalselenium.com/', f'Link gresit'

    #@unittest.skip
    def test_mesaj_alerta(self): # test 6
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')

    #@unittest.skip
    def test_mesaj_eroare(self): # test 7
        self.chrome.find_element(*self.USER_NAME).send_keys('cipri')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual_message = self.chrome.find_element(*self.ERROR_MESSAGE).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual_message, 'Error message text is incorrect')
        sleep(5)

    #@unittest.skip
    def test_loghin_error_close(self): # test 8
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.CLOSE_ERROR_LOGHIN).click()
        sleep(4)
        try:
            self.chrome.find_element(*self.CLOSE_ERROR_LOGHIN)
        except NoSuchElementException:
            print("The text is not visible on the page! It's ok")

    #@unittest.skip
    def test_label_list(self): # test 9
        lista = self.chrome.find_elements(*self.LABEL_LIST)
        i = 0
        correct_ussername = False
        correct_password = False
        while i<len(lista):
            if lista[i].text == 'Username':
                correct_ussername = True
            elif lista[i].text == 'Password':
                correct_password = True
            i += 1
        assert correct_ussername ==True
        assert correct_password == True

    @unittest.skip
    def test_login_secure(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        url_dupa_logare = self.chrome.current_url
        self.assertTrue("secure" in url_dupa_logare, 'Noul url nu contine secure')
        actual = WebDriverWait(self.chrome,10).until(EC.presence_of_element_located(self.SUCCES_MESSAGE))
        assert actual.is_displayed() == True, 'Elementul flash success nu este afisat'
        self.assertIn('secure area!', actual.text, "URL-ul este incorrect")

    #@unittest.skip
    def test_loghin_logout(self): #test 11
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        sleep(2)
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        sleep(2)
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(3)
        loghin_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/secure"
        assert loghin_url == expected_url, f"Url incorect"
        sleep(3)
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        logout_url = self.chrome.current_url
        expected_logout_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(logout_url,expected_logout_url, f'Pagina invalida')
        sleep(7)

    #def test_brute_force_pass(self):
        parole = self.chrome.find_element(*self.H4_ELEMENT).text.split()
        url = None
        for password in parole:
            self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
            self.chrome.find_element(*self.PASSWORD).send_keys(password)
            self.chrome.find_element(*self.LOGIN_BUTTON).click()
            expected_url = "https://the-internet.herokuapp.com/secure"
            url = self.chrome.current_url
            if "secure" in url:
                print(f'Parola secreta este {password}')
                break
            else:
                print("Nu am reusit sa gasesc parola. Continuam cautarea")
        assert "secure" in url, "Eroare: parola nu a fost gasita"
