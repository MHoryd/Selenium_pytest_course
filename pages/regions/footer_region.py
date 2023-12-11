from pages.regions.base_region import BaseRegion
from selenium.webdriver.common.by import By


class FooterRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR,"p[class='woocommerce-store-notice demo_store']")
    _dissmiss_button = (By.CSS_SELECTOR,"a[class='woocommerce-store-notice__dismiss-link']")
    
    
    
    def click_dissmiss_button(self):
        self.find_element(*self._dissmiss_button).click()