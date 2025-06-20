Feature: Facebook Login
  As a user
  I want to try to login to facebook.com with invalid credentials
  So that I can verify the error handling of the login functionality

Scenario: Invalid Credentials
  Given I am on the facebook.com login page
  When I enter "satyam.singhania123@gmail.com" as username
  And I enter "satyam123" as password
  And I click the login button
  Then I should see an error message
  And I should not be logged in