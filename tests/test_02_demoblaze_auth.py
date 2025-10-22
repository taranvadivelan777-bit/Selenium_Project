import pytest
import os
import time
import random
import string
import csv
from pages.demoblaze_home import DemoBlazeHome
from pages.demoblaze_auth import AuthPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# CSV utility function
def write_csv(file_path, fieldnames, data_list):
    """Append new user data to CSV, create file if not exists"""
    file_exists = os.path.exists(file_path)
    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for data in data_list:
            writer.writerow(data)

# Mark class to use the setup fixture
@pytest.mark.usefixtures("setup")
class TestDemoBlazeAuth:

    def test_demoblaze_auth_flow(self):
        data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
        os.makedirs(data_dir, exist_ok=True)
        users_csv = os.path.join(data_dir, "test_data.csv")

        username = f"auto_user_{''.join(random.choices(string.ascii_lowercase, k=5))}"
        password = "password1234"

        # Use self.driver provided by setup fixture
        home = DemoBlazeHome(self.driver)
        home.open_home()
        home.open_signup()

        auth = AuthPage(self.driver)
        auth.signup(username, password)

        # Handle alert if it appears
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            if "exist" in alert_text:
                print(f"⚠️ User already exists: {username}")
            else:
                print(f"✅ Signup success: {username}")
        except TimeoutException:
            print("No alert shown after signup")

        # Save user to CSV
        new_user = [{"username": username, "password": password}]
        write_csv(users_csv, ["username", "password"], new_user)

        home.open_login()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(auth.login_user)
        )
        time.sleep(1)
        auth.login(username, password)

        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(auth.logout_btn)
        )
        assert logout_btn.is_displayed(), "Logout button should be visible after login"

        auth.logout()

        login_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(home.login_btn)
        )
        assert login_btn.is_displayed(), "Login button should be visible after logout"
