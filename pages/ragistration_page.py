import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.BaseClass import BasePage


class RegPage(BasePage):
    #   Locators

    CUSTOMER_DATA = "//button[@class='e4uhfkv0 css-pjyyz3 e4mggex0']"
    FIRST_NAME = "//input[@name='RecipientForm__first-name']"
    LAST_NAME = "//input[@name='RecipientForm__last-name']"
    PHONE_NUMBER = "(//input[@name='input-validation-field'])[1]"
    CREATE_BUTTON = "//button[@class='e4uhfkv0 css-gh3izc e4mggex0']"
    APPLY_DATA = "//span[contains(text(), 'Данные получателя указаны верно*')]"
    END_ORDER = "//button[@class='e1jq023s0 css-ol7d38 e4mggex0']"
    APPROVED_ORDER = "//span[contains(text(), 'Заказ ожидает оплаты!')]"

    #   Getters

    def get_customer_data(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CUSTOMER_DATA)))
        return locator

    def get_first_name(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.FIRST_NAME)))
        return locator

    def get_last_name(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.LAST_NAME)))
        return locator

    def get_phone_num(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PHONE_NUMBER)))
        return locator

    def get_create_button(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.CREATE_BUTTON)))
        return locator

    def get_apply_data(self):
        locator = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.APPLY_DATA)))
        return locator

    def get_end_order(self):
        locator = self.driver.find_element(by=By.XPATH, value=self.END_ORDER)
        return locator

    def get_approve(self):
        locator = self.driver.find_element(by=By.XPATH, value=self.APPROVED_ORDER)
        text = locator.text
        return text

    #   Actions

    def click_customer_data(self):
        obj = self.get_customer_data()
        obj.click()
        print("Click on customer data!")

    def click_first_name(self):
        obj = self.get_first_name()
        obj.send_keys("Ivan")
        print("First name was sent!")

    def click_last_name(self):
        obj = self.get_last_name()
        obj.send_keys("Ivanov")
        print("Last name was sent!")

    def click_phone_num(self):
        obj = self.get_phone_num()
        obj.send_keys('79600248889')
        print("Phone number was sent!")

    def click_create(self):
        obj = self.get_create_button()
        obj.click()
        print("Click on create button!")

    def click_apply_data(self):
        obj = self.get_apply_data()
        obj.click()
        print("Click on apply data!")

    def click_end_order(self):
        obj = self.get_end_order()
        obj.click()
        print("Click on end order!")

    #   Methods

    def end_registration(self):
        self.get_current_url()
        self.click_customer_data()
        self.click_first_name()
        self.click_last_name()
        self.click_phone_num()
        self.click_create()
        time.sleep(2)
        self.click_apply_data()
        time.sleep(2)
        self.click_end_order()

