from pages.base_page import BasePage
from pages.regions.base_region import BaseRegion
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers.helpers import find_item_by_name

class CartPage(BasePage):
    _cart_title = (By.CSS_SELECTOR,"h1[class='entry-title']")
    _product_in_the_cart = (By.CSS_SELECTOR,"tr[class*='cart_item']")
    _checkout_button = (By.CSS_SELECTOR,"a[class*='checkout']")
    _item_removed_info = (By.CSS_SELECTOR,"div [class='woocommerce-message'][role='alert']")

    
    @property
    def loaded(self):
        return self.is_element_displayed(*self._cart_title)

    @property
    def items_in_the_cart(self):
        return [CartItem(self,product) for product in self.find_elements(*self._product_in_the_cart)]

    def assert_item_data(self, item_name, item_unit_price,quanity="1",total_price=None):
        if total_price is None:
            total_price = item_unit_price
        
        item = find_item_by_name(item_name,self.items_in_the_cart)

        assert item.item_unit_price == item_unit_price
        assert item.quanity == quanity
        assert item.item_total_price == total_price
    
    def go_to_checkout(self):
        self.driver.execute_script(("arguments[0].click();"),self.find_element(*self._checkout_button))
        return self
    
    def remove_item_from_cart(self, item_name):
        item = find_item_by_name(item_name,self.items_in_the_cart)
        item.find_element(By.CLASS_NAME,'remove').click()
        self.wait.until(self.ec.visibility_of_element_located(self._item_removed_info))
        return self
        
        

class CartItem(BaseRegion):
    _name = (By.CSS_SELECTOR,"td[class*='product-name']")
    _item_unit_price = (By.CSS_SELECTOR,"td[class*='product-price']")
    _quanity = (By.CSS_SELECTOR,"td[class*='product-quantity'] input")
    _item_total_price = (By.CSS_SELECTOR,"td[class*='product-subtotal']")
    
    @property
    def name(self):
        return self.find_element(*self._name).text

    @property
    def item_unit_price(self):
        price = self.find_element(*self._item_unit_price).text
        return price[1:]

    @property
    def quanity(self):
        return self.find_element(*self._quanity).get_attribute('value')
    
    @property
    def item_total_price(self):
        price = self.find_element(*self._item_total_price).text
        return price[1:]