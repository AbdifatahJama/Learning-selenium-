from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.fullscreen_window()

# Actions chains simulate clicking different elements on a webpage

# We must find the cookie element that is clicked and the element that tracks the number changes

## We need an implicit wait to give page time to load fully to make sure the elements actually exist on the page before we carry out actions

driver.implicitly_wait(5)
bigCookie = driver.find_element_by_id('bigCookie')
NumberTracker = driver.find_element_by_id('cookies') 

# Get cost of upgrades [cursor grandma]

upgrade = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1,-1,-1)] # puts each element into a list using list comprehemsion

# Instatiate action chain object
actions = ActionChains(driver) 
actions.click(bigCookie) # Action chain that presses cookie which inputs the element of the html

for i in range(5000):
  actions.perform() # Runs all action chains at once
  # We then want to track the number of times the cookie is clicked so we can now when to start upgrading the type of clicker we use 
  count = int(NumberTracker.text[0:2]) # Now checks the current count after each cookie click
  for item in upgrade: # Loops through each upgrade list containing each upgrades element
    value = int(item.text) # Gets price of each upgrade via the element text
    if count<= value: # if statement checks if we can afford an upgrade
      upgrade_actions = ActionChains(driver) # Instatiate new action chain object needed for clicking upgrades 
      upgrade_actions.move_to_element(item) # Moves mouse pointer to uprgrade item
      upgrade_actions.click(item) # Action chain click on item
      upgrade_actions.perform() # Action peformed
      print('a')
      
    else: # If statement is false then else statement is triggerred and passed
      pass
      
       
      
  
  
  
  
