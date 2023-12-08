from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class StorePage(BasePage):
    _products_list = (By.CSS_SELECTOR,"ul[class='products columns-4']")
    
    
    @property
    def loaded(self):
        return self.is_element_displayed(*self._products_list)