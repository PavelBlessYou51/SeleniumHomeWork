import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.BaseClass import BasePage


class NotepadesPage(BasePage):
    #   Locators for products

    PRODUCT_LOCATOR = "(//div[@data-meta-product-id='1979696'])[1]"

    #   Loctors for filters

    COUNT_OF_PRODUCTS = "//span[@data-meta-name='SubcategoryPageTitle__product-count']"
    PRICE_FILTER_RIGHT = "(//div[@class='rc-slider-handle rc-slider-handle-2'])[5]"
    BRAND_FILTER = "//input[@id='asus']"

    #   Getters for product

    def get_product(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PRODUCT_LOCATOR)))
        return locator

    #   Getters for filters

    def get_count_of_prod(self):
        locator = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.COUNT_OF_PRODUCTS)))
        return locator

    def get_price_filter_right(self):
        locator = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.PRICE_FILTER_RIGHT)))
        return locator

    def get_brand_filter(self):
        locator = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.BRAND_FILTER)))
        return locator

    #   Actions for product

    def click_on_product(self):
        obj = self.get_product()
        obj.click()
        print("Click on product!")

    #   Actions for filters

    def save_count_of_prod(self):
        obj = self.get_count_of_prod()
        count = obj.text.split()[0]
        print(f"Count of product = {count}")
        return count

    def click_and_pool_price_filter_right(self):
        obj = self.get_price_filter_right()
        action = ActionChains(self.driver)
        action.move_to_element(obj).perform()
        self.driver.execute_script("window.scrollTo(0, 500)")
        action.click_and_hold(obj).move_by_offset(-30, 0).release()
        action.perform()
        print("Move the price filter!")

    def click_brand_filter(self):
        brand_obj = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-meta-value='Бренд']")))
        ActionChains(self.driver).move_to_element(brand_obj).perform()
        obj = self.get_brand_filter()
        obj.click()
        print("Click on brand!")

    #   Methods for products

    def go_to_card_of_product(self):
        self.get_current_url()
        self.click_on_product()

    #   Methods for filter

    def checking_filters(self):
        count_of_prod = list()
        count_of_prod.append(self.save_count_of_prod())
        self.click_and_pool_price_filter_right()
        time.sleep(2)
        count_of_prod.append(self.save_count_of_prod())
        self.click_brand_filter()
        time.sleep(2)
        count_of_prod.append(self.save_count_of_prod())
        return count_of_prod
