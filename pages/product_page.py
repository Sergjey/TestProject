from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def go_to_product_page(self):
        link = self.browser.find_element(*ProductPageLocators.ITEM)
        link.click()

    def should_be_item(self):
        assert self.is_element_present(*ProductPageLocators.ITEM), "item is not presented"

    def add_item_in_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_ITEM)
        add_button.click()

    def should_be_item_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_ITEM), "cant add item in basket"