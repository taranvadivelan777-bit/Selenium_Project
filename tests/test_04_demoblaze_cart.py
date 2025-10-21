import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.runner import Runner
from pages.demoblaze_home import DemoBlazeHome
from pages.demoblaze_product import ProductPage
from pages.demoblaze_cart import CartPage
from selenium.common.exceptions import NoAlertPresentException


def test_demoblaze_cart_order_flow():
    r = Runner(headless=True)
    try:
        home = DemoBlazeHome(r)
        home.open_home()
        home.open_first_product()

        product = ProductPage(r)
        product.add_to_cart()

        # Handle alert safely
        try:
            alert = WebDriverWait(r.driver, 5).until(EC.alert_is_present())
            alert.accept()
        except NoAlertPresentException:
            pass

        home.go_to_cart()

        # Wait until cart total is visible
        cart = CartPage(r)
        total_elem = WebDriverWait(r.driver, 10).until(
            lambda driver: cart.find(*cart.total_price).is_displayed()
        )
        total = cart.get_total()
        assert total is not None, "Total price should be visible in cart"

        # Optionally: you can add more asserts for item names, quantity, etc.

    finally:
        r.close()
