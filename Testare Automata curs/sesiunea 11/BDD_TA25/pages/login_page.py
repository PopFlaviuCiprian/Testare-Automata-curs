from browser import Browser
from selenium.webdriver.common.by import By


class LoginPage(Browser):

    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot password?")


    def navigate_to_login_page(self):
        self.driver.get("https://demo.nopcommerce.com/login")

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, pswrd):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(pswrd)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

