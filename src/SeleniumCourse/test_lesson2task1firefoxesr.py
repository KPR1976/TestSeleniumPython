import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

@pytest.fixture
def driver(request):
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = False
    ffbin = webdriver.firefox.firefox_binary.FirefoxBinary('/Applications/FirefoxESR.app/Contents/MacOS/firefox-bin')
    wd = webdriver.Firefox(capabilities=caps,firefox_binary=ffbin)
    print (wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.google.com/ncr")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 100).until(EC.title_is("webdriver - Google Search"))