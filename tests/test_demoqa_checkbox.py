import pytest
import os
from pages.demoqa_checkbox import CheckboxPage

@pytest.mark.usefixtures("setup")
class TestCheckboxPage:

    def test_checkbox_page(self):
        r = self.driver
        page = CheckboxPage(r)
        page.run_demo()

        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_checkbox.png')
        assert os.path.exists(screenshot_path), "Checkbox screenshot should exist"