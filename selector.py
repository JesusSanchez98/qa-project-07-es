from selenium.webdriver.common.by import By


# class UrbanRoutesPage
from_field = (By.ID, 'from')
to_field = (By.ID, 'to')

#class confort
personal = (By.XPATH, "//div[@class='mode' and text()='Personal']")
taxi = (By.XPATH, "//div[@class='types-container']//div[contains(@class, 'type active') and .//img[contains(src, '/static/media/taxi-active.b0be3054.svg')]]")
button_taxi = (By.CSS_SELECTOR, 'button.button.round')
comfort_button = (By.XPATH, "//div[@class='tariff-picker shown']//div[@class='tariff-cards']//div[contains(@class, 'tcard')]//div[@class='tcard-title' and text()='Comfort']/..")

#class Phone
button_phone = (By.CLASS_NAME, 'np-button')
phone_number = (By.ID, 'phone')
button_Sig = (By.XPATH, "//button[@class='button full' and text() = 'Siguiente']")
Ath_code = (By.ID, 'code')
button_confirmar = (By.XPATH, "//button[@class='button full' and text() = 'Confirmar']")

#class CreditCard
metodo_pago = (By.XPATH, "//div[@class= 'pp-button filled']")
agregar_tarjeta = (By.XPATH, "//div[@class= 'pp-title' and text()= 'Agregar tarjeta']")
numero_tarjeta = (By.ID, 'number')
codigo = (By.XPATH, "//div[@class='card-code-input']//input[@id= 'code']")
Atv_btton = (By.XPATH, "//div[@class='pp-buttons']")
button_agregar = (By.XPATH, "//button[@class='button full' and text()='Agregar']")
button_cerrar = (By.XPATH, '//*[@id="root"]/div/div[@class="payment-picker open"]/div[@class="modal"]/div[@class="section active"]/button')

#class MensajeConductor
scroll = (By.CLASS_NAME, 'workflow-subcontainer')
mensaje = (By.XPATH, "//div[@class= 'input-container']//div[@class='label'][contains(text(), 'Mensaje para el conductor')]")
mensaje_conductor = (By.XPATH, "//div[@class='input-container']/input[@id= 'comment']")

#Class MantasyPañuelos
Box_MP = (By.XPATH, "//div[@class='r-sw-container']")
Switch = (By.XPATH, "//div[@class='switch']//span[@class='slider round']")

#class Helado
add_cantidad = (By.CLASS_NAME, 'counter-plus')
counter = (By.CLASS_NAME, 'counter-value')

#class BuscarTaxi
btton_taxi = (By.XPATH, "//button[@class='smart-button' and span[@class='smart-button-main' and text() = 'Pedir un taxi']]")
