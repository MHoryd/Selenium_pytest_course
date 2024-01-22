from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import os

class AccountPage(BasePage):
    _welcome_header = (By.XPATH,"//h1[@class='entry-title']")
    _username_input = (By.CSS_SELECTOR,"input[id='username']")
    _password_input = (By.CSS_SELECTOR,"input[id='password']")
    _log_in_button = (By.CSS_SELECTOR,"button[class*='woocommerce-form-login__submit']")
    _log_off_link = (By.XPATH,"//div[@class='woocommerce-MyAccount-content']//a[contains(text(),'Wyloguj się')]")
    
    @property
    def loaded(self):
        return self.is_element_displayed(*self._welcome_header)
    
    def fill_proper_credentials(self):
        username = os.environ.get('tapsshop_proper_email')
        password = os.environ.get('tapsshop_proper_password')
        self.find_element(*self._username_input).send_keys(username)
        self.find_element(*self._password_input).send_keys(password)
        return self
        
    def click_log_in_button(self):
        self.find_element(*self._log_in_button).click()
        self.wait.until(self.ec.visibility_of_element_located(self._log_off_link))
        return self