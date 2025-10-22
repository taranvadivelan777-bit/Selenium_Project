from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class WebTablesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/webtables'
        self.add_btn = (By.ID, 'addNewRecordButton')
        self.first_name = (By.ID, 'firstName')
        self.last_name = (By.ID, 'lastName')
        self.email = (By.ID, 'userEmail')
        self.age = (By.ID, 'age')
        self.salary = (By.ID, 'salary')
        self.department = (By.ID, 'department')
        self.submit = (By.ID, 'submit')

    def run_demo(self):
        self.goto(self.url)
        self.click(*self.add_btn)
        self.find(*self.first_name).send_keys("Demo")
        self.find(*self.last_name).send_keys("User")
        self.find(*self.email).send_keys("demo@example.com")
        self.find(*self.age).send_keys("30")
        self.find(*self.salary).send_keys("5000")
        self.find(*self.department).send_keys("IT")
        self.click(*self.submit)
        self.screenshot('demoqa_webtables')
