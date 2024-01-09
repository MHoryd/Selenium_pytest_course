from datetime import datetime
import os
from selenium import webdriver
from config.config import HEADLESS,FULLSCREEN
import pytest

@pytest.fixture()
def driver(request):
    options = chrome_options()
    chrome_driver = webdriver.Chrome(options=options)
    request.cls.driver = chrome_driver
    yield chrome_driver
    chrome_driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report,'extra', [])
    
    if report.failed:
        # get tge WebDriver instance from test item
        driver = item.funcargs['driver']
        
        # create dir to save screenshot
        screenshot_dir = 'screenshots'
        os.makedirs(screenshot_dir, exist_ok=True)
        
        # Generate a unique filename based on the test name and timestamp
        test_name = item.nodeid.replace('/', '_').replace(':','-')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'{test_name}_{timestamp}.png'
        
        # capture screenshot and save it
        screehshot_path = os.path.join(screenshot_dir,filename)
        driver.save_screenshot(screehshot_path)
        
        # add screenshot path to test report
        extra.append(pytest_html.extras.image(screehshot_path))
    report.extra = extra    
    
    

def chrome_options():
    options = webdriver.ChromeOptions()
    if HEADLESS:
        options.add_argument('--headless')
    if FULLSCREEN:
        options.add_argument('--start-fullscreen')
    return options
    