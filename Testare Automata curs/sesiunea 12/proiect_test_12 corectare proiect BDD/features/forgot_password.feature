Feature: Check the Forgot password functionality

  Background:
    Given login: I am a user on the login page
    When login: I click on the forgot password link

  @smoke
  Scenario: Check validation error message when email is invalid format
    When forgot_pass: I fill in my email "my_email@"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Wrong email"


  @forgot_pass
  Scenario: Check validation error message when email is empty
    When forgot_pass: I make sure the email input is cleared
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Enter your email"

  @multiple_values_email @forgot_pass
  Scenario Outline: Check various email validations
    When forgot_pass: I fill in my email "<email>"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "<expected_error>"
    Then forgot_pass: I verify the notification "<expected_notif>"

    Examples:
    | email          |  expected_error   |  expected_notif     |
    | test           |  Wrong email      |   None              |
    | test@          |  Wrong email      |   None              |
    | test.com       |  Wrong email      |   None              |
    | test@te.       |  Wrong email      |   None              |
    | test@test.com  |  None             |   Email not found.  |