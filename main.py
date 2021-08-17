'''The following script is being used to make bot to purchase a PS5 which is currently in demand. The site being scraped is - https://www.amazon.co.uk/ '''

import bs4
import requests
from requests.api import head
from requests.auth import HTTPProxyAuth
import json
from requests.exceptions import RequestException, RetryError
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import action_chains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException,ElementNotVisibleException
from bs4 import BeautifulSoup as bs
import time 
import random
import os
import shutil
from datetime import datetime,timedelta

PATH = 'C:\Program Files (x86)\chromedriver.exe'# Location of web driver file
 # Allows us to specify the browser we want to specify, in this case Chrome, the nessecary webdriver for the current chrome version is specified as an argument
header = {
  'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}


class Robot:
  def __init__(self,username = '',password = ''):
    '''Initialising logins and link'''
    self.driver = webdriver.Chrome(PATH) # Allows us to specify the browser we want to specify, in this case Chrome, the nessecary webdriver for the current chrome version is specified as an argument
    self.username = username
    self.password = password
    self.link = 'https://www.amazon.co.uk/'
    self.product = 'PS5'
    self.driver.delete_all_cookies()
    self.driver.get(self.link)
    self.driver.fullscreen_window()
    self.dict  ={
      1:username,
      2:password
    }
    
  def run(self):
    self.accept_cookies()
    self.login()
    self.search_for_product()
    
  def login(self,tries = 5):
    '''Logins to website using unique login details'''
    # self.accept_cookies() # Method accept cookies
    email_box = self.driver.find_element_by_id('ap_email') # Two element with class name form control
    i = 1
    '''Iterates through both login boxes and send keys that are stored in a dictionary object in the initialisation'''
    for char in self.username:
      '''Iterares through each charecter in the username and send keys into the email'''
      email_box.send_keys(char)
      time.sleep(0.3)
      
    self.driver.find_element_by_id('continue').click() # Automates clicking continue button
    self.driver.implicitly_wait(2)
    
    product_name = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.ID, "ap_password"))
    )
    for char in self.password:
      '''Iterares through each charecter in the username and send keys into the email'''
      product_name.send_keys(char)
      time.sleep(0.3)
      
    self.driver.find_element_by_id('signInSubmit').click() # Automates clicking sign in button
    
  '''Then want click on PS5 product named - Sony PlayStation 5 Console'''
  def search_for_product(self):
    '''Click account and list button'''
    self.driver.find_element_by_id('nav-link-accountList').click()
    '''Then want to send keys of the product into search bar '''
    
    list_item = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.LINK_TEXT, "Lists"))
    )
    list_item.click()
    
    add_to_basket_element = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.LINK_TEXT,'Add to Basket'))
    ) # Finds basket element using explicit wait then clicks
    add_to_basket_element.click() 
    
    
    proceed_to_checkout = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.LINK_TEXT,'Proceed to checkout'))
    ) # After add to basket is clicked the button is configued and changes to proceed to checkout
    proceed_to_checkout.click()
    
    deliver_to_this_address_btn = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.LINK_TEXT,'Deliver to this address'))
    ) # Current default address is correct so this button is clicked to confirm to deliver to this address
    deliver_to_this_address_btn.click()
    
    confirm_payement_method_btn = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.NAME,'ppw-widgetEvent:SetPaymentPlanSelectContinueEvent'))
    ) # Confirm default payement method that amazon already have saved to my account
    confirm_payement_method_btn.click()
    
    '''Final button is buy now button that confirms order'''
    confirm_order = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.NAME,'placeYourOrder1'))
          )
    confirm_order.click()
    
    self.driver.implicitly_wait(10)
    
    '''Then want to take screenshot of confirmation page'''
    self.driver.save_screenshot('confirmation_page.png')
    
    time.sleep(5)
    self.driver.quit()
    
  def accept_cookies(self):
    '''When website is first loaded up, user has to accept cookies'''
    cookies_button = self.driver.find_element_by_id('sp-cc-accept') # locates button using the xpath
    cookies_button.click() # Clicks on to accept cookies
    '''Bot then wants to press account button to proceed to login page'''
    account_button = self.driver.find_element_by_id('nav-link-accountList-nav-line-1')
    account_button.click()
    
  
  def scan(self):
    '''Scans for any changes on the website constantly to catch when product is available '''
    pass

auth = HTTPProxyAuth('TestProxy12','Ronaldo81_country-gb')
def check_availability():
  header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
  '''Proxies dict that contains key:value of host proxy'''
  proxies = {
    "http":"http://91.239.130.17:12323"
  }
  try:
    r = requests.get('https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?dchild=1&keywords=ps5&qid=1629058931&sr=8-1',auth=auth,proxies=proxies,headers=header)
    # response = requests.get('http://httpbin.org/ip',auth=auth,proxies=proxies,headers=header)
    # print(response.text)
    source = r.text
    if r.status_code == 200:
      x = bs(source,'html.parser')
      avail_div = x.find('div',id = 'availability') # Locates div that contains availability information of the product using webscraping
      availability_status = avail_div.span.text.strip() # Then goes down the HTML tree to locate the first span element within the div and get the text within span
      print("Status code:",r.status_code)
      return availability_status
    
    else:
      return 'Status code not 200'
    
  except:
    return 'EXCEPTION'

'''Then want to check if on every request the availibility status has changed to "In stock."


If so then the bot is run, else: nothing happens and the page is continued to be scanned for any changes in stock. 

To prevent any mishaps 500 pounds will be put into the debit card to prevent the PS5 being bought more than once

Requests will be made using rotating proxies to ensure all request do not look like bot activity but happening by various different people in various different ip addresses in the UK

Requests will happen constantly with the use proxies that rotate

Proxies are provided using -  https://iproyal.com/

Proxies provided requires authentication using the HTTP

'''

condition = True # Conditon sers to boolean True 
while condition:
  '''Requests occurs within a infinite loop as the webpage wants to scanned constantly'''
  status = check_availability()
  if status == 'In stock.':
    '''IF block is triggered if status of product becomes availabile'''
    r = Robot('abdifatah.jama@icloud.com','Ronaldo81') # Creating robot object with login information initialised
    r.run() # Bot is ran
    condition = False # When bot is ran condition is set to False which terminates loop
  
  elif status == 'Currently unavailable.':
    '''ELSE block is triggered if status is anything than but availabilitye'''
    print('Currently not available ')
  
  else:
    pass



    