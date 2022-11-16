Feature: AppCrue Universia

  @generar_cookies
  Scenario Outline: Add cookies
    Given acceder '<urls>'
    When esperar 90 segundos para logarte manualmente
    Then guardar cookies una vez logado
    Examples:
      | urls                                          |
      | https://pre.appuniversitaria.idsant.com/login |


