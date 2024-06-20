from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.BaseClass import BasePage


class CartPage(BasePage):
    #   Locators

    CODE_PRODUCT = "//span[contains(text(), 'Код товара')]"
    APPLY_ORDER = "//button[@class='e4uhfkv0 css-ki69qx e4mggex0']"

    #   Getters

    def get_code_product(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CODE_PRODUCT)))
        return locator

    def get_button_apply_order(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.APPLY_ORDER)))
        return locator

    #   Actions

    def save_code_of_product(self):
        obj = self.get_code_product()
        self.code = obj.text.split()[2]
        print(f"Code of product {self.code}")

    def click_on_button_apply_order(self):
        obj = self.get_button_apply_order()
        obj.click()
        print("Click on button apply order!")

    #   Methods

    def go_to_registration(self):
        self.get_current_url()
        self.save_code_of_product()
        self.click_on_button_apply_order()
