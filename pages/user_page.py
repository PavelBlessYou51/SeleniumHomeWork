from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.BaseClass import BasePage


class UserPage(BasePage):
    #   Locators

    CATALOG = "//span[contains(text(), 'Каталог товаров')]"
    NOTEPADES = "(//a[@href='/catalog/noutbuki-i-kompyutery/?ref=mainmenu'])[2]"
    NOTEPADE_CATEGORY = "//a[contains(text(), 'Игровые ноутбуки')]"

    #   Getters

    def get_catalog(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CATALOG)))
        return locator

    def get_notepades(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.NOTEPADES)))
        return locator

    def get_notepade_category(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.NOTEPADE_CATEGORY)))
        return locator

    #   Actions

    def click_on_catalog(self):
        obj = self.get_catalog()
        obj.click()
        print("Click on catalog!")

    def click_on_notepades(self):
        obj = self.get_notepades()
        obj.click()
        print("Click notepades!")

    def click_on_notepade_category(self):
        obj = self.get_notepade_category()
        obj.click()
        print("Click on notepade category")

    #   Methods

    def go_to_list_of_notepades(self):
        self.get_current_url()
        self.click_on_catalog()
        self.click_on_notepades()
        self.click_on_notepade_category()
