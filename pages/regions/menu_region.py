from pages.regions.base_region import BaseRegion
from selenium.webdriver.common.by import By

class MenuRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR, "div[class*=storefront-primary]")
    _store_button = (By.XPATH, ".//li[@id='menu-item-102']/a[contains(text(),'Sklep')]")
    _amount_to_pay = (By.CSS_SELECTOR,"a[class='cart-contents'] span[class='woocommerce-Price-amount amount']")
    
    def amount(self):
        value = self.find_element(*self._amount_to_pay).text
        return value[1:]
    
    def open_store_page(self):
        self.find_element(*self._store_button).click()
        return self
    