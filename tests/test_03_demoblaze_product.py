from core.runner import Runner
from pages.demoblaze_home import DemoBlazeHome
from pages.demoblaze_product import ProductPage
from selenium.common.exceptions import NoAlertPresentException
import time

def test_demoblaze_add_to_cart():
    r = Runner(headless=True)
    try:
        home = DemoBlazeHome(r)
        home.open_home()
        home.open_first_product()
        time.sleep(1)

        product = ProductPage(r)
        title = product.add_to_cart()

        # Assert product added successfully
        assert title != "", "Product title should not be empty"

        # Handle alert safely
        try:
            alert = r.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass
    finally:
        r.close()
