import os

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    current_directory = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_new_tab_with_link(self, link):
        """ Открывает новую вкладку и переходит по данной ссылке """
        self.driver.execute_script("window.open('');")  # открываем новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])  # переключаемся на новую вкладку
        self.driver.get(link)