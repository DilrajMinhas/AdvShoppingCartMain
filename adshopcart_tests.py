import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdvantageshoppingcartAppPositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_main_advantage_shop_cart():
        methods.setUp()
        methods.create_new_user()
        methods.delete_account_login()
        methods.sign_out()
        methods.login()
        methods.home_page()
        methods.Contact_Form()
        methods.tearDown()




