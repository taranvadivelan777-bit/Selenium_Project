from core.runner import Runner
from pages.demoblaze_home import DemoBlazeHome
from pages.demoblaze_auth import AuthPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_demoblaze_auth_flow():
    r = Runner(headless=True)
    try:
        home = DemoBlazeHome(r)
        home.open_home()
        home.open_signup()

        auth = AuthPage(r)
        auth.signup("auto_user1234", "password1234")

        home.open_login()
        auth.login("auto_user1234", "password1234")

        # Assert login success by checking logout button visible
        logout_btn = WebDriverWait(r.driver, 10).until(
            EC.visibility_of_element_located(auth.logout_btn)
        )
        assert logout_btn.is_displayed(), "Logout button should be visible after login"

        auth.logout()

        # Assert login button visible after logout
        login_btn = WebDriverWait(r.driver, 10).until(
            EC.visibility_of_element_located(home.login_btn)
        )
        assert login_btn.is_displayed(), "Login button should be visible after logout"

    finally:
        r.close()
