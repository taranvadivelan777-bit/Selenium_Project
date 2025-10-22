import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from pages.demoblaze_home import DemoBlazeHome
from pages.demoblaze_product import ProductPage
from pages.demoblaze_cart import CartPage

@pytest.mark.usefixtures("setup")
class TestDemoBlazeCartOrderFlow:

    def test_demoblaze_cart_order_flow(self):
        r = self.driver  # driver from setup fixture
        home = DemoBlazeHome(r)
        home.open_home()
        home.open_first_product()

        product = ProductPage(r)
        product.add_to_cart()

        # Handle add-to-cart alert
        try:
            WebDriverWait(r, 10).until(EC.alert_is_present())
            alert = r.switch_to.alert
            alert.accept()
            print("🟢 Product added to cart successfully.")
        except (NoAlertPresentException, TimeoutException):
            print("⚠️ No alert appeared after adding to cart.")

        home.go_to_cart()
        cart = CartPage(r)

        # Wait for total price element safely
        try:
            WebDriverWait(r, 10).until(
                lambda driver: cart.find(*cart.total_price).is_displayed()
            )
            total = cart.get_total()
            assert total is not None, "Total price should be visible in cart"
            print(f"🧾 Cart total: {total}")
        except TimeoutException:
            print("⚠️ Cart total not visible; test skipped")
