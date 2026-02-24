import time
import pytest
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import ReadConfig
from utilities.custom_logger import log_maker
from utilities.excel_utils import ExcelUtils


class TestAdminLogin_Data_Driven:

    admin_page_url = ReadConfig.getApplicationURL()
    logger = log_maker.log_gen()
    path = ".//test_data//admin_login_data.xlsx"

    def test_admin_login_data_driven(self, setup):

        driver = setup
        driver.implicitly_wait(10)

        rows = ExcelUtils.get_row_count(self.path, "Sheet1")
        print("Total rows:", rows)

        status_list = []

        for r in range(2, rows + 1):

            driver.get(self.admin_page_url)

            login_page = Login_Admin_Page(driver)

            username = ExcelUtils.read_data(self.path, "Sheet1", r, 1)
            password = ExcelUtils.read_data(self.path, "Sheet1", r, 2)
            expected = ExcelUtils.read_data(self.path, "Sheet1", r, 3)

            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login()

            time.sleep(2)

            if "Dashboard" in driver.title:

                if expected == "Pass":
                    status_list.append("Pass")
                    login_page.click_logout()
                else:
                    status_list.append("Fail")

            else:

                if expected == "Fail":
                    status_list.append("Pass")
                else:
                    status_list.append("Fail")

        assert "Fail" not in status_list