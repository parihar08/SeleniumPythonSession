Feature: OrangeHRM Logo

  Scenario: Login to OrangeHRM with valid parameters

    Given I Launch Chrome browser
    When Open OrangeHRM Homepage
    And Enter username "admin" and password "admin123"
    And Click on Login button
    Then User logged on to Dashboard Page