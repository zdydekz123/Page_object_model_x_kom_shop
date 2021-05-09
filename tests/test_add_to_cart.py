import unittest
from tests.test_base import TestBase
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.veryfication_page import VeryficationPage
from time import sleep

class TestAddToCartTest(TestBase):

    def test_product_to_cart(self):
        hp = HomePage(self.driver)

        # 2. Kliknij w puste pole głównej wyszukiwarki sklepu
        hp.click_on_search_field()

        # 3. W polu wyszukiwarki wpisz wartość "laptop"
        hp.type_proper_value('laptop')

        # 4. Wyszukaj pozadana wartosc naciskajac w submit button
        hp.submit_search_value()

        # 5. Kolejno z listy produktów, wybierz element z dostępnym przyciskiem "Dodaj do koszyka”.
        sp = SearchPage(self.driver)
        sp.select_product()

        # 6. Po wyświetleniu okna popup kliknij w przycisk "Przejdź do koszyka".
        sp.go_to_cart()

        # (VERIFICATION) Czy produkt został poprawnie dodany do koszyka
        vp = VeryficationPage(self.driver)
        vp.verify_cart_value()

        sleep(5)

if __name__=="__main__":
    unittest.main(verbosity=2)