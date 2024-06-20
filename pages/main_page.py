from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.BaseClass import BasePage


class MainPage(BasePage):
    #   Locators

    ENTER_ICON = "(//div[@class='css-1wyvf5z eyoh4ac0'])[1]"
    LOGIN_POLE = "//input[@name='login']"
    PASSWORD_POLE = "//input[@name='pass']"
    ENTER_BUTTON = "//button[@class='e4uhfkv0 css-1nvnwij e4mggex0']"

    #   Getters

    def get_enter_icon(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ENTER_ICON)))
        return locator

    def get_login_pole(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.LOGIN_POLE)))
        return locator

    def get_password_pole(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PASSWORD_POLE)))
        return locator

    def get_enter_button(self):
        locator = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.ENTER_BUTTON)))
        return locator

    #   Actions

    def click_on_enter_icon(self):
        obj = self.get_enter_icon()
        obj.click()
        print("Click enter icon!")

    def send_login(self):
        obj = self.get_login_pole()
        obj.send_keys("prokoshevpavel@mail.ru")
        print("Login sent!")

    def send_password(self):
        obj = self.get_password_pole()
        obj.send_keys('murmansk512345')
        print("Password sent")

    def click_on_enter_button(self):
        obj = self.get_enter_button()
        obj.click()
        print("Click on login button!")

    #   Methods

    def go_to_auth_page(self):
        self.get_current_url()
        self.click_on_enter_icon()
        self.send_login()
        self.send_password()
        self.click_on_enter_button()
