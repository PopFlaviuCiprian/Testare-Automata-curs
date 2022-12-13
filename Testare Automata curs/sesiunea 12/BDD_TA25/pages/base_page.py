from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


# in aceasta pagina punem toate metodele care sunt utile in orice pagina
# si nu neaparat specifice doar unei pagini

class BasePage(Browser):

    LOGIN_BUTTON = (By.CLASS_NAME, "ico-login")
    MY_ACCOUNT = (By.LINK_TEXT, 'My account')

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((by, selector)))

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def verify_my_account_is_displayed(self):
        sleep(3)
        actual = self.driver.find_element(*self.MY_ACCOUNT)
        assert actual.is_displayed() is True, f'My account is not displayed in the menu'