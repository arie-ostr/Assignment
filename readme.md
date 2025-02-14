# Percepto home assignemnt
I must perform checks on elements within the flow of searching for a product.

## How to run this project:
Make sure to have python3.12
On mac/linux:
```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
On Windows:
```bash
python --version
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Then run 
```bash
pytest --html=report.html
```
Pytest will automatically run `test_best_buy.py` and generate a basic HTML report. 


## How this project is built:
This is going to be a straight POM+Selenium ipmelementation.
This would allow for efficient maintainable & clean tests given the limited scope.
A utility module in python will prodive a webdriver, a secrets module will provide test users
There isn't any test data associated with any page (like product names) within the assignment - not implementing.

## Known issues with the solution:
Q&A section contents seems to pull feature contents, not sure why..
browser sessions aren't shared across - significantly slowing down test
no logging and no reporting. 
User Login section in the assignment were blocked due to Best Buy issue.



## Understanding of the best buy site:
Built with react and a whole lot of JS frameworks (wapalizer) 
Not an off-the-shelf solution (so it seems)
There is an annoying survey popup that crashes tests. 
 but it disappears from DOM quickly so I failed to capture the right flow to make sure it's closed. we can also use pytest-retry plugin for this. but it's not the best practice.


## Viable suggestions for further development
If I would think of the assignment as a personal project I would:

**Functionality** 
1. checking browser breakpoints
2. cross browser testing (browser stack)
3. Widgets toolkit with healing selectors
4. add API testing focusing on data integrity. 
5. test the URL and other edoints against access permissions ("IDOR")
6. Visual testing (Applitools, Pytesserect)
7. Parametrize across different users and products with a select set of test cases 
    Test data to be modeled in a way that associates with each page, but not attached to it
    - product data most notably.
