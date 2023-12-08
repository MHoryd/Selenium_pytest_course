from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    _welcome_header = (By.CSS_SELECTOR, "img[class*=image-background]")
    
    
    @property
    def loaded(self):
        return self.is_element_displayed(*self._welcome_header)