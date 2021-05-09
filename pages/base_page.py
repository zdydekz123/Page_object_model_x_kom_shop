class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.verify_page()
        self.verify_search_field()
        self.verify_search_result()

    def verify_page(self):
        return

    def verify_search_field(self):
        return

    def verify_search_result(self):
        return