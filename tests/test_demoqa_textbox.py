import pytest
import os
from pages.demoqa_textbox import TextBoxPage

@pytest.mark.usefixtures("setup")
class TestTextBoxPage:

    def test_textbox_page(self):
        r = self.driver  # driver from setup fixture
        textbox = TextBoxPage(r)
        textbox.run_demo()

        # Assert screenshot is taken
        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_textbox.png')
        assert os.path.exists(screenshot_path), "Textbox screenshot should exist"
