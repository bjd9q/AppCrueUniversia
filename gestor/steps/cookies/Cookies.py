import pickle
import time
from behave import *


@given("acceder '{urls}'")
def abrir_web(context, urls):
    context.behave_driver.get(urls)


@when("esperar 90 segundos para logarte manualmente")
def espera_logado_manual(context):
    print(context)


@then("guardar cookies una vez logado")
def guardar_cookies(context):
    print(context)
    #                                            nombre de file de cookie(nombre + entorno + rol de usuario de panel)
    #                                                          ^
    #                                                          |
    #pickle.dump(context.behave_driver.get_cookies(), open("cookiesPreUniadmin.pkl", "wb"))
