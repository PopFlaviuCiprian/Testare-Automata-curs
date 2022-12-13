from behave import *

@given('login: I am a user on the login page')
def step_impl(context):
    context.login_page.navighate_to_login_page()

@when('login: I click on the forgot password link')
def step_impl(context):
    context.login_page.click_forgot_password_link()

@when('login: I fill in an email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)