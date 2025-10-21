from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DemoBlazeHome(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.demoblaze.com/index.html'
        self.prod_links = (By.CSS_SELECTOR, 'a.hrefch')
        self.cart_link = (By.ID, 'cartur')
        self.login_btn = (By.ID, 'login2')
        self.signup_btn = (By.ID, 'signin2')

    def open_home(self):
        self.goto(self.url)

    def open_first_product(self):
        elems = self.finds(*self.prod_links)
        if elems:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elems[0])
            elems[0].click()

    def go_to_cart(self):
        self.click(*self.cart_link)

    def open_login(self):
        self.click(*self.login_btn)

    def open_signup(self):
        self.click(*self.signup_btn)
