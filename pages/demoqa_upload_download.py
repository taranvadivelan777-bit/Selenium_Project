from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import os

class UploadDownloadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://demoqa.com/upload-download'
        self.uinput = (By.ID, 'uploadFile')
        self.dbtn = (By.ID, 'downloadButton')

    def run_demo(self):
        self.goto(self.url)
        tmp = os.path.join(os.getcwd(), 'reports', 'sample_upload.txt')
        with open(tmp, 'w') as f:
            f.write('demo upload content')

        self.find(*self.uinput).send_keys(tmp)
        self.click(*self.dbtn)
        self.screenshot('demoqa_upload_download')
