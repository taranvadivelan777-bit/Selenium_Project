# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.edge.options import Options as EdgeOptions
# from webdriver_manager.chrome import ChromeDriverManager
#
# EDGE_DRIVER_PATH = r"C:\WebDrivers\msedgedriver.exe"
#
# # CLI option
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser", action="append", default=["chrome"],
#         help="Browsers to run: chrome, edge"
#     )
#
# # Parametrize tests automatically
# def pytest_generate_tests(metafunc):
#     if "browser" in metafunc.fixturenames:
#         browsers = metafunc.config.getoption("browser")
#         browsers = list(dict.fromkeys(browsers))
#         metafunc.parametrize("browser", browsers)
#
# # Fixture for driver (function scope)
# @pytest.fixture(scope="function")
# def setup(request, browser):
#     driver = None
#
#     if browser.lower() == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif browser.lower() == "edge":
#         driver = webdriver.Edge(service=EdgeService(EDGE_DRIVER_PATH))
#     else:
#         raise ValueError(f"Browser '{browser}' not supported!")
#
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     request.instance.driver = driver  # use instance instead of cls
#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os

# CLI option for browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="append",
        default=["chrome"],
        help="Browser(s) to run: chrome, edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browsers in headless mode"
    )

# Fixture to parametrize tests across browsers
def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("browser")
        browsers = list(dict.fromkeys(browsers))  # Remove duplicates
        metafunc.parametrize("browser", browsers)

# Fixture to initialize WebDriver
@pytest.fixture(scope="function")
def driver(request, browser):
    headless = request.config.getoption("--headless") or os.getenv("CI") == "true"

    if browser.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser.lower() == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    else:
        raise ValueError(f"Browser '{browser}' is not supported!")

    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()
