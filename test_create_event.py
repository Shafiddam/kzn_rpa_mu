import pytest

from .pages.admin_page import AdminPage


def test_create_event(driver):

    admin_page = AdminPage(driver)  # Создание объекта LoginPage
    title = 'Test_01'

    try:
        admin_page.login_and_prepare()
        admin_page.click_create_event()
        admin_page.insert_title_create_event(title)
        admin_page.click_save()

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()
