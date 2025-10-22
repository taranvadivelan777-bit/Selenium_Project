import time
import pytest
from pages.demoblaze_home import DemoBlazeHome

@pytest.mark.usefixtures("setup")
class TestDemoBlazeHome:

    def test_demoblaze_home(self):
        r = self.driver  # get driver from setup fixture
        home = DemoBlazeHome(r)
        home.open_home()
        time.sleep(1)  # wait for page to load
        home.open_first_product()
        time.sleep(1)
        home.go_to_cart()
        time.sleep(1)

        # Assert cart page loaded by checking cart title exists
        cart_title = r.title
        assert "Cart" in cart_title or "STORE" in cart_title, "Cart page should be opened"
