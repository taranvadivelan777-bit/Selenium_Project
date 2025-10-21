from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import os

class CartPage(BasePage):
    place_order_btn = (By.XPATH, "//button[text()='Place Order']")
    purchase_btn = (By.XPATH, "//button[text()='Purchase']")
    name_input = (By.ID, "name")
    country_input = (By.ID, "country")
    city_input = (By.ID, "city")
    credit_card_input = (By.ID, "card")
    month_input = (By.ID, "month")
    year_input = (By.ID, "year")
    total_price = (By.ID, "totalp")

    def get_total(self):
        total_text = self.find(*self.total_price).text
        return int(total_text) if total_text.isdigit() else 0

    def fill_order_form(self, name, country, city, credit_card, month, year):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.name_input)).send_keys(name)
        wait.until(EC.visibility_of_element_located(self.country_input)).send_keys(country)
        wait.until(EC.visibility_of_element_located(self.city_input)).send_keys(city)
        wait.until(EC.visibility_of_element_located(self.credit_card_input)).send_keys(credit_card)
        wait.until(EC.visibility_of_element_located(self.month_input)).send_keys(month)
        wait.until(EC.visibility_of_element_located(self.year_input)).send_keys(year)

    def place_order_flow(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.place_order_btn)).click()
        self.fill_order_form(
            name="Auto Tester",
            country="USA",
            city="New York",
            credit_card="1234123412341234",
            month="12",
            year="2025"
        )
        wait.until(EC.element_to_be_clickable(self.purchase_btn)).click()

        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass

        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)
        screenshot_path = os.path.join(reports_dir, "demoblaze_purchase.png")
        self.driver.save_screenshot(screenshot_path)
