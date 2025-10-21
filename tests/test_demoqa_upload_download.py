from core.runner import Runner
from pages.demoqa_upload_download import UploadDownloadPage

def test_upload_download_page():
    r = Runner(headless=True)
    try:
        ud = UploadDownloadPage(r)
        ud.run_demo()

        import os
        screenshot_path = os.path.join(os.getcwd(), 'reports', 'demoqa_upload_download.png')
        assert os.path.exists(screenshot_path), "Upload/Download screenshot should exist"
    finally:
        r.close()
