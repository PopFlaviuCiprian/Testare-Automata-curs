from browser import Browser
from selenium.webdriver.common.by import By


class SecurePage(Browser):

    AFISARE_SUCCES_LOGIN = (By.CLASS_NAME, "subheader")
    LOGOUT_BTN = (By.XPATH, "//i[@class='icon-2x icon-signout']")

    def loghin_secure(self):
        self.driver.get("https://the-internet.herokuapp.com/secure")

    # verificare daca mesajul e corect si e displayed
    def display_succes_message(self):
        actual_message = self.driver.find_element(*self.AFISARE_SUCCES_LOGIN).text
        expected_message = "Welcome to the Secure Area. When you are done click logout below."
        assert actual_message == expected_message, f"Mesajul afisat este incorrect"

    # logout
    def logout_secure(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()
