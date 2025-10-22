from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckboxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/checkbox'
        self.expand_all = (By.CSS_SELECTOR, "button[title='Expand all']")
        self.collapse_all = (By.CSS_SELECTOR, "button[title='Collapse all']")
        self.home_checkbox = (By.CSS_SELECTOR, "label[for='tree-node-home'] span.rct-checkbox")
        self.result = (By.ID, "result")

    def run_demo(self):
        self.goto(self.url)
        # expand all and click Home checkbox then collapse to validate interaction
        self.click(*self.expand_all)
        self.click(*self.home_checkbox)
        # wait for result text to appear
        self.wait.until(lambda d: d.find_element(*self.result).text != "")
        self.click(*self.collapse_all)
        self.screenshot('demoqa_checkbox')