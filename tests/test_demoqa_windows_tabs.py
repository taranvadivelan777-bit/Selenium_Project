import pytest
import os
from pages.demoqa_windows_tabs import WindowsTabsPage

@pytest.mark.usefixtures("setup")
class TestWindowsTabsPage:

    def test_windows_tabs_page(self):
        r = self.driver
        page = WindowsTabsPage(r)
        page.run_demo()

        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_windows_tabs.png')
        assert os.path.exists(screenshot_path), "Windows/Tabs screenshot should exist"