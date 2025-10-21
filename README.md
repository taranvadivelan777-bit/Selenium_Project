
# DemoQA + DemoBlaze Automation Project

This project implements UI automation for demoqa.com and demoblaze.com using Selenium (Chrome + webdriver-manager).

## Structure
- core/runner.py - WebDriver wrapper + logger
- pages/ - Page objects for DemoQA and DemoBlaze flows
- run_all.py - Script that runs both DemoQA and DemoBlaze demos sequentially
- reports/ - Screenshots and logs are saved here
- requirements.txt - dependencies

## Run
1. Create venv and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
2. Run the demo flows:
   ```bash
   python run_all.py
   ```

Note: Chrome must be installed. The project uses webdriver-manager to automatically download chromedriver.
