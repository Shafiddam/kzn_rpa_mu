from time import sleep

import pytest

from .data.data import passwords
from .pages.login_page import LoginPage


def test_login(driver):

    login_page = LoginPage(driver)  # Создание объекта LoginPage
    password = passwords.get('kznadmin', "DefaultPasswordIfNotFound")
    login = list(passwords.keys())[0]

    try:
        login_page.open()
        login_page.click_entry()
        login_page.send_keys_login(login)
        login_page.send_keys_password(password)
        login_page.click_btn_entry()

        login_page.click_admin_panel()
        assert driver.current_url == 'https://kzn.rpa-mu.ru/Admin', "Ошибка: не вошли в панель!"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()
