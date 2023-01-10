Feature: Check the Login functionality

  # se ruleaza inainte de fiecare scenariu
  Background:
    Given login: I am a user on the login page

  @login
  Scenario: Login is successful with valid credentials
    When login: I fill in an email "test_automation_ta25@mailinator.com"
    When login: I fill in a password "Test1234"
    When login: I click the login button
    Then base: I can see my account in the menu



