import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *


@given("acceder a la pagina web y logarse con cookies '{url}' '{cookiedefault}'")
def abrir_web_entrar_con_cookies(context, url, cookiedefault):
    context.behave_driver.get(url)
    context.behave_driver.maximize_window()
    cookies = pickle.load(open(f"C:/Users/adam/PycharmProjects/AppCrueUniversia/gestor/resources/cookies/{cookiedefault}", "rb"))
    for cookie in cookies:
        context.behave_driver.add_cookie(cookie)
        context.behave_driver.refresh()


@when('seleccionar chosen container')
def seleccionar_chosen_container(context):
    btnsearch_universities = context.behave_driver.find_element(By.XPATH, "//div[@class='form-group mr5']")
    btnsearch_universities.click()


@then("buscar universidad, seleccionar y desplegar universidad '{universidad}' '{cookieselect}'")
def buscar_desplegar_universidad(context, universidad, cookieselect):
    search_university = context.behave_driver.find_element(By.XPATH, "//input[@type='text']")
    search_university.send_keys(universidad)
    search_university.send_keys(Keys.ENTER)
    search_university.send_keys(Keys.ENTER)
    cookies = pickle.load(open(f"C:/Users/adam/PycharmProjects/AppCrueUniversia/gestor/resources/cookies/{cookieselect}", "rb"))
    for cookie in cookies:
        context.behave_driver.add_cookie(cookie)
        context.behave_driver.refresh()

    university = WebDriverWait(context.behave_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Universidad']")))
    context.behave_driver.execute_script("arguments[0].click();", university)


@then('ir a configuracion de la integracion')
def configuracion_integracion(context):
    confi_integracion = WebDriverWait(context.behave_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Configuración de la integración']")))
    context.behave_driver.execute_script("arguments[0].click();", confi_integracion)


@then('probar usuarios en servicios integrados')
def test_servicio_integrado(context):
    ser_integ = WebDriverWait(context.behave_driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, "//span[normalize-space()='Configuración de la integración']//following::a")))
    context.behave_driver.execute_script("arguments[0].click();", ser_integ)
    ser_integ_email = context.behave_driver.find_element(By.XPATH, "//input[@id='target_user']")
    for row in context.table:
        ser_integ_email.send_keys(row["email"])

        btn_test = WebDriverWait(context.behave_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH,  "//button[@id='test_directory_url']")))
        btn_test.click()

        endpoint_ok = WebDriverWait(context.behave_driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='test_explanation']")))
        assert endpoint_ok.text == "OK: El endpoint devuelve un resultado correcto"
        ser_integ_email.clear()