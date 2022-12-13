from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage(Browser):

    LOGHIN_BUTTON = (By.CLASS_NAME, 'ico-login')

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((by, selector)))

    def click_loghin_button(self):
        self.driver.find_element(*self.LOGHIN_BUTTON).click()

