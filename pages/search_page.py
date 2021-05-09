from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from locators.locators_x_kom import SearchEngineLocators
from locators.locators_x_kom import AddToCartLocators

class SearchPage(BasePage):

    def verify_search_result(self):
        try:
            result = self.driver.find_element(*SearchEngineLocators.NO_SEARCH_RESULTS).get_attribute('textContent')
            complement = self.driver.find_element(*SearchEngineLocators.RESULT_COMPLEMENT).get_attribute('textContent')
            assert 'Brak wyników dla ' + complement + '.' not in result
            print(result)
        except NoSuchElementException:
            amount = self.driver.find_element(*SearchEngineLocators.AMOUNT_SEARCH_RESULTS).get_attribute('textContent')
            print('Ilość znalezionych produktów: ' + amount)

    def select_product(self):
        item_visible = self.driver.find_elements(*AddToCartLocators.FIND_PRODUCT)
        item_visible[0].click()

    def go_to_cart(self):
        order_popup = self.driver.find_element(*AddToCartLocators.ORDER_POPUP)
        button_gtc = self.driver.find_element(*AddToCartLocators.GO_TO_CART)
        if order_popup.is_displayed():
            button_gtc.click()
            print('Popup kontynuacji zamówienia jest dostępny')
        else:
            self.driver.close()
            print('Popup kontynuacji zamówienia jest niedostępny')