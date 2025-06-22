Feature: Facebook Login
  As a user
  I want to login to Facebook
  So I can access my account

Scenario: Successful Login
  Given I am on the Facebook login page
  When I enter valid username and password
  Then I should be logged in successfully
  And I should see my profile page

Scenario: Invalid Username
  Given I am on the Facebook login page
  When I enter invalid username and valid password
  Then I should see an error message
  And I should not be logged in

Scenario: Invalid Password
  Given I am on the Facebook login page
  When I enter valid username and invalid password
  Then I should see an error message
  And I should not be logged in

Scenario: Empty Credentials
  Given I am on the Facebook login page
  When I enter empty username and password
  Then I should see an error message
  And I should not be logged in