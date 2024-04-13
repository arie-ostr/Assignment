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

    def get_elem(self, css_selector):
        """
        Hides the Bys, not relevant for the assignment.
        """
        self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def get_elems(self, css_selector):
        """
        Hides the Bys, not relevant for the assignment.
        """
        self.driver.find_elements(By.CSS_SELECTOR, css_selector)

    def get_visible_elem_while_waiting(self, css_selector, wait_time_seconds=4):
        """
        waits for the elements, sometimes needed.
        """
        wait = WebDriverWait(self.driver, wait_time_seconds)
        element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        return element

    def get_elems_while_waiting(self, css_selector, wait_time_seconds):
        """
        Abstracts out waits
        """
        wait = WebDriverWait(self.driver, wait_time_seconds)
        elems_list = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
        )
        return elems_list

    def click(self, css_locator, wait_time_seconds=4):
        wait = WebDriverWait(self.driver, wait_time_seconds)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_locator))).click()

    def enter_text(self, css_locator, text):
        self.wait.until(
            EC.visibility_of_element_located(By.CSS_SELECTOR, css_locator)
        ).send_keys(text)

    def get_text(self, css_locator):
        return self.wait.until(
            EC.visibility_of_element_located(By.CSS_SELECTOR(css_locator))
        ).text

    def hover_on(self, web_elem, delay=2):
        """Hover over the given web element with an optional delay."""
        action = ActionChains(self.driver)
        action.move_to_element(web_elem)
        action.pause(delay)  # Add a delay before performing the hover action
        action.perform()

    def get_css_computed(self, elem, property):
        script = "return window.getComputedStyle(arguments[0]).getPropertyValue('font-size');"
        result = self.driver.execute_script(script, elem)
        return result

    def get_text_size(self, elem):
        """
        Used in the final test in the best buy assignment
        gets the computed CSS value of some property.
        """
        return self.get_css_computed(elem, "text-size")

    def click_and_wait_for(self, btn_css, result_css, timeout_seconds=2):
        """
        clicks element and waits for result elem
        """
        self.click(btn_css)
        try:
            return self.get_visible_elem_while_waiting(result_css,wait_time_seconds=timeout_seconds)
        except TimeoutError:
            raise TimeoutError(
                f"Failed to locate {result_css} after clicking {btn_css}"
            )

