from core.runner import Runner
from pages.demoqa_buttons import ButtonsPage

def test_buttons_page():
    r = Runner(headless=True)
    try:
        buttons = ButtonsPage(r)
        buttons.run_demo()

        import os
        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_buttons.png')
        assert os.path.exists(screenshot_path), "Buttons screenshot should exist"
    finally:
        r.close()
