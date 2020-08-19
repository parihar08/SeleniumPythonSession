Feature: OrangeHRM Logo

  Scenario: Logo presence on OrangeHRM Home Page

    Given Launch Chrome browser
    When Open OrangeHRM Home Page
    Then Verify that the logo present on page
    And Close Browser