import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains

# Automation of an ecommerence site

PATH  = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('http://automationpractice.com/index.php')
driver.fullscreen_window()

SignInButton = driver.find_element_by_link_text('Sign in') # Get sign in button element via link text within a tag
SignInButton.click() # Clicks sign in link button

# Simulate logging in with email and password

USERNAME = 'Jamaa061.309@gmail.com'
PASSWORD = 'Ronaldo81'

try:
    Email_Login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email")) # Waits until email element is present using ID
    )
    Email_Login.send_keys(USERNAME) # Sends username key into email search bar
    
    Password_Login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwd")) # Waits until password element is present using ID
    )
    Password_Login.send_keys(PASSWORD) # Sends password key into password search field
    Password_Login.send_keys(Keys.RETURN) # Sends a return(enter) key in password search field that simulates a login
    
except:
  print('LOGIN EXCPEPTION')

# We then want to navigate to the t shirt section and click on it

try:
    TshirtButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='block_top_menu']/ul/li[3]/a"))
    ) # Uses XPATH to locate T shirt button that we can click
    TshirtButton.click() # T shirt button is clicked use webdriver click method
    
    AddToCart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))
    )
    AddToCart.click()
    
    GoToCheckout = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,'Proceed to checkout'))
    )
    GoToCheckout.click()
    
    checkoutBtn = WebDriverWait(driver, 10).until( # Fins proceed to checkout button
        EC.presence_of_element_located((By.LINK_TEXT, "Proceed to checkout"))
    )
    checkoutBtn.click() # Automates clicking the proceed checkout button to go to the next page
    print('Checkout page/payement page reached')
    
    # Next page at checkout we want to add some comments on how we would like the order to delivered. Text box is identified using name attribute
    textInput = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.NAME, "message")) 
    )
    textInput.send_keys('I would like this order to placed next to the green mat\non the right side of the front door. Thank you in advance') # We then send keys into the text box
    textInput.submit() # We can use the submit button rather than manually finding the button element as all text inputs have a submit method that will crawl up the dom to find the submit button and click it
    
    # we will continue to use explicit waits to ensure the page is fully loaded before we search for an element 
    
    # On the shipping section we need to accept the term and conditions by checking the check box. We first need to find the checkbox element
    termsCheckboxBtn = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.ID, "cgv")) 
    ) # Identifies checkbox element using the checkbox id attribute
    
    status = termsCheckboxBtn.is_selected()
    if status: 
        print('TRUE')# if status returns True(ie: check box is already checked it passes)
        pass
    
    else: # else if it checks the checkbox (IT SHOULD ALWAYS RESORT TO THE ELSE STATEMENT AS THE CHECKBOX WILL NEVER BE CHECKED WHEN THE PAGE IS FIRST LOADED)
        termsCheckboxBtn.click()
        print('Checked')
        # termsCheckboxBtn.submit() # using submit method() on form elements like text inputs checkboxes, radio button , dropdown lists. DOES NOT FOR SOME REASON
        
        
    NextBTN = WebDriverWait(driver, 10).until( # Finds the element of the button we need to press after the checkbox is checked
        EC.presence_of_element_located((By.NAME, "processCarrier")) 
    ) 
    NextBTN.click()
    
    # We then want to show the final price of the order in the console
    
    TotalPrice = WebDriverWait(driver, 10).until( # Locates the span element with the the price within the tags using the elements id attribute
        EC.presence_of_element_located((By.ID, "total_price")) 
    ) 
    print(TotalPrice.text)
    
    # We then want to press the type of payement we would like to pay for the order in.
    # In this case will pay via 'Bank wire'
    # We do not need to use an explicit wait as the page is loaded already
    
    BankWireBtn = driver.find_element_by_class_name('bankwire') # Finds Bankwire element via class attribute
    BankWireBtn.click()
    
    # The final page has a single button that is required to be clicked to confirm and send order 
    # We require an explicit wait 
    
    ConfirmOrderBtn = WebDriverWait(driver, 10).until( # Locates the button element using the tag name(button) by using the button xpath
        EC.presence_of_element_located((By.XPATH, "//*[@id='cart_navigation']/button")) 
    ) 
    ConfirmOrderBtn.click() # The confirm button element is then clicked is submitted
    driver.fullscreen_window() # browser is expanded into full screen
    
    # Order has been succesfully automated from logging in to confirming and sending order
    # Next step is to automate a real order. Will require rotating proxies 
    
    
    
    
    
        
        
        
    
    
    
    
    
    
    
    
    # Logout_Button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.LINK_TEXT,'Sign out'))
    # )
    # Logout_Button.click()
    # print('SUCCESFULLY LOGGED OUT')
    
        
except:
    driver.quit()



## Next step to expand is to go through the payment process(Address and payment details) then submit order. Finally Logout 