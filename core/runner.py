# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.edge.options import Options as EdgeOptions
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# import os, time
# from core.logger import get_logger
#
# class Runner:
#     def __init__(self, driver=None, browser="chrome", headless=True):
#         self.logger = get_logger()
#         self.reports = os.path.join(os.getcwd(), 'reports')
#         os.makedirs(self.reports, exist_ok=True)
#
#         if driver:
#             self.driver = driver
#             return
#
#         if browser.lower() == "chrome":
#             opts = ChromeOptions()
#             if headless:
#                 opts.add_argument("--headless=new")
#                 opts.add_argument("--window-size=1920,1080")
#             opts.add_argument("--start-maximized")
#             prefs = {"profile.default_content_setting_values.notifications": 2}
#             opts.add_experimental_option("prefs", prefs)
#             self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
#
#         elif browser.lower() == "edge":
#             opts = EdgeOptions()
#             if headless:
#                 opts.add_argument("--headless=new")
#                 opts.add_argument("--window-size=1920,1080")
#             opts.add_argument("--start-maximized")
#             self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=opts)
#
#         else:
#             raise ValueError(f"Browser '{browser}' is not supported!")
#
#     def open(self, url):
#         self.driver.get(url)
#         time.sleep(0.8)
#
#     def screenshot(self, name):
#         path = os.path.join(self.reports, f"{int(time.time())}_{name}.png")
#         self.driver.save_screenshot(path)
#         self.logger.info(f"Screenshot saved: {path}")
#
#     def close(self):
#         try:
#             self.driver.quit()
#         except Exception:
#             pass


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
import os, time
from core.logger import get_logger

# Path to your manually downloaded Edge driver
EDGE_DRIVER_PATH = r"C:\WebDrivers\msedgedriver.exe"

class Runner:
    def __init__(self, driver=None, browser="chrome", headless=True):
        self.logger = get_logger()
        self.reports = os.path.join(os.getcwd(), 'reports')
        os.makedirs(self.reports, exist_ok=True)

        if driver:
            self.driver = driver
            return

        if browser.lower() == "chrome":
            opts = ChromeOptions()
            if headless:
                opts.add_argument("--headless=new")
                opts.add_argument("--window-size=1920,1080")
            opts.add_argument("--start-maximized")
            prefs = {"profile.default_content_setting_values.notifications": 2}
            opts.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

        elif browser.lower() == "edge":
            opts = EdgeOptions()
            if headless:
                opts.add_argument("--headless=new")
                opts.add_argument("--window-size=1920,1080")
            opts.add_argument("--start-maximized")
            self.driver = webdriver.Edge(service=EdgeService(EDGE_DRIVER_PATH), options=opts)

        else:
            raise ValueError(f"Browser '{browser}' is not supported!")

    def open(self, url):
        self.driver.get(url)
        time.sleep(0.8)

    def screenshot(self, name):
        path = os.path.join(self.reports, f"{int(time.time())}_{name}.png")
        self.driver.save_screenshot(path)
        self.logger.info(f"Screenshot saved: {path}")

    def close(self):
        try:
            self.driver.quit()
        except Exception:
            pass
