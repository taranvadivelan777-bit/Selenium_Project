import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from pages.demoblaze_home import DemoBlazeHome
from pages.demoblaze_product import ProductPage

@pytest.mark.usefixtures("setup")
class TestDemoBlazeAddToCart:

    def test_demoblaze_add_to_cart(self):
        r = self.driver  # driver from setup fixture
        home = DemoBlazeHome(r)
        home.open_home()

        first_product = (By.XPATH, "//div[@id='tbodyid']//a")
        WebDriverWait(r, 10).until(
            EC.element_to_be_clickable(first_product)
        ).click()

        product = ProductPage(r)
        time.sleep(1)
        title = product.add_to_cart()
        assert title != "", "Product title should not be empty"

        # Handle add-to-cart alert
        try:
            WebDriverWait(r, 5).until(EC.alert_is_present())
            alert = r.switch_to.alert
            alert.accept()
            print("🟢 Product added to cart successfully.")
        except (NoAlertPresentException, TimeoutException):
            print("⚠️ No alert appeared after adding to cart.")
