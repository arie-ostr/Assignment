import pytest
from selenium_pages.best_buy_page import BestBuyMainPage
from selenium_pages.bast_buy_product_page import BestBuyProductPage
from utils import misc_utils
from utils import baseline_writer

record_baseline = True # this can be set via sys env

@pytest.mark.smoke
def test_bestbuy_navigate():
    """
        Smoke test to see that URL is availible.
    """
    try:
        page = BestBuyMainPage.open_independently()
    except TimeoutError:
        assert False, "Best Buy was not loaded succesfully"



@pytest.mark.smoke
def test_bestbuy_navigate():
    """
        Smoke test to see that URL is availible.
    """
    try:
        page = BestBuyMainPage.open_independently()
    except TimeoutError:
        assert False, "Best Buy was not loaded succesfully"



test_data = [("hello", "hello kitty")]
@pytest.mark.xfail(reason="we get items with just hello")
@pytest.mark.parametrize("search_term, expected_text", test_data)
def test_all_items_contain_search_string(search_term,expected_text):
    """
    Given :user opens system
    When  :user searches like "hello"
    Then  :all search results contain 'hello kitty'

    Note: This assumes there isn't anything like `hello world`
    """
    page = BestBuyMainPage.open_independently()
    search_results_names = page.get_search_preview_results_names_for(search_term)

    #more readable than a list comprehension
    unexpected_serarch_results = []
    for result in search_results_names:
        if expected_text not in result:
            unexpected_serarch_results.append(result)

    err_msg = f"unexpected results :\n\t {unexpected_serarch_results} \n found."
    assert len(unexpected_serarch_results) == 0, err_msg




@pytest.mark.parametrize("search_term", ["hello kitty"])
def test_change_of_products_content_after_hover_on_resut(search_term):
    """
    Given user has searched a string
    When user hovers on different search results
    Then search box displays different products for each search result.

    Note: Assumes no two search results are the same.
    Note2: We will use InnerHTML to implement this quickly. 
    """
    page = BestBuyMainPage.open_independently()
    search_results_elems = page.get_search_preview_results_elems(search_term)
    products_results= page.hover_on_search_elems_get_changs(search_results_elems)

    # need better logging
    assert not misc_utils.n_lists_of_lists_are_same(
        products_results), "found two search results that don't change"


test_data = {
    "hello neighbor game": (
        "https://www.bestbuy.com/site/hello-neighbor-nintendo-switch/6203184.p?skuId=6203184&intl=nosplash", 
        "hello_neighbor_game"
    ),
    "hello neighbor 2 game, switch": (
        "https://www.bestbuy.com/site/hello-neighbor-2-standard-edition-xbox-series-x/6505081.p?skuId=6505081&intl=nosplash", 
        "hello_neighbor_2_game_switch"
    ),
    # "hello kitty and friends": (
    #     "https://www.bestbuy.com/site/razer-hello-kitty-edition-wired-optical-gaming-mouse-with-deathadder-essential-and-goliathus-mouse-pad-medium-pink/6496626.p?skuId=6496626&intl=nosplash", 
    #     "hello_kitty_and_friends"
    # ), removed due to different spec button, OOS
    "hello kitty iphone 15 pro cover": (
        "https://www.bestbuy.com/site/sonix-magsafe-case-for-apple-iphone-15-pro-hello-kitty-cosmic-multiple-colors/6563272.p?skuId=6563272&intl=nosplash", 
        "hello_kitty_iphone_15_pro_cover"
    )
}

@pytest.mark.parametrize("url,baseline_key", test_data.values(),ids=test_data.keys())
def test_test_products_page_price_30px(url,baseline_key):
    """
    Given a product page
    When user navigates to product page
    Then certain constraints are satisfied. 

    Note: more advanced frameworks can split the blocks of code below
          Into their own test cases, reusing the browser. 

    """

    #open page, get price
    page = BestBuyProductPage.open_independently(url)
    get_price_text_size = page.get_price_text_size()
    err_str = f"expecting {get_price_text_size} to be 30px"
    assert get_price_text_size == "30px" , err_str




@pytest.mark.parametrize("url,baseline_key", test_data.values(),ids=test_data.keys())
def test_test_products_page_sections_baseline_compare(url,baseline_key):
    """
    Given a product page
    When user navigates to product page
    Then certain constraints are satisfied. 

    Note: more advanced frameworks can split the blocks of code below
          Into their own test cases, reusing the browser. 

    """

    #open page, get price
    page = BestBuyProductPage.open_independently(url)

    qna_text = page.get_qna_text()
    features_text = page.get_features_text()
    specs_text = page.get_specs_text()


    if record_baseline:
        #might as well be db or s3 bucket.
        baseline_writer.record_data(f"{baseline_key}_qna_text",features_text)
        baseline_writer.record_data(f"{baseline_key}_features_text",features_text)
        baseline_writer.record_data(f"{baseline_key}_specs_text",specs_text)

    else:
        baseline_qna_text = baseline_writer.get_data(
            f"{baseline_key}_qna_text")
        assert "Aryeh" not in baseline_qna_text
        assert baseline_qna_text == qna_text

        baseline_features_text = baseline_writer.get_data(
            f"{baseline_key}_features_text")
        assert "Aryeh" not in features_text
        assert baseline_features_text == features_text

        baseline_specs_text = baseline_writer.get_data(
            f"{baseline_key}_specs_text")
        assert "Aryeh" not in specs_text
        assert baseline_specs_text == specs_text
