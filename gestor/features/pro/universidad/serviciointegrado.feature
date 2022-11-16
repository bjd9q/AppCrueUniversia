Feature: AppCrue Universia

  @f1s1
  Scenario Outline: Test servicios integrados
    Given acceder a la pagina web y logarse con cookies '<url>' '<cookiedefault>'
    When seleccionar chosen container
    Then buscar universidad, seleccionar y desplegar universidad '<universidad>' '<cookieselect>'
    Then ir a configuracion de la integracion
    And probar usuarios en servicios integrados
      |email                    |
      |appcrueempleado@cunef.edu|
      |alumnoprueba@cunef.edu   |
    Examples:
      | url                                           | cookiedefault     | universidad        |  cookieselect             |
      | https://pre.appuniversitaria.idsant.com/login | cookiesPRE.pkl    | CUNEF: CUNEF       |  cunefprecookies.pkl      |

