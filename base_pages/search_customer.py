from selenium.webdriver.common.by import By


class SearchCustomerPage:

    # -------- Locators --------
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"

    btnSearch_id = "search-customers"

    # Table locators
    table_rows_xpath = "//table[@id='customers-grid']/tbody/tr"
    table_cols_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    # -------- Constructor --------
    def __init__(self, driver):
        self.driver = driver

    # -------- Actions --------

    def enter_customer_email(self, email):
        email_field = self.driver.find_element(By.ID, self.txtEmail_id)
        email_field.clear()
        email_field.send_keys(email)

    def enter_customer_firstname(self, firstname):
        firstname_field = self.driver.find_element(By.ID, self.txtFirstName_id)
        firstname_field.clear()
        firstname_field.send_keys(firstname)

    def enter_customer_lastname(self, lastname):
        lastname_field = self.driver.find_element(By.ID, self.txtLastName_id)
        lastname_field.clear()
        lastname_field.send_keys(lastname)



    def click_search(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    # -------- Get table size --------

    def get_total_rows(self):
        rows = self.driver.find_elements(By.XPATH, self.table_rows_xpath)
        return len(rows)

    def get_total_columns(self):
        cols = self.driver.find_elements(By.XPATH, self.table_cols_xpath)
        return len(cols)

    # -------- Search by Email --------

    def search_customer_by_email(self, email):

        flag = False

        for r in range(1, self.get_total_rows() + 1):

            table_email = self.driver.find_element(
                By.XPATH,
                "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]"
            ).text

            if table_email == email:
                flag = True
                break

        return flag


    # -------- Search by Name --------

    def search_customer_by_name(self, name):

        flag = False

        for r in range(1, self.get_total_rows() + 1):

            table_name = self.driver.find_element(
                By.XPATH,
                "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]"
            ).text

            if table_name == name:
                flag = True
                break

        return flag


    # -------- Search by Company --------

