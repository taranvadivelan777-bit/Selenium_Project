from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class FramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/frames'
        self.frame1 = (By.ID, 'frame1')
        self.frame2 = (By.ID, 'frame2')
        self.sample_heading = (By.ID, 'sampleHeading')

    def run_demo(self):
        self.goto(self.url)
        # switch to frame1 and read text
        f1 = self.find(*self.frame1)
        self.driver.switch_to.frame(f1)
        _ = self.find(*self.sample_heading).text
        self.driver.switch_to.default_content()

        # switch to frame2
        f2 = self.find(*self.frame2)
        self.driver.switch_to.frame(f2)
        _ = self.find(*self.sample_heading).text
        self.driver.switch_to.default_content()
        self.screenshot('demoqa_frames')