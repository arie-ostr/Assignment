from selenium_pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time

class BestBuyProductPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)

    price_label = "[data-testid='customer-price']"
    primary_product_image = ".primary-image"

    # features:
    features_drawer_btn = ".features-drawer-btn"
    features_overlay_container = "[aria-label='Features']"
    features_overlay_close_btn = f"{features_overlay_container} [aria-label='Close']"
    features_overlay_details_section = (
        f"{features_overlay_container} .pdp-drawer-content"
    )

    # specs:
    specs_drawer_btn = ".specifications-drawer-btn"
    specs_drawer_container = ".shop-specifications"
    specs_overlay_close_btn = f"{specs_drawer_container} [aria-label='Close']"
    specs_drawer_details_section = f"{specs_drawer_container} .pdp-drawer-content"

    # Q&A - user generated questions
    qna_drawer_btn = ".user-generated-content-question-distillation button"
    qna_container = ".user-generated-content-question-distillation"
    qna_close_btn = f"{qna_container} [aria-label='Close']"
    qna_details_section = f"{qna_container} [data-testid='drawer']"

    #to handle survey before it flakes tests
    survey_close_btn = "#survey_invite_no"

    @staticmethod
    def open_independently(url):
        """
        Initializes the root base by page, makes sure all elems are loaded
        """
        page_instance = BestBuyProductPage(driver=None)  # open with new driver
        page_instance.driver.get(url)
        page_instance.driver.maximize_window()

        # have some elements load to confirm.
        page_instance.get_elems_while_waiting(
            BestBuyProductPage.primary_product_image, 10
        )



        return page_instance

    def get_price_text_size(self):
        """
        For the Assignment test

        Note: I would pull all the HTML or all the computed CSS and filter it
              By the 10-20 attributes I want to ensure are OK

        """
        elem = self.get_visible_elem_while_waiting(self.price_label)
        return self.get_text_size(elem)

    def get_features_text(self):
        """
        extracts text from product features section
        """
        features_content_elem = self.click_and_wait_for(
            self.features_drawer_btn, self.features_overlay_details_section
        )

        text = features_content_elem.text
        # I confirmed this manually.
        self.click(self.features_overlay_close_btn)

        return text

    def get_specs_text(self):
        """
        extracts text from product specs section
        """
        specs_content_elem = self.click_and_wait_for(
            self.specs_drawer_btn, self.specs_drawer_details_section
        )
        text = specs_content_elem.text

        self.click(self.specs_overlay_close_btn)
        return text

    def get_qna_text(self):
        """
        extracts text from product user generated q&a section
        """
        
        btn = self.get_elem(self.qna_drawer_btn)
        self.scroll_to_elem(btn)

        qna_content_elem = self.click_and_wait_for(
            self.qna_drawer_btn, self.qna_details_section
        )
                
        text = qna_content_elem.text

        self.click(self.qna_close_btn)

        return text
