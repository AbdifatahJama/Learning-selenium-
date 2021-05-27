from types import DynamicClassAttribute
from selenium import webdriver
import time

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Further practising explicit waits

my_user_agent  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get('https://www.argos.co.uk/') # Practise automation site
driver.fullscreen_window() # Makes browser full screen

## Clicks cookies accept button

cookieAcceptButton = driver.find_element_by_id('consent_prompt_submit') # Gets element of cookies accept button
cookieAcceptButton.click()

# Finds the search element using the search input id
search = driver.find_element_by_id('searchTerm') 
search.send_keys('Headphones') # Send keys text into search bar
search.send_keys(Keys.RETURN)

try:
    titleOfProduct = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sony WH-CH510 On-Ear Wireless Headphones - Black")) # Using an explicit wait until element via Link Text is present
    )
    titleOfProduct.click() # Clicks Product title Link    
    
    AddToBasketButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div[1]/div[3]/div[1]/section[2]/section/div[15]/div/div[2]/button")) # Waits until add to basket button element button is present on screen
    )
    AddToBasketButton.click() # Simulates add to basket click
    
    AddTrolleyButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Go to trolley")) # Waits until add to trolley button is present
    )
    AddTrolleyButton.click() # Simulates add to trolley click using click method in webdriver
    driver.fullscreen_window() # Makes browser full screen
    
    time.sleep(10)
    
    

except:
    print('Exception')
    
driver.back() # uses back method from webdriver to go back 
driver.back()
driver.back()
driver.fullscreen_window() # Finally increases browser to full screen


    




