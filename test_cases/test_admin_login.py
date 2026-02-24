import pytest
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import ReadConfig
from utilities.custom_logger import log_maker


class TestAdminLogin:

    admin_page_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    invalid_username = ReadConfig.getInvalidUsername()
    logger = log_maker.log_gen()

    def test_title_verification(self, setup):

        self.logger.info("******** Test Title ********")

        driver = setup
        driver.get(self.admin_page_url)

        assert driver.title == "nopCommerce demo store. Login"

    def test_admin_login(self, setup):

        driver = setup
        driver.get(self.admin_page_url)

        login_page = Login_Admin_Page(driver)

        login_page.enter_username(self.username)
        login_page.enter_password(self.password)
        login_page.click_login()

        assert "Dashboard" in driver.title

    def test_admin_invalid_login(self, setup):

        driver = setup
        driver.get(self.admin_page_url)

        login_page = Login_Admin_Page(driver)

        login_page.enter_username(self.invalid_username)
        login_page.enter_password(self.password)
        login_page.click_login()

        error_message = login_page.get_error_message()

        assert "Login was unsuccessful" in error_message


