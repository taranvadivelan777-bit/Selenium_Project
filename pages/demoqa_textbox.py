from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TextBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/text-box'
        self.name = (By.ID, 'userName')
        self.email = (By.ID, 'userEmail')
        self.curr = (By.ID, 'currentAddress')
        self.perm = (By.ID, 'permanentAddress')
        self.submit = (By.ID, 'submit')

    def run_demo(self):
        self.goto(self.url)
        self.find(*self.name).clear(); self.find(*self.name).send_keys('Alex Demo')
        self.find(*self.email).clear(); self.find(*self.email).send_keys('alex@example.com')
        self.find(*self.curr).clear(); self.find(*self.curr).send_keys('Current Address')
        self.find(*self.perm).clear(); self.find(*self.perm).send_keys('Permanent Address')

        btn = self.find(*self.submit)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.submit))
        self.driver.execute_script("arguments[0].click();", btn)
        self.screenshot('demoqa_textbox')
