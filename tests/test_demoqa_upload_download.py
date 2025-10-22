import pytest
import os
from pages.demoqa_upload_download import UploadDownloadPage

@pytest.mark.usefixtures("setup")
class TestUploadDownloadPage:

    def test_upload_download_page(self):
        r = self.driver  # driver from setup fixture
        ud = UploadDownloadPage(r)
        ud.run_demo()

        # Assert screenshot is taken
        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_upload_download.png')
        assert os.path.exists(screenshot_path), "Upload/Download screenshot should exist"
