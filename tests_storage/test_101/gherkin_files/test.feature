Feature: Facebook Login
  As a user
  I want to login to Facebook
  So that I can access my account

Scenario: Login with invalid credentials
  Given I am on facebook.com
  When I enter "satyam.singhania123@gmail.com" and "Satyam123" as login credentials
  Then I should see an error message