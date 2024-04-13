from selenium_pages.base_page import BasePage
import time

class BestBuyMainPage(BasePage):
    #TODO: validate URL 
    BEST_BUY_URL  = "https://www.bestbuy.com/?intl=nosplash"
    
    #singular elems:
    title_img = "[title='BestBuy.com']"
    main_page_account_menu_btn = "#account-menu-account-button"
    main_page_account_menu_container = ".account-menu"
    main_page_account_menu_sign_in_btn = ".sign-in-btn"
    main_page_search_input = "#gh-search-input"

    #elem lists:
    search_suggestion_container = "#suggestViewClientComponent"
    search_suggestion_result_listings = f"{search_suggestion_container} a span[data-testid='Highlighter']"
    search_suggestion_results_products = f"{search_suggestion_container} li[data-testid='related-product-SR-list']"

    def __init__(self,driver):
        super().__init__(driver)

    @staticmethod
    def open_independently():
        """
            Initializes the root base by page, makes sure all elems are loaded
        """
        page_instance = BestBuyMainPage(driver = None) # open with new driver

        #no splash by default
        page_instance.driver.get(BestBuyMainPage.BEST_BUY_URL)
        page_instance.driver.maximize_window()

        #have some elements load to confirm.
        page_instance.get_elems_while_waiting(BestBuyMainPage.title_img,10)

        return page_instance


    def execute_search(self, search_string):
        """
        opens the (difficult) search box in the page
        """
        search_box = self.get_visible_elem_while_waiting(
            self.main_page_search_input,5)
        search_box.click()
        time.sleep(1) # to replace with wait.
        search_box.send_keys(search_string)
        search_box.click()
        time.sleep(1) # to replace with wait.

    def get_search_preview_results_elems(self,search_string):
        """
        returns titles of searched items
        """
        self.execute_search(search_string)
        elems = self.get_elems_while_waiting(self.search_suggestion_result_listings,2)
        return elems

    def get_search_preview_results_names_for(self,search_string):
        """
        returns titles of searched items
        """
        elems = self.get_search_preview_results_elems(search_string)
        return [elem.text for elem in elems]
    
    def hover_on_search_elems_verify_change(self,elems_list):
        """
        Takes ready made elems list and hovers on it. 
        """
        product_result_htmls = []
        for elem in elems_list:
            self.hover_on(elem)
            self.get_elem()
            prudct_results = self.get_elems_while_waiting(
                self.search_suggestion_results_products,3)
            hrefs = [elem.get_attribute("innerHTML") for elem in prudct_results]
            product_result_hrefs.append(hrefs)