from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class WindowsTabsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/browser-windows'
        self.new_tab = (By.ID, 'tabButton')
        self.new_window = (By.ID, 'windowButton')
        self.new_window_message = (By.ID, 'messageWindowButton')

    def run_demo(self):
        self.goto(self.url)
        main = self.driver.current_window_handle
        # Open a new tab
        self.click(*self.new_tab)
        self.wait.until(lambda d: len(d.window_handles) > 1)
        handles = self.driver.window_handles
        for h in handles:
            if h != main:
                self.driver.switch_to.window(h)
                # grab title/body then close
                time.sleep(1)
                self.driver.close()
        self.driver.switch_to.window(main)

        # Open a new window and close similarly
        self.click(*self.new_window)
        self.wait.until(lambda d: len(d.window_handles) > 1)
        for h in self.driver.window_handles:
            if h != main:
                self.driver.switch_to.window(h)
                time.sleep(1)
                self.driver.close()
        self.driver.switch_to.window(main)

        self.screenshot('demoqa_windows_tabs')