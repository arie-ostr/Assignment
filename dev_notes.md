# Percepto Assignment
- 5~ hr time

### 2024-04-13 10:01 
Starting the assignment , taking an old gmaps project as the base - it has selenium and pytest dependencies. 

### 10:17
Building up the notes, playing around with how I want to do things. 
I have decided to mock everything to highlight the high-level choices I would make
But only add in serious implementation after the assignment is functionally complete. 
For example : Secrets management, storing URLs etc. 

I will model the bestbuy page 
- Landing Page (no splash option)
- Search Bar Component (page)
- 

### 10:28
`https://www.bestbuy.com/site/razer-kraken-hello-kitty-edition-wireless-gaming-headset-pink/6496627.p?skuId=6496627`
current target product. 
might have to scroll to in order to uncover the accordions
    - features
    - q&a
    
Full spec is a different flow

## 12:10
After modelling some of the selectors in regular chrome I realized I can't log in to any user when in a selenium session
Been stuck with it for about 40m now. 

# 12:19
After more testing: I am skipping serach/user related actions, I will try to leave code to support log-in functionality as possible.

# 13:52
I managed to get the flaky element selectors using innerHTML analysis 
I have also did a basic flow in sandbox.py 
I am now making tests in the POM format. (made some progress)
Noting the lack of time I am making things bare-bones. 

# 14:55
I have implemented the search step using the POM

# 15:23
Doing the test with elements hovering. 
Recalled that a good selenium practice is adding innerHTML contents to a text file
This allows to conviniently search for locators without using (the heavy) devtools