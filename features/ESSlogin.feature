Feature: OrangeHRM ESS login
  As an ESS user, I want to login to the portal
  So that I can access my dashboard page.

  Scenario: Verify login with valid ESS credentials
    Given the user launches the OrangeHRM portal
#    When the user enters credentials for "ess_user1" //using users.json
    When the user enters username "ravimb1" and password "RaviM1B1"
    And clicks on the login button
    Then the user should be redirected to the dashboard page