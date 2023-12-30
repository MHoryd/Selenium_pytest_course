from pypom import Region
from selenium.webdriver import ActionChains

class BaseRegion(Region):
    def __init__(self, page, root=None):
        super().__init__(page, root)
        self.action = ActionChains(page.driver)