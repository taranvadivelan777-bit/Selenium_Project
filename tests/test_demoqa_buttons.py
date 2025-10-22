import pytest
import os
from pages.demoqa_buttons import ButtonsPage

@pytest.mark.usefixtures("setup")
class TestButtonsPage:

    def test_buttons_page(self):
        r = self.driver  # driver from setup fixture
        buttons = ButtonsPage(r)
        buttons.run_demo()

        # Assert screenshot is taken
        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_buttons.png')
        assert os.path.exists(screenshot_path), "Buttons screenshot should exist"
