Feature: Facebook Login
  As a user
  I want to login to Facebook
  So that I can access my account

Scenario: Valid Credentials
  Given I am on the Facebook login page
  When I enter valid username and password
  Then I should be logged in successfully

Scenario: Invalid Credentials
  Given I am on the Facebook login page
  When I enter invalid username and password
  Then I should see an error message

Scenario: Empty Credentials
  Given I am on the Facebook login page
  When I enter empty username and password
  Then I should see an error message