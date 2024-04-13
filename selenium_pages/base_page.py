# base page with instance of driver 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.selenium_utils import get_chromedriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """
        Basic selenium boilerplate, 
        
        Some pages will have static method for creation? 
    
    """
    def __init__(self, driver=None):
        """
        Also: Sets up  a chromedriver instance, 
        Typically set up as a fixture, depending on how we manage resources

        Here we will create a driver with the page. 
        """
        if driver is None:
            self.driver = get_chromedriver()
        else: 
            self.driver = driver 
        self.wait = WebDriverWait(self.driver, 10) 

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
   

    def get_elem(self,css_selector):
        """
        Hides the Bys, not relevant for the assignment.
        """
        self.driver.find_element(By.CSS_SELECTOR,css_selector)

    def get_elems(self,css_selector):
        """
        Hides the Bys, not relevant for the assignment.
        """
        self.driver.find_elements(By.CSS_SELECTOR,css_selector)

    def get_visible_elem_while_waiting(self, css_selector, wait_time_seconds):
        """
        waits for the elements, sometimes needed.
        """
        wait = WebDriverWait(self.driver, wait_time_seconds)
        element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
        )    
        return element

    def get_elems_while_waiting(self,css_selector, wait_time_seconds):
        """
        Abstracts out waits
        """
        wait = WebDriverWait(self.driver, wait_time_seconds)
        elems_list = wait.until(
                    EC.presence_of_all_elements_located((
                        By.CSS_SELECTOR,
                          css_selector)))
        return elems_list

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()
    
    def enter_text(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    
    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text
    
    def hover_on(self,web_elem,delay=2):
        """Hover over the given web element with an optional delay."""
        action = ActionChains(self.driver)
        action.move_to_element(web_elem)
        action.pause(delay)  # Add a delay before performing the hover action
        action.perform()

    












