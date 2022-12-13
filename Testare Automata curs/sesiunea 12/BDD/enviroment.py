from browser import Browser
from pages.login_page import Login_page
from pages.forgot_password_page import ForgotPasswordPage


def before_all(context):
    context.browser = Browser()
    context.login_page = Login_page()
    context.forgot_password_page = ForgotPasswordPage()


def after_all(context):
    context.browser.close()