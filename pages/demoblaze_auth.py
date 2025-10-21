from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

class AuthPage(BasePage):
    signup_user = (By.ID, "sign-username")
    signup_pass = (By.ID, "sign-password")
    signup_btn = (By.XPATH, "//button[text()='Sign up']")
    signup_modal_close = (By.XPATH, "//div[@id='signInModal']//button[@class='close']")

    login_user = (By.ID, "loginusername")
    login_pass = (By.ID, "loginpassword")
    login_btn = (By.XPATH, "//button[text()='Log in']")
    logout_btn = (By.ID, "logout2")

    def signup(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.signup_user)).send_keys(username)
        wait.until(EC.element_to_be_clickable(self.signup_pass)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.signup_btn)).click()

        # Handle alert if present
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            if "already exist" in alert_text:
                print("User already exists, continuing to login...")
        except TimeoutException:
            pass

        # Close signup modal if it’s still open
        try:
            close_btn = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(self.signup_modal_close)
            )
            close_btn.click()
        except TimeoutException:
            pass

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.login_user)).send_keys(username)
        wait.until(EC.element_to_be_clickable(self.login_pass)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_btn)).click()
