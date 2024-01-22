from pages.regions.base_region import BaseRegion
from selenium.webdriver.common.by import By

class MenuRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR, "div[class*=storefront-primary]")
    _store_button = (By.XPATH, ".//li[@id='menu-item-102']/a[contains(text(),'Sklep')]")
    _account_button = (By.XPATH, "//li[@id='menu-item-100']/a[contains(text(),'Moje konto')]")
    _amount_to_pay = (By.CSS_SELECTOR,"a[class='cart-contents'] span[class='woocommerce-Price-amount amount']")
    _product_count = (By.XPATH,"//a[@class='cart-contents']/span[@class='count']")
    
    @property
    def amount(self):
        value = self.find_element(*self._amount_to_pay).text
        return value[1:]
    
    def open_store_page(self):
        self.find_element(*self._store_button).click()
        return self
    
    def open_account_page(self):
        self.find_element(*self._account_button).click()
        return self
    
    def menu_pop_up(self):
        amount_element = self.find_element(*self._amount_to_pay)
        self.action.move_to_element(amount_element).perform()
        return CartPopUpRegion(self)
    
    def wait_until_multiple_products_are_added(self, product_count):
        self.wait.until(self.ec.text_to_be_present_in_element(self._product_count,f'{product_count} Produkty'))
        return self
    
class CartPopUpRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR,"div[class='widget woocommerce widget_shopping_cart']")
    _view_cart_button = (By.XPATH,".//a[contains(text(), 'Zobacz koszyk')]")
    _second_item_in_Popup = (By.XPATH,"//div[@class='widget woocommerce widget_shopping_cart']//ul/li[2]")
    
    def go_to_the_cart(self):
        self.wait.until(self.ec.visibility_of_element_located(self._view_cart_button)).click()
        return self