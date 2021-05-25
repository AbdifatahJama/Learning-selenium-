from types import DynamicClassAttribute
from selenium import webdriver
import time

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Further practising explicit waits

my_user_agent  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get('http://automationpractice.com/index.php') # Practise automation site
driver.fullscreen_window() # Makes browser full screen


try:
    sign_up_butt = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
      )
    sign_up_butt.click()
    email_login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_login.clear()
    email_login.send_keys('Jamaa061.309@gmail.com')
   
    password_login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwd"))
    )
    password_login.send_keys('Ronaldo81')
    
    press_butt = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "SubmitLogin"))
    )
    press_butt.click()
    print('SUCCESFUL LOGIN')
    driver.fullscreen_window()
    
except:
    driver.quit()
    print('EXCEPTION THROWN')

# Now we are on the main page after now we want to navigate to the t shirt section

try:
    product_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sf-menu clearfix menu-content"))
    )
    t_shirt_list = product_list.find_element_by_class_name('')
    t_shirt_list.find_element_by_link_text('T-shirts').click()
    
    
    add_to_cart_butt = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))
    )
    add_to_cart_butt.click()
    
except:
  print('ERROR THROWN')
  driver.quit()









 