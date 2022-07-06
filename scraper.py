from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import DesiredCapabilities



capabilities = DesiredCapabilities.CHROME
capabilities["loggingPrefs"] = {"performance": "ALL"}
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headers')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options,desired_capabilities=capabilities)
driver.maximize_window()
