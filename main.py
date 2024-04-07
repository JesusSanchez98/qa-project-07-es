
import main
import selector
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:
    from_field = selector.from_field
    to_field = selector.to_field

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(data.address_from)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, to_address, from_address):
        self.set_from(data.address_from)
        self.set_to(data.address_to)

class Comfort:
    personal = selector.personal
    taxi = selector.taxi
    button_taxi = selector.button_taxi
    comfort_button = selector.comfort_button

    def __init__(self, driver):
        self.driver = driver

    def click(self):
        self.driver.find_element(*self.personal).click()

    def click_2(self):
        self.driver.find_element(*self.taxi).click()

    def click_button(self):
        self.driver.find_element(*self.button_taxi).click()
    def confort_tarif(self):
        self.driver.find_element(*self.comfort_button).click()

    def taxi_comfort(self):
        self.click()
        #self.click_2()
        self.click_button()
        self.confort_tarif()
        return "Comfort"

class Phone:

    button_phone = selector.button_phone
    phone_num = selector.phone_number
    button_Sig = selector.button_Sig
    Ath_code = selector.Ath_code
    button_confirmar = selector.button_confirmar

    def __init__(self, driver):
        self.driver = driver

    def click_phone(self):
        self.driver.find_element(*self.button_phone).click()

    def phone_box(self, phone_number):
        self.driver.find_element(*self.phone_num).send_keys(data.phone_number)

    def get_phone(self):
        return self.driver.find_element(*self.phone_num).get_property('value')

    def click_sig(self):
        self.driver.find_element(*self.button_Sig).click()

    def confirmar(self, codigo):
        self.driver.find_element(*self.Ath_code).send_keys(codigo)

    def btton_confirmar(self):
        self.driver.find_element(*self.button_confirmar).click()

    def phone_number(self, phone_number):
        self.click_phone()
        self.phone_box(phone_number)
        self.get_phone()
        self.click_sig()
        self.confirmar(retrieve_phone_code(self.driver))
        self.btton_confirmar()

class CreditCard:
    metodo_pago = selector.metodo_pago   #metodo_pago
    agregar_tarjeta = selector.agregar_tarjeta  #agregar_tarjeta
    numero = selector.numero_t   #numero_tarjeta
    codigo = selector.codigo           #añadir cogigo
    Atv_btton = selector.Atv_btton      #activar_agregar
    button_agregar = selector.button_agregar     #button_agregar
    button_cerrar = selector.button_cerrar       #button_cerrar

    def __init__(self, driver):
        self.driver = driver

    def click_met(self):
        self.driver.find_element(*self.metodo_pago).click()

    def add_card(self):
        self.driver.find_element(*self.agregar_tarjeta).click()

    def add_num_card(self, card_number):
        self.driver.find_element(*self.numero).send_keys(card_number)

    def add_code_card(self, card_code):
        self.driver.find_element(*self.codigo).send_keys(card_code)

    def click_Atv(self):
        self.driver.find_element(*self.Atv_btton).click()

    def click_aggr(self):
        self.driver.find_element(*self.button_agregar).click()

    def click_exit(self):
        self.driver.find_element(*self.button_cerrar).click()

    def credit_card(self):
        self.click_met()
        self.add_card()
        card_number = data.card_number
        self.add_num_card(card_number)
        sleep(1)
        card_code = data.card_code
        self.add_code_card(card_code)
        self.click_Atv()
        self.click_aggr()
        self.click_exit()
        return card_number, card_code

class MensajeConductor:

    scroll = selector.scroll
    mensaje = selector.mensaje
    mensaje_conductor = selector.mensaje_conductor

    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.scroll)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def send_massage(self,message_for_driver):
        self.driver.find_element(*self.mensaje_conductor).send_keys(data.message_for_driver)

    def massage(self,message_for_driver):
        self.send_massage(message_for_driver)

        return 'Muéstrame el camino al museo'

class MantasPanuelos:

    #Box = selector.Box
    Box_MP = selector.Box_MP
    Switch = selector.Switch

    def __init__(self, driver):
        self.driver = driver

    def Mantas_p(self):
        box_element = self.driver.find_element(*self.Box_MP)
        box_element.click()

        switch_element = self.driver.find_element(*self.Switch)
        switch_element.click()
        sleep(1)
        return "Mantas y pañuelos"

class Helado:

    add_cantidad = selector.add_cantidad
    counter = selector.counter

    def __init__(self, driver):
        self.driver = driver

    def click_helado(self):
        helado = self.driver.find_element(*self.add_cantidad)
        actions = ActionChains(self.driver)
        actions.double_click(helado).perform()

    def cantidad(self):
        return self.driver.find_element(*self.counter).text

    def cant_helado(self):
        self.click_helado()
        sleep(1)
        self.cantidad()

class PedirTaxi:

    btton_taxi = selector.btton_taxi

    def __init__(self, driver):
        self.driver = driver

    def click_taxi(self):
        self.driver.find_element(*self.btton_taxi).click()

    def pedir_tx(self):
        self.click_taxi()
        sleep(2)

