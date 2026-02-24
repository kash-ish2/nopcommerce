from selenium.webdriver.common.by import By
import random
import string


class Add_Customer_Page:

    # Menu Locators
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath = "//a[@class='btn btn-primary']"

    # Form Locators
    # Email
    txtEmail_xpath = "//input[@id='Email']"

    # Password
    txtPassword_xpath = "//input[@id='Password']"

    # First Name
    txtFirstName_xpath = "//input[@id='FirstName']"

    # Last Name
    txtLastName_xpath = "//input[@id='LastName']"

    # Gender (Male)
    rdMale_xpath = "//input[@id='Gender_Male']"

    # Company
    txtCompany_xpath = "//input[@id='Company']"

    # Is Tax Exempt checkbox
    chkIsTaxExempt_xpath = "//input[@id='IsTaxExempt']"

    # Customer Roles dropdown
    drpCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"

    # Registered role
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"

    # Vendors role
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    # Manager of Vendor dropdown
    drpManagerOfVendor_xpath = "//select[@id='VendorId']"

    # Active checkbox
    chkActive_xpath = "//input[@id='Active']"

    # Must Change Password
    chkMustChangePassword_xpath = "//input[@id='MustChangePassword']"

    # Admin Comment
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"

    # Save button
    btnSave_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    # ----------------- Navigation -----------------

    def click_customers_menu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def click_customers_submenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    # ----------------- Set Customer Info -----------------

    def set_email(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.txtPassword_id).clear()
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(password)

    def set_firstname(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lastname)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()

    def set_company_name(self, company):
        self.driver.find_element(By.ID, self.txtCompanyName_id).clear()
        self.driver.find_element(By.ID, self.txtCompanyName_id).send_keys(company)

    def set_tax_exempt(self):
        self.driver.find_element(By.ID, self.chkIsTaxExempt_id).click()

    # ----------------- Customer Roles -----------------

    def set_customer_role(self, role):

        self.driver.find_element(By.XPATH, self.drpCustomerRoles_xpath).click()

        if role == "Administrators":
            self.driver.find_element(By.XPATH, self.roleAdministrators_xpath).click()

        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.roleForumModerators_xpath).click()

        elif role == "Registered":
            self.driver.find_element(By.XPATH, self.roleRegistered_xpath).click()

        elif role == "Guests":
            self.driver.find_element(By.XPATH, self.roleGuests_xpath).click()

        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.roleVendors_xpath).click()

    # ----------------- Vendor -----------------

    def set_manager_of_vendor(self, vendor_name):
        from selenium.webdriver.support.select import Select
        Select(self.driver.find_element(By.ID, self.drpManagerOfVendor_id))\
            .select_by_visible_text(vendor_name)

    # ----------------- Other Options -----------------

    def set_active(self):
        self.driver.find_element(By.ID, self.chkActive_id).click()

    def set_must_change_password(self):
        self.driver.find_element(By.ID, self.chkMustChangePassword_id).click()

    def set_admin_comment(self, comment):
        self.driver.find_element(By.ID, self.txtAdminComment_id).clear()
        self.driver.find_element(By.ID, self.txtAdminComment_id).send_keys(comment)

    # ----------------- Save -----------------

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()


class SearchCustomerPage:
    pass