from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_btn = (By.LINK_TEXT, 'Add to cart')
        self.product_title = (By.CSS_SELECTOR, 'h2.name')

    def add_to_cart(self):
        title = self.find(*self.product_title).text
        self.click(*self.add_btn)
        try:
            self.driver.switch_to.alert.accept()
        except:
            pass
        return title
