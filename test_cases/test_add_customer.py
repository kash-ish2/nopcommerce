import pytest
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.add_customer import Add_Customer_Page
from utilities.read_properties import ReadConfig
from utilities.custom_logger import log_maker





class Test_Add_Customer:

    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_add_new_customer(self, setup):

        driver = setup
        driver.get(self.url)
        driver.maximize_window()

        # ---------------- Login ----------------
        login = Login_Admin_Page(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()

        assert "Dashboard" in driver.title

        # ---------------- Navigate ----------------
        add_customer = Add_Customer_Page(driver)
        add_customer.click_customers_menu()
        add_customer.click_customers_submenu()
        add_customer.click_add_new()

        # ---------------- Fill Customer Form ----------------



        add_customer.set_password("Test@123")
        add_customer.set_firstname("Kashish")
        add_customer.set_lastname("Tiwari")
        add_customer.set_gender("Female")
        add_customer.set_company_name("Angel Star")

        add_customer.set_tax_exempt()

        # Customer Role
        add_customer.set_customer_role("Registered")

        # Vendor
        add_customer.set_manager_of_vendor("Vendor 1")

        add_customer.set_active()
        add_customer.set_must_change_password()

        add_customer.set_admin_comment("Customer created by automation test")

        # ---------------- Save ----------------
        add_customer.click_save()

        # ---------------- Validation ----------------
        success_message = driver.page_source

        assert "The new customer has been added successfully" in success_message