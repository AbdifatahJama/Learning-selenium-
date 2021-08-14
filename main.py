'''The following script is being used to make bot to purchase a PS5 which is currently in demand. The site being scraped is - https://www.argos.co.uk/?clickOrigin=header:search:argos+logo '''

import requests
import json
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
import time 
import random
import os
import shutil
from datetime import datetime,timedelta


PATH = 'C:\Program Files (x86)\chromedriver.exe' # Location of web driver file
driver = webdriver.Chrome(PATH) # Allows us to specify the browser we want to specify, in this case Chrome, the nessecary webdriver for the current chrome version is specified as an argument


class Robot:
  def __init__(self,username = '',password = ''):
    '''Initialising logins and link'''
    self.username = username
    self.password = password
    self.link = 'https://www.argos.co.uk/'
    self.product = 'PS5'
    driver.delete_all_cookies()
    driver.get(self.link)
    driver.fullscreen_window()
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
    login_boxes = driver.find_elements_by_class_name('form-control') # Two element with class name form control
    i = 1
    for form in login_boxes:
      '''Iterates through both login boxes and send keys that are stored in a dictionary object in the initialisation'''
      for char in self.dict[i]:
        form.send_keys(char)
        # time.sleep(0.3)
      i+=1 # Increment by 1 to get key for '2' in dictonary
    form.send_keys(Keys.RETURN) # Return key pressed which logs in if username and password succesful
    
  '''Then want click on PS5 product named - Sony PlayStation 5 Console'''
  def search_for_product(self):
    '''Then want to send keys of the product into search bar '''
    # list_of_char = self.product.split('-') # Creates list of charecters that split from the specified delimiter 
    try:
      time.sleep(5)
      '''Locates search bar to type product name'''
      search_bar = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.NAME, "searchTerm"))
      )
      '''Iterates through each charecter in the Product Name(Eg:PS5)'''
      for char in self.product:
        search_bar.send_keys(char)
        time.sleep(0.5)
      time.sleep(0.5)
      search_bar.send_keys(Keys.ENTER) # Search bar is entered
    
      
      product_name = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.LINK_TEXT, "FIFA 22 PS5 Game Pre-Order"))
    )
      product_name.click()
      
    except NoSuchElementException:
      print('EXCEPTION TRIGGERED IN SEARCH FOR PRODUCT SECTION 1')
      driver.quit()
      
    
      
      '''Explicit wait used to wait for presence of XPATH, add to trolley button is  located on web and clicked'''
      time.sleep(1)
      try:
        trolley_button = driver.find_element_by_css_selector('//*[@id="content"]/main/div[1]/div[3]/div[1]/section[2]/section/div[14]/div/div[2]/button') 
        trolley_button.click()
        print('Clicked function pressed')
      except NoSuchElementException :
        print('EXCEPTION TRIGGERED IN SEARCH FOR PRODUCT SECTION 2')
        print('ADD TO TROLLEY BUTTON IS NOT AVAILABLE SO PRODUCT IS NOT AVAILABLE ')
        driver.quit()
      
      '''To go to checkout page go to trolley button must be found '''
      try:
        go_to_trolley_btn = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.LINK_TEXT,'Go to\ntrolley'))
        )
        go_to_trolley_btn.click()
        
      except NoSuchElementException:
        '''If element is no located then exception blocked is triggered'''
        driver.quit()
      
    
      

    
  def accept_cookies(self):
    '''When website is first loaded up, user has to accept cookies'''
    cookies_button = driver.find_element_by_xpath('//*[@id="consent_prompt_submit"]') # locates button using the xpath
    cookies_button.click() # Clicks on to accept cookies
    '''Bot then wants to press account button to proceed to login page'''
    account_button = driver.find_element_by_link_text('Account')
    account_button.click()
    
  
  def scan(self):
    '''Scans for any changes on the website constantly to catch when product is available '''
    pass
    
r = Robot('abdifatah.jama@icloud.com','Ronaldo81.')
r.run()



    