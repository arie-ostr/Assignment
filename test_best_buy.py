import pytest
from selenium_pages.best_buy_page import BestBuyMainPage


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
    page.get_search_preview_results_names_for(search_term)



# given :user logged in 
# when :user searches "hello" , search string.
# then : search page opens, all results contain "hello kitty" (arbitrary).

# given: login data
# when:  user logs in best buy
# then: Login page loads



# given : User has searched for hello kitty & sees search results
# when : user hovers between search results 
# then : Search results value changes (in any way)

#Test: User clicks on first product
# Given logged in user, search page, when: user clicks on product in serch page then: this page opens. 

#---- Product page
#Test : Product page conditions:
#  Price on first page
#  Text size 30px 


# Test : Accordion state has required features