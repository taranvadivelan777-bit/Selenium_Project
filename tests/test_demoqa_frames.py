import pytest
import os
from pages.demoqa_frames import FramesPage

@pytest.mark.usefixtures("setup")
class TestFramesPage:

    def test_frames_page(self):
        r = self.driver
        page = FramesPage(r)
        page.run_demo()

        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_frames.png')
        assert os.path.exists(screenshot_path), "Frames screenshot should exist"