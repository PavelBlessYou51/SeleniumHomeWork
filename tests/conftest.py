import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def start_testing_info():
    """Функция сообщает о старте и финише всех запущенных тестов"""
    print("Start testing!")
    yield
    print("\nEnd testing!")


@pytest.fixture(scope="module")
def get_driver():
    """Функция возвращает вкшмуе"""
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    url = "https://www.citilink.ru/"
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
