
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/bin/google-chrome"
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()


@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
        ("tomsmith", "wrong123", "Your password is invalid!"),
        ("wronguser", "password123", "Your username is invalid!"),
    ]
)
def test_login(driver, username, password, expected_message):

    driver.get("https://the-internet.herokuapp.com/login")

    login_page = LoginPage(driver)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert expected_message in message
