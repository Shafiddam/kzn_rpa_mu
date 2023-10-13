from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options  # для запуска браузера в безоконном режиме; на английском
from selenium.webdriver.chrome.service import Service
from .pages.admin_page import AdminPage
from .data.data import *
import os


@pytest.fixture
def driver():
    """ Функция для настройки браузера """
    chrome_options = Options()
    chrome_options.add_argument("--lang=en-US")  # Установите желаемый язык, например, en-US для английского
    # chrome_options.add_argument("--headless")
    driver_path = "c:\\Chromedriver\\chromedriver.exe"
    service = Service(driver_path)  # Создание объекта Service с указанием пути к драйверу
    # Создание экземпляра браузерного драйвера с использованием объекта Service
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()  # Максимизация окна браузера
    yield driver
    driver.quit()


@pytest.fixture
def login_and_prepare():
    password = passwords.get('kznadmin', "DefaultPasswordIfNotFound")
    login = list(passwords.keys())[0]

    chrome_options = Options()
    chrome_options.add_argument("--lang=en-US")
    # chrome_options.add_argument("--headless")
    driver_path = "c:\\Chromedriver\\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    admin_page = AdminPage(driver)
    yield driver
    driver.quit()


def take_screenshot(driver, screenshot_name, screenshots_folder="screenshots"):
    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)
    screenshot_path = os.path.join(screenshots_folder, screenshot_name)
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved as {screenshot_path}")


