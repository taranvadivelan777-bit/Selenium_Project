from core.runner import Runner
from pages.demoqa_alerts import AlertsPage

def test_alerts_page():
    r = Runner(headless=True)
    try:
        alerts = AlertsPage(r)
        alerts.run_demo()

        # Assert screenshot is taken
        import os
        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_alerts.png')
        assert os.path.exists(screenshot_path), "Alerts screenshot should exist"
    finally:
        r.close()
