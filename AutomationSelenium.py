from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains

# Automation of an ecommerence site
# We need to login,go to t shirt section, add to cart, then logout,finally revert to a google main page

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
    
    Logout_Button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,'Sign out'))
    )
    Logout_Button.click()
    print('SUCCESFULLY LOGGED OUT')
    
        
except:
    driver.quit()



## Next step to expand is to go through the payment process(Address and payment details) then submit order. Finally Logout 