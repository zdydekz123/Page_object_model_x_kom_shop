import unittest
from tests.test_add_to_cart import TestAddToCartTest

# Pobieramy testy, ktore chcemy uruchomic
add_product_to_cart = unittest.TestLoader().loadTestsFromTestCase(TestAddToCartTest)

# Łączenie testów (test suit)
test_suite = unittest.TestSuite([add_product_to_cart])

# run test
unittest.TextTestRunner(verbosity=2).run(test_suite)