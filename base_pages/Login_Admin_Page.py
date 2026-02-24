from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Admin_Page:

    # Locators
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    error_message_xpath = "//div[contains(@class,'validation-summary-errors')]"
    logout_link_xpath = "//a[@href='/logout']"


    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)


    # Actions
    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, self.textbox_username_id))
        )
        username_field.clear()
        username_field.send_keys(username)


    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, self.textbox_password_id))
        )
        password_field.clear()
        password_field.send_keys(password)


    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
        )
        login_button.click()


    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.error_message_xpath))
        )
        return error.text


    def click_logout(self):
        logout_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.logout_link_xpath))
        )

        logout_button.click()
