Feature: Facebook Login Flow
  As a user
  I want to log in to Facebook
  So that I can access my account

  Scenario: Successful login
    Given I am on the Facebook login page
    When I enter valid username and password
    And I click the "Log In" button
    Then I should be logged in successfully
    And I should see my profile page

  Scenario: Unsuccessful login
    Given I am on the Facebook login page
    When I enter invalid username and password
    And I click the "Log In" button
    Then I should see an error message
    And I should still be on the login page