Feature: OrangeHRM Login
  As an admin user, I want to login to the portal
  So that I can access dashboard page.

  Scenario: Verify login with valid admin credentials
    Given the user launches the OrangeHRM portal
    When the user enters username "<username>" and password "<password>"
    And clicks on the login button
    Then the user should be redirected to the dashboard page

    Examples:
      | username | password |
      | Admin    | admin123 |
      |