Feature: Scenario Background Feature to execute common steps before every scenario

#Scenario Background helps to reduce the size of feature file

  Background: Common Steps

    Given I launch browser
    When I open application
    And Enter valid username and password
    And Click on login

  Scenario: Login to HRM Application

    #Given I launch browser
    #When I open application
    #And Enter valid username and password
    #And Click on login
    Then User must login to the Dashboard Page

  Scenario: Search User

    #Given I launch browser
    #When I open application
    #And Enter valid username and password
    #And Click on login
    When Navigate to search page
    Then Search page should display

  Scenario: Advanced Search User

    #Given I launch browser
    #When I open application
    #And Enter valid username and password
    #And Click on login
    When Navigate to advanced search page
    Then Advanced search page should display