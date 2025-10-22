import pytest
import os
from pages.demoqa_alerts import AlertsPage

@pytest.mark.usefixtures("setup")
class TestAlertsPage:

    def test_alerts_page(self):
        r = self.driver  # driver from setup fixture
        alerts = AlertsPage(r)
        alerts.run_demo()

        # Assert screenshot is taken
        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_alerts.png')
        assert os.path.exists(screenshot_path), "Alerts screenshot should exist"
