import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # 1. Wejdź na stronę "https://www.x-kom.pl/".
        self.driver.get('https://www.x-kom.pl')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()