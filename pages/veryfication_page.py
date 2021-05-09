from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators_x_kom import VerificationOrder

class VeryficationPage(BasePage):

    def verify_cart_value(self):
        wait = WebDriverWait(self.driver, 40)
        value_cart = wait.until(EC.visibility_of_element_located(VerificationOrder.VERIFY_PRODUCT))
        go_delivery = wait.until(EC.element_to_be_clickable(VerificationOrder.GO_TO_DELIVERY))
        if value_cart.text[-1] != '0':
            go_delivery.click()
            print('Produkt został poprawnie dodany do koszyka!')
            print('Ilość produktów dodanych do koszyka: ' + value_cart.text[-1])
        else:
            print('Produkt nie może zostać dodany do Twojego koszyka!')
            print('Ilość produktów dodanych do koszyka: ' + value_cart.text[-1])

        assert value_cart.text[-1] >= '1'