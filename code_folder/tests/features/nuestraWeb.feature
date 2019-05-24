
Feature: testing nustraweb

  Scenario: visit localhost and check
    Given we visit our localhost
    Then I see the tittle web Twitter top words finder

  Scenario: search a valid username
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press search
    Then it should have a textfield "{"concepto": "3", "t": "2", "eh": "2", "aquí": "1", "hostias": "1", "hondonadas": "1", "haber": "1", "van": "1", "si": "1", "bien": "1", "llevarnos": "1", "vamos": "1", "criatura": "1", "vicio": "1", "alardes": "1", "formas": "1", "idiota": "1", "payaso": "1", "abogao": "1", "dicho": "1"}"

  Scenario: search a valid username
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press enter
    Then it should have a textfield "{"concepto": "3", "t": "2", "eh": "2", "aquí": "1", "hostias": "1", "hondonadas": "1", "haber": "1", "van": "1", "si": "1", "bien": "1", "llevarnos": "1", "vamos": "1", "criatura": "1", "vicio": "1", "alardes": "1", "formas": "1", "idiota": "1", "payaso": "1", "abogao": "1", "dicho": "1"}"

  Scenario: search username with wmpty checkbox
    Given we visit our localhost
    When we press enter
    Then it should have no body
    
  Scenario: search invalid username 
    Given we visit our localhost
    And write username "manolocabezabolobolobolo"
    When we press search
    Then it should have no body
    
  Scenario: press reset without checkbox and without body 
    Given we visit our localhost
    When we press reset
    Then it should have no body
    And no element in checkbox
    
  Scenario: press reset with checkbox and without body 
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press reset
    Then it should have no body
    And no element in checkbox

  Scenario: press reset without checkbox and with body 
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press search
    And reset checkbox
    And we press reset
    Then it should have no body
    And no element in checkbox    
    
  Scenario: press reset with checkbox and with body 
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press search
    And we press reset
    Then it should have no body
    And no element in checkbox