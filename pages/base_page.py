from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver.driver if hasattr(driver, 'driver') else driver
        self.wait = WebDriverWait(self.driver, 10)

    def goto(self, url):
        self.driver.get(url)

    def find(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def finds(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    def click(self, by, value):
        elem = self.wait.until(EC.element_to_be_clickable((by, value)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        elem.click()

    def screenshot(self, name):
        p = os.path.join(os.getcwd(), 'reports', f"{name}.png")
        self.driver.save_screenshot(p)
