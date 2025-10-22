import pytest
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# ---------- Browser Fixture ----------
@pytest.fixture(params=["chrome"], scope="class")
def setup(request):
    browser = request.param
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Browser not supported!")

    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


# ---------- CSV Utility Functions ----------
def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def write_csv(file_path, fieldnames, data_rows):
    """Overwrite CSV file with new data"""
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_rows)


@pytest.fixture(scope="session")
def user_data():
    """Fixture to read user data from CSV"""
    return read_csv("data/users.csv")


@pytest.fixture(scope="session")
def customer_data():
    """Fixture to read customer data from CSV"""
    return read_csv("data/customers.csv")


# ---------- Optional Hooks for Reports ----------
# def pytest_configure(config):
#     # Example Allure/Extent placeholder
#     # You can integrate Allure here later
#     pass
