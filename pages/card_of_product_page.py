from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from base.BaseClass import BasePage


class CardProductPage(BasePage):
    #   Locators

    CODE_OF_PRODUCT = "//span[@class='e1n0yuko0 e1o6fkkp0 e106ikdt0 app-catalog-ahcgzg e1gjr6xo0']"
    BUTTON_CART = "//span[contains(text(), 'В корзину')]"
    GO_TO_CART_BUTTON = "(//button[@class='e4uhfkv0 css-gh3izc e4mggex0'])[1]"

    #   Getters

    def get_code_product(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CODE_OF_PRODUCT)))
        return locator

    def get_button_card(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_CART)))
        return locator

    def get_go_to_cart_button(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.GO_TO_CART_BUTTON)))
        return locator

    #   Actions

    def save_code_of_product(self):
        obj = self.get_code_product()
        self.code = obj.text.split()[2]
        print(f"Code of product {self.code}")

    def click_on_button_card(self):
        obj = self.get_button_card()
        obj.click()
        print("Product added in the cart!")

    def click_on_go_to_cart_button(self):
        obj = self.get_go_to_cart_button()
        obj.click()
        print("Product added in the cart!")

    #   Methods

    def go_to_cart(self):
        self.get_current_url()
        self.save_code_of_product()
        self.click_on_button_card()
        self.click_on_go_to_cart_button()
