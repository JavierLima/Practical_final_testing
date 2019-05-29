
Feature: testing nustraweb

  Scenario: visit localhost and check
    Given we visit our localhost
    Then I see the tittle web Twitter top words finder

  Scenario: search a valid username
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press search
    Then the webpage content must be shown the word "concepto" with a 
          frequency of "3" that appears in these tweets "['En tanto en cuanto nos den lo que es nuestro discutiremos el concepto con el fin de discutirlo', 'El concepto es el concepto', 'El concepto es el concepto']"

  Scenario: search a valid username
    Given we visit our localhost
    And write username "LalindeAlvaro"
    When we press enter
    Then the webpage content must be shown "{'concepto': {'count': '3', 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos el concepto con el fin de discutirlo', 'El concepto es el concepto', 'El concepto es el concepto']}, 'eh': {'count': '2', 'tweetsContaining': ['Los hijos estudiando la carrera en los mejores colegios de Kanfort con aprovechamiento eh Ay Carmiña tú en Cambados y yo en el País Vasco', 'Vamos a llevarnos bien porque si no van a haber hondonadas de hostias aquí eh']}, 'digo': {'count': '2', 'tweetsContaining': ['El señor Villambrosa que es un gentelmán me dijo que viniera a solucionar esto con pacifismo así que A lo mismo que le digo una cosa le digo la otra y B se levanta y pone el arma sobre la mesa y cuidao tocándose las partes que igual te viene la C', 'El señor Villambrosa que es un gentelmán me dijo que viniera a solucionar esto con pacifismo así que A lo mismo que le digo una cosa le digo la otra y B se levanta y pone el arma sobre la mesa y cuidao tocándose las partes que igual te viene la C']}, 'sumachingún': {'count': '1', 'tweetsContaining': ['Esto es una sumachingún']}, 'cuanto': {'count': '1', 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos el concepto con el fin de discutirlo']}, 'den': {'count': '1', 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos el concepto con el fin de discutirlo']}, 'discutiremos': {'count': '1', 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos el concepto con el fin de discutirlo']}, 'fin': {'count': '1', 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos el concepto con el fin de discutirlo']}, 'discutirlo': {'count': '1', 'tweetsContaining': ['En tanto en cuanto nos den lo que es nuestro discutiremos el concepto con el fin de discutirlo']}, 'disculpe': {'count': '1', 'tweetsContaining': ['Disculpe agente se refiere a antes en el tiempo o antes en el espacio']}}"

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
