
Feature: testing nustraweb

  Scenario: visit localhost and check
    Given we visit our localhost
    Then I see the tittle web Twitter top words finder

  
  Scenario Outline: Given the inputs below search a valid username pressing with the mouse
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press search
    Then the webpage content must be shown the word "concepto" 
    And with a frequency of "3" 
    And the word appears in these tweets "<List>"

    Examples: Input Variables
      |List                                                                                                                                                            |
      |['En tanto en cuanto nos den lo que es nuestro discutiremos el concepto con el fin de discutirlo', 'El concepto es el concepto', 'El concepto es el concepto']  |
      
  Scenario Outline: Given the inputs below search a valid username pressing the keyboard
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press enter
    Then the webpage content must be shown the word "sumachingún" 
    And with a frequency of "1" 
    And the word appears in these tweets "<List>"

    Examples: Input Variables
      |List                         |
      |['Esto es una sumachingún']  |
      
  Scenario: search username with empty value
    Given we visit our localhost
    When we press enter
    Then it should have no content
    
  Scenario: search invalid username 
    Given we visit our localhost
    And write username "manolocabezabolobolobolo"
    When we press search
    Then it should have no content
    
  Scenario: press reset without username written and without content 
    Given we visit our localhost
    When we press reset
    Then it should have no content
    And no element in checkbox
    
  Scenario: press reset with username written and without content 
    Given we visit our localhost
    And write username "LalindeALvaro"
    When we press reset
    Then it should have no content
    And no element in checkbox

  Scenario: press reset without username written and with content 
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press search
    And reset checkbox
    And we press reset
    Then it should have no content
    And no element in checkbox    
    
  Scenario: press reset with username written and with content 
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press search
    And we press reset
    Then it should have no content
    And no element in checkbox
