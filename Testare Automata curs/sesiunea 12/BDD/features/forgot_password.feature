Feature: Check the forgot password functionality

  @smoke
  Scenario: Invalid email format validation message
    Given login: I am a user on the login page
    When login: I click on the forgot password link
    When forgot_pass: I fill in my email "my_email@"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Wrong email"
    