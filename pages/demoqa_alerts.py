from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/alerts'
        self.alert_btn = (By.ID, 'alertButton')
        self.confirm_btn = (By.ID, 'confirmButton')
        self.prompt_btn = (By.ID, 'promtButton')

    def run_demo(self):
        self.goto(self.url)
        # Simple alert
        self.click(*self.alert_btn)
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

        # Confirm alert
        self.click(*self.confirm_btn)
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()

        # Prompt alert
        self.click(*self.prompt_btn)
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys("DemoText")
        alert.accept()

        self.screenshot('demoqa_alerts')
