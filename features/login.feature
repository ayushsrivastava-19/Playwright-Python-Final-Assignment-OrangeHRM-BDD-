Feature: OrangeHRM Login Functionality
  As an admin user, I want to login to the portal
  So that I can access dashboard page.

  #Happy Flow
  Scenario: Verify login with valid admin credentials
    Given the user launches the OrangeHRM portal
    When the user enters username "Admin" and password "admin123"
    And clicks on the login button
    Then the user should be redirected to the dashboard page

#    Examples:
#      | username | password |
#      | Admin    | admin123 |

  #Negative Flow
  Scenario Outline: Verify login with invalid credentials
    Given the user launches the OrangeHRM portal
    When the user enters username "<username>" and password "<password>"
    And clicks on the login button
    Then the user should see error message "Invalid credentials"

    Examples:
      | username | password |
      | adminnn  | xxxxxxxx |
      | aadmin   | admin123 |
      | Admin    | aadmin45 |

