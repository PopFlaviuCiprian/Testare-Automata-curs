from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Loghin_page(BasePage):
    EMAIL_IMPUT = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGHIN_BUTTON = (By.CLASS_NAME, "login-button")
    FORGOT_PASSWORD = (By.LINK_TEXT, "Forgot password?")

    def navighate_to_loghin_page(self):
        self.driver.get("https://demo.nopcommerce.com/loghin")

    # set email
    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_IMPUT).send_keys(email)

    # set password
    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_loghin_button(self):
        self.driver.find_element(*self.LOGHIN_BUTTON).click()

    def click_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD).click()
