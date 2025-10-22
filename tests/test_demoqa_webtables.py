import pytest
import os
from pages.demoqa_webtables import WebTablesPage

@pytest.mark.usefixtures("setup")
class TestWebTablesPage:

    def test_webtables_page(self):
        r = self.driver  # driver from setup fixture
        webtables = WebTablesPage(r)
        webtables.run_demo()

        # Assert screenshot is taken
        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_webtables.png')
        assert os.path.exists(screenshot_path), "WebTables screenshot should exist"
