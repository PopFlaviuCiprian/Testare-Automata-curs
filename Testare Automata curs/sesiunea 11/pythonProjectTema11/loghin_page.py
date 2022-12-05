from browser import Browser
from selenium.webdriver.common.by import By

class LoghinPage(Browser):
    USSER = (By.ID, "username")
    PASS =(By.ID, "password")
    LOGHIN_BTN = (By.LINK_TEXT, "Login")

    # navigam catre link
    def go_to_logh_page(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    # introducem user
    def intro_user(self):
        self.driver.find_element(*self.USSER).send_keys("tomsmith")

    # intrducem parola
    def intro_pass(self):
        self.driver.find_element(*self.PASS).send_keys("SuperSecretPassword!")

    # loghin pe site
    def logare_site(self):
        self.driver.find_element(*self.LOGHIN_BTN).click()