from pages.base_page import BasePage
from pages.regions.base_region import BaseRegion
from pages.regions.menu_region import MenuRegion
from selenium.webdriver.common.by import By
from helpers.helpers import find_item_by_name

class StorePage(BasePage):
    _products_list = (By.CSS_SELECTOR,"ul[class='products columns-4']")
    _product = (By.CSS_SELECTOR,"li[class*='product type-product']")
    
    
    @property
    def loaded(self):
        return self.is_element_displayed(*self._products_list)
    
    @property
    def items(self):
        return [Item(self, product) for product in self.find_elements(*self._product)]
    

    def add_item_to_cart(self,item_name):
        find_item_by_name(item_name, self.items).click_add_to_cart_button()
        
        menu = MenuRegion(self)
        self.wait.until(lambda page: menu.amount != "0,00", "Invalid price value in cart after adding item")
    
    
class Item(BaseRegion):
    _name = (By.CSS_SELECTOR, "h2[class*='woocommerce-loop-product']")
    _add_to_cart_button = (By.CSS_SELECTOR,"a[class*='add_to_cart_button']")
    
    
    @property
    def name(self):
        return self.find_element(*self._name).text
    
    def click_add_to_cart_button(self):
        self.find_element(*self._add_to_cart_button).click()