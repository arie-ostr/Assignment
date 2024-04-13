from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# new method of remotely installing up-to-date chromedriver.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

GMAP_PATH = "http://maps.google.com/maps"

def get_path_from_lat_long_zoom(lat="32.0998172", long="34.783232", zoom="10"):
    return f"{GMAP_PATH}?q={lat},{long}&z={zoom}"

driver.get(get_path_from_lat_long_zoom()) 

driver.quit()  