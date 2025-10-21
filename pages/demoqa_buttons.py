from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class ButtonsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/buttons'
        self.double = (By.ID, 'doubleClickBtn')
        self.right = (By.ID, 'rightClickBtn')
        self.dynamic = (By.XPATH, "//button[text()='Click Me']")

    def run_demo(self):
        self.goto(self.url)
        ac = ActionChains(self.driver)
        ac.double_click(self.find(*self.double)).perform()
        ac.context_click(self.find(*self.right)).perform()
        self.click(*self.dynamic)
        self.screenshot('demoqa_buttons')
