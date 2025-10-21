
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import os, time
from core.logger import get_logger

class Runner:
    def __init__(self, headless=True):
        opts = Options()
        if headless:
            opts.add_argument('--headless=new')
            opts.add_argument('--window-size=1920,1080')
        opts.add_argument('--start-maximized')
        prefs = {"profile.default_content_setting_values.notifications": 2}
        opts.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
        self.reports = os.path.join(os.getcwd(), 'reports')
        os.makedirs(self.reports, exist_ok=True)
        self.logger = get_logger()
    def open(self, url):
        self.driver.get(url)
        time.sleep(0.8)
    def screenshot(self, name):
        path = os.path.join(self.reports, f"{int(time.time())}_{name}.png")
        self.driver.save_screenshot(path)
        self.logger.info(f'Screenshot saved: {path}')
    def close(self):
        try:
            self.driver.quit()
        except Exception:
            pass
