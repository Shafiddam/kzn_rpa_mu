import json
import os
import secrets
import string
from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from ..data.data import *

current_directory = os.path.dirname(os.path.abspath(__file__))
counter_file_path = os.path.join(current_directory, '..', 'data', 'counter.txt')


class AdminPage(BasePage):

    class Locators:
        LOGIN_URL = 'https://kzn.rpa-mu.ru/'
        BTN_LOGIN = (By.CSS_SELECTOR, btn_login)
        BTN_ENTRY = (By.XPATH, btn_entry)
        HREF_ADMIN = (By.XPATH, href_admin)
        CREATE_EVENT = (By.XPATH, create_event)
        BTN_SAVE = (By.NAME, btn_save)
        INSERT_TITLE_CREATE_EVENT = (By.ID, insert_title_create_event)
        SELECTOR_ENTER_LOGIN = (By.ID, selector_enter_login)
        SELECTOR_ENTER_PASSWORD = (By.ID, selector_enter_password)

    def login_and_prepare(self):
        password = passwords.get('kznadmin', "DefaultPasswordIfNotFound")
        login = list(passwords.keys())[0]

        self.open()
        self.click_entry()
        self.send_keys_login(login)
        self.send_keys_password(password)
        self.click_btn_entry()
        self.click_admin_panel()

    def open(self):
        self.driver.get(self.Locators.LOGIN_URL)

    def click_entry(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_LOGIN)).click()

    def click_btn_entry(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_ENTRY)).click()

    def find_href_admin(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.HREF_ADMIN))

    def click_admin_panel(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.HREF_ADMIN)).click()

    def click_create_event(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.CREATE_EVENT)).click()

    def click_save(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SAVE)).click()

    def insert_title_create_event(self, data):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_TITLE_CREATE_EVENT))
        element.click()
        element.send_keys(data)

    def _send_keys_to_input(self, locator, data):
        input_element = self.wait.until(EC.visibility_of_element_located(locator))
        input_element.click()
        input_element.clear()
        input_element.send_keys(data)

    def click_agree_terms(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_AGREE_TERMS)).click()

    def reset_confirm(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_RESET_CONFIRM)).click()

    def enter_code(self, data):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.ENTER_CODE))
        element.click()
        element.send_keys(data)

    def send_keys_new_password(self, data):
        self._send_keys_to_input(self.Locators.SELECTOR_ENTER_PASSWORD, data)

    def send_keys_login(self, data):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_ENTER_LOGIN)).clear()
        self._send_keys_to_input(self.Locators.SELECTOR_ENTER_LOGIN, data)

    def send_keys_password(self, data):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_ENTER_PASSWORD)).clear()
        self._send_keys_to_input(self.Locators.SELECTOR_ENTER_PASSWORD, data)

    def reset_create(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_RESET_CREATE)).click()

    def click_login_tonkeeper(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_TONKEEPER)).click()

    def click_signup_tonkeeper(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_TONKEEPER)).click()

    def click_login_telegram(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_TELEGRAM)).click()

    def click_login_google(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GOOGLE_LOGIN)).click()

    def click_login_apple(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_APPLE_LOGIN)).click()

    def click_login_qr_code(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_QR_CODE)).click()

    def find_text_2fa_in_apple(self):
        locator = (By.CSS_SELECTOR, '.si-container-title')
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            raise Exception("Ошибка: не удалось найти текст о вводе 2ФА")

    def insert_email(self, email):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_EMAIL))
        element.click()
        element.send_keys(email)

    def insert_email_in_apple(self, email):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_EMAIL_IN_APPLE))
        element.click()
        element.send_keys(email)

    def insert_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_PASSWORD_IN_GOOGLE))
        element.click()
        element.send_keys(password)

    def insert_password_in_apple(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_PASSWORD_IN_APPLE))
        element.click()
        element.send_keys(password)

    def modal_tonkeeper(self):
        # поиск модалки
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_MODAL_TONKEEPER))

    def modal_qr_code(self):
        # поиск модалки
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_MODAL_QR_CODE))

    def qr_code_tonkeeper(self):
        # поиск QR-кода
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_QR_CODE_TONKEEPER))

    def qr_code_pict(self):
        # поиск QR-кода
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_QR_CODE_PICT))

    def tonkeeper_message_text(self):
        # поиск названия модалки "Log in via TonKeeper"
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_MESSAGE_TEXT))

    def tonkeeper_message_text2(self):
        # поиск названия модалки "Sign up via TonKeeper"
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_MESSAGE_TEXT2))

    def qr_message_text(self):
        # поиск названия модалки "Log in with QR code"
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_QR_MESSAGE_TEXT))

    def qr_code_tonkeeper_screenshot(self):
        """ Создание скриншота qr-кода (вход через тонкипер) и сохранение в папку screenshot """
        qr_code_modal = self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_QR_TONKEEPER_PICT))
        # путь к папке screenshot, которая находится на одном уровне с pages
        screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshot')
        # Если папка не существует, создаем ее
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        sleep(1)  # надо явно задать паузу, иначе скриншот не распознается
        screenshot_path = os.path.join(screenshot_folder, 'qr_code_tonkeeper.png')
        qr_code_modal.screenshot(screenshot_path)
        return screenshot_path

    def compare_url_dashboard(self):
        """
        Сравнение url: проверяем, что вошли на дашборд
        """
        self.wait.until(EC.url_to_be('https://app.cryptomus.com/dashboard/'))

    def get_new_email(self):
        """ метод создания нового почтового ящика на основе добавления +1 к имени """
        # Попробуем прочитать счетчик из файла, и если его нет, создадим файл с начальным значением 0
        try:
            with open(counter_file_path, 'r') as f:
                counter = int(f.read().strip())
        except FileNotFoundError:
            # Убедимся, что папка data существует
            if not os.path.exists('data'):
                os.makedirs('data')
            counter = 0
            with open(counter_file_path, 'w') as f:
                f.write(str(counter))
        # Увеличиваем счетчик на 1
        counter += 1
        # Обновляем файл
        with open(counter_file_path, 'w') as f:
            f.write(str(counter))
        # Возвращаем новый email на основе счетчика
        return f"{self.base_email}+{counter}{self.domain}"


class PasswordManager:

    def __init__(self):
        self.passwords_dict = {}

    @staticmethod
    def generate_password(length=10):
        """
        генерация нового пароля из 10 символов (обязательно одна заглавная и одна цифра)
        """
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        # Check if the password contains at least one uppercase letter and one digit
        while not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
            password = ''.join(secrets.choice(alphabet) for _ in range(length))
        print("Пароль:", password)
        return password

    @staticmethod
    def save_password_to_env(password):
        """ Сохраняем пароль в переменной окружения """
        os.environ["AUTOMATION_PASSWORD"] = password

    @staticmethod
    def get_saved_password():
        """ получить сохраненный пароль из переменной окружения """
        return os.environ.get("AUTOMATION_PASSWORD", "")

    def save_password(self, login, password):
        """ Сохраняет пароль в словаре """
        self.passwords_dict[login] = password

    def save_to_json(self, filename='passwords.json'):
        """
        Сохраняет словарь паролей в JSON-файл
        """
        # Получаем директорию, в которой находится данный скрипт
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Возвращаемся на уровень вверх (из pages в Work)
        parent_dir = os.path.dirname(current_script_dir)
        # Создайте путь к папке data
        data_dir = os.path.join(parent_dir, 'data')
        # Если папка data не существует, создайте её
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        # Создайте полный путь к файлу внутри папки data
        full_path = os.path.join(data_dir, filename)
        with open(full_path, 'w') as file:
            json.dump(self.passwords_dict, file)

    def load_from_json(self, filename='passwords.json'):
        """
        Загружает словарь паролей из JSON-файла
        """
        try:
            with open(filename, 'r') as file:
                self.passwords_dict = json.load(file)
        except FileNotFoundError:
            # Файл не найден, можно обработать ошибку или просто пропустить
            pass
