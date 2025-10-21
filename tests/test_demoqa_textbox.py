from core.runner import Runner
from pages.demoqa_textbox import TextBoxPage

def test_textbox_page():
    r = Runner(headless=True)
    try:
        textbox = TextBoxPage(r)
        textbox.run_demo()

        import os
        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_textbox.png')
        assert os.path.exists(screenshot_path), "Textbox screenshot should exist"
    finally:
        r.close()
