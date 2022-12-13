from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    EMAIL_IMPUT =(By.ID, "Email")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Recover']")
    EMAIL_ERROR_MESSAGE = (By.ID, "Email-error")
    NOTIFICATION_MESSAGE = (By.XPATH, "//p[@class='content']")

    def navigate_to_forgot_password_page(self):
        self.driver.get("https://demo.nopcommerce.com/passwordrecovery")

    def set_email(self,email):
        self.driver.find_element(*self.EMAIL_IMPUT).send_keys(email)

    def click_recover_button(self):
        self.driver.find_element(*self.RECOVER_BUTTON).click()

    def verify_email_error_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.EMAIL_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message == expected_message, f'Error, the message is incorrect, expected {expected_message}, actual {actual_message}'

    def verify_notification_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.NOTIFICATION_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message == expected_message, f'Error, the message is incorrect, expected {expected_message}, actual {actual_message}'




