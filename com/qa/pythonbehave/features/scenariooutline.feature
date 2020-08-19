Feature: OrangeHRM Logo

  Scenario Outline: Login to OrangeHRM with multiple parameters

    Given I Launch Chrome browser
    When Open OrangeHRM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on Login button
    Then User logged on to Dashboard Page

    Examples:

      | username   | password |
      |   admin    | admin123 |
      |   admin123 | admin    |
      |   adminxyz | admin123 |
      |   admin    | adminxyz |