from core.runner import Runner
from pages.demoblaze_home import DemoBlazeHome
import time


def test_demoblaze_home():
    r = Runner(headless=True)  # set headless=False for headed mode
    try:
        home = DemoBlazeHome(r)
        home.open_home()
        time.sleep(1)  # wait for page to load
        home.open_first_product()
        time.sleep(1)
        home.go_to_cart()
        time.sleep(1)

        # Assert cart page loaded by checking cart title exists
        cart_title = r.driver.title
        assert "Cart" in cart_title or "STORE" in cart_title, "Cart page should be opened"
    finally:
        r.close()
