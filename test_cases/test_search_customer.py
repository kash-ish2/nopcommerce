import pytest
import time
from base_pages.add_customer import SearchCustomerPage
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.add_customer import Add_Customer_Page
from utilities.read_properties import ReadConfig
from utilities.custom_logger import log_maker


class AddCustomerPage:
    pass


class Test_Search_Customer:
    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = log_maker.log_gen()

    def test_search_customer(self, setup):
        self.logger.info("Test__04__kk")
        driver = setup
        driver.get(self.url)
        driver.maximize_window()

        # Login
        login = Login_Admin_Page(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()

        assert "Dashboard" in driver.title

        # Navigate to Customers
        add_customer = AddCustomerPage(driver)
        add_customer.click_customers_menu()
        add_customer.click_customers_submenu()

        # Search by Email
        search = SearchCustomerPage(driver)
        search.enter_customer_email("arthur.holmes@nopcommerce.com")
        search.click_search()
        time.sleep(3)

        is_email_present = search.search_customer_by_email("arthur.holmes@nopcommerce.com")

        if is_email_present:
            self.logger.info("Test Passed")
            assert True
        else:
            self.logger.info("Test Failed")
            assert False

    def test_search_customer_by_name(self, setup):
        self.logger.info("Test__05__kk")
        driver = setup
        driver.get(self.url)
        driver.maximize_window()

        # Login
        login = Login_Admin_Page(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()

        assert "Dashboard" in driver.title

        # Navigate
        add_customer = AddCustomerPage(driver)
        add_customer.click_customers_menu()
        add_customer.click_customers_submenu()

        # Search by Name
        search = SearchCustomerPage(driver)
        search.enter_customer_firstname("Arthur")
        search.enter_customer_lastname("Holmes")
        search.click_search()
        time.sleep(3)

        is_name_present = search.search_customer_by_name("Arthur Holmes")

        if is_name_present:
            self.logger.info("Test Passed")
            assert True
        else:
            self.logger.info("Test Failed")
            assert False