from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os 

IMPLICT_WAIT = 5


def create_driver(headless=False):
    chrome_options = Options()
    # if headless:
    #     chrome_options.headless = True

    #prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_extension("GPlaces-get.crx")

    path = os.path.dirname(os.path.abspath(__file__))
    prefs = {"download.default_directory" : path+"/DOWNLOADED"}
    chrome_options.add_experimental_option("prefs",prefs)



    #prefs = {"profile.managed_default_content_settings.images": 2}
    #chrome_options.add_experimental_option("prefs", prefs)
    #chrome_options.add_argument("--disable-features=ExtensionsToolbarMenu")



    driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
    #driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    #driver.implicitly_wait(IMPLICT_WAIT)

    return driver
