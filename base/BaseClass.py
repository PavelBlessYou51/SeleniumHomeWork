import datetime


class BasePage:
    """Базовый класс, содержащий общие методы для классов страниц"""

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Method returns current URL"""
        url = self.driver.current_url
        print(f"Current URL: {url}")
        return url

    def get_screen(self):
        """Made screen"""
        now_date = datetime.datetime.now(datetime.UTC).strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = "screenshot" + now_date + '.png'
        self.driver.save_screenshot(r'C:\Users\user\PycharmProjects\SeleniumHomeWork\screens\\' + name_screenshot)


