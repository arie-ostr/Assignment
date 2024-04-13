from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def get_chromedriver():
    """
    Handles provisioning of selenium webdriver

    the
    """
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    driver_instance = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options)

    return  driver_instance
