from xml.sax.handler import property_dom_node
from pypom import Page
from config import config
from selenium.webdriver.support.wait import WebDriverWait
from pages.regions.menu_region import MenuRegion

class BasePage(Page):
    def __init__(self, driver, **url_kwargs):
        super().__init__(driver, **url_kwargs)
        self.base_url = config.BASE_URL
        self.wait = WebDriverWait(driver, config.MAX_WAIT)
        
    @property
    def menu(self):
        return MenuRegion(self)