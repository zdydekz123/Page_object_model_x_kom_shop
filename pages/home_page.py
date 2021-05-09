from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators_x_kom import SearchEngineLocators

class HomePage(BasePage):

    def verify_page(self):
        assert 'x-kom.pl - Sklep komputerowy' in self.driver.title
        print('Potwierdzenie tytułu strony glównej')

    def verify_search_field(self):
        wait = WebDriverWait(self.driver, 40)
        search_field = wait.until(EC.presence_of_element_located(SearchEngineLocators.SEARCH_FIELD))
        placeholder = search_field.get_attribute('placeholder')
        assert placeholder == 'Czego szukasz?'
        print('Wartość placeholdera wyszukiwarki jest równa: ' + placeholder)

    def click_on_search_field(self):
        search_field = self.driver.find_element(*SearchEngineLocators.SEARCH_FIELD)
        search_field.click()

    def type_proper_value(self, item_name):
        search_value = self.driver.find_element(*SearchEngineLocators.SEARCH_FIELD)
        search_value.send_keys(item_name)

    def submit_search_value(self):
        wait = WebDriverWait(self.driver, 40)
        submit_value = wait.until(EC.element_to_be_clickable(SearchEngineLocators.SEARCH_SUBMIT))
        submit_value.click()