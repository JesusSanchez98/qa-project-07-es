import main
from time import sleep
import data
from selenium import webdriver

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.routes_page = main.UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        sleep(1)
        routes_page = main.UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.set_route(address_from, address_to)
        sleep(1)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_slect_comfort(self):
        taxi = main.Comfort(self.driver)
        select_taxi = taxi.taxi_comfort()
        sleep(1)
        answerd = "Comfort"
        assert answerd == select_taxi

    def test_phone_number(self):
        phone = main.Phone(self.driver)
        num = data.PHONE_NUMBER
        phone.phone_number(num)
        get_phone = phone.get_phone()
        sleep(1)
        expect_phone = num
        assert get_phone == expect_phone

    def test_credit_card(self):
        card = main.CreditCard(self.driver)
        number, code = card.credit_card()
        expec_number = data.CARD_NUMBER
        expec_code = data.CARD_CODE
        assert number == expec_number
        assert code == expec_code

    def test_message_for_driver(self):
        message_driver = main.MensajeConductor(self.driver)
        check_message = message_driver.massage(message_driver)
        message_to_send = "Muéstrame el camino al museo"
        assert check_message == message_to_send

    def test_mantas_pañuelos(self):
        mantas_pañuelos = main.MantasPanuelos(self.driver)
        check_box = mantas_pañuelos.Mantas_p()
        expec_answerd = "Mantas y pañuelos"
        assert check_box == expec_answerd

    def test_helado(self):
        ice = main.Helado(self.driver)
        ice.cant_helado()
        counter = ice.cantidad()
        assert counter == "2"

    def test_pedir_taxi(self):
        taxi = main.PedirTaxi(self.driver)
        taxi.pedir_tx()
        expec_answerd = 'Pedir un taxi\nEl recorrido será de 1 kilómetros y se hará en 1 minutos'
        text = self.driver.find_element(*taxi.btton_taxi).text
        assert expec_answerd == text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
