import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#main page
main_page_account_menu_btn = "#account-menu-account-button"
main_page_account_menu_container = ".account-menu"
main_page_account_menu_sign_in_btn = ".sign-in-btn"
main_page_search_input = "#gh-search-input"









chrome_options = Options()

# new method of remotely installing up-to-date chromedriver.

# Create a ChromeOptions instance

# Set a custom user-agent string
#chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
wait = WebDriverWait(driver, 5)


best_buy_path = "https://www.bestbuy.com/?intl=nosplash"



driver.get(best_buy_path) 
driver.maximize_window()

title_img = driver.find_element(By.CSS_SELECTOR,"[title='BestBuy.com']")
title_img.click()
search_box = driver.find_element(By.CSS_SELECTOR,"#gh-search-input")


search_box.click()
time.sleep(1)
search_box.send_keys("hello")
search_box.click()
time.sleep(1)
wait = WebDriverWait(driver, 2)
search_items = wait.until(
    EC.presence_of_all_elements_located((
        By.CSS_SELECTOR, "#suggestViewClientComponent a span[data-testid='Highlighter']")))



for search_item in search_items:
    print (search_item.text)


#html = options_container_html.get_attribute('inner_HTML')
driver.quit()  