Feature: Instagram Login
  As a user
  I want to log in to Instagram
  So I can access my account

  Scenario: Successful login
    Given I am on the Instagram login page
    When I enter valid credentials
    Then I should be logged in successfully
    And I should see my account profile picture