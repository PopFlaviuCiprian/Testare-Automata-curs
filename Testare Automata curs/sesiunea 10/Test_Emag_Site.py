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

class Emag(unittest.TestCase):

    CAUTARE_PRODUS = (By.ID, 'searchboxTrigger')
    APASA_SEARCH = (By.XPATH, '//i[@class="em em-search"]')

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(15)
        self.chrome.get("https://www.emag.ro/")
        self.chrome.find_element(By.NAME, "query").send_keys('telefoane')
        self.chrome.find_element(*self.APASA_SEARCH).click()


    def tearDown(self):
        self.chrome.quit()

    def test_cautare_produs(self):
        actual_url = self.chrome.current_url
        self.chrome.find_element(*self.APASA_SEARCH).click()
        sleep(3)

    #@unittest.skip
    def test_url_nou(self):  # test 1
        actual_url = self.chrome.current_url
        expected_url = "https://www.emag.ro/search/telefoane?ref=effective_search"
        assert actual_url == expected_url, f"Url incorect"
        sleep(2)

    def test_titlu_pagina(self):
        self.chrome.current_url
        actual_title = self.chrome.title
        expected_title = 'Cautare Telefoane - Descopera Oferta - eMAG.ro'
        self.assertEqual(actual_title, expected_title, 'Titlul paginii este incorect')



