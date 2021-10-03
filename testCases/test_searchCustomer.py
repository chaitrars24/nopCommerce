import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig


class Test_001_SearchCust:

    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_searchCust(self, setup):
        self.driver = setup
        # self.lp = LoginPage(self.driver)
        # self.lp.set_email(self.email)
        # self.lp.set_password(self.password)
        # self.lp.click_login()
        # print("clicked login")
        # time.sleep(4)

        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.click_customerMain_link()
        time.sleep(2)
        self.searchCust.click_customer_rd()
        self.searchCust.enter_emailid('victoria_victoria@nopCommerce.com')
        self.searchCust.click_search_btn()
        self.searchCust.verify_user('victoria_victoria@nopCommerce.com')
        time.sleep(5)


