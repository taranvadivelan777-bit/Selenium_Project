from core.runner import Runner
from pages.demoqa_webtables import WebTablesPage

def test_webtables_page():
    r = Runner(headless=True)
    try:
        webtables = WebTablesPage(r)
        webtables.run_demo()

        import os
        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_webtables.png')
        assert os.path.exists(screenshot_path), "WebTables screenshot should exist"
    finally:
        r.close()
