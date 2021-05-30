from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Action chains automate different type of mouse movement and clicks, such a double click,long hold drag and drop etc

PATH  = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH) # We again have to make a driver instance of chrome webdriver. Uisng the path of the chrome driver that is the program files
# driver.get('http://essemble.co.uk/escript/drag_drop_engine/dragdrop1.html')
# time.sleep(5)
action  = ActionChains(driver)

drag = [driver.find_element_by_id('drag' + str(i)) for i in range(1,9,1)] # Creates a list of each element with id using list comprehension
print(drag)
drop = [driver.find_element_by_id('drop' + str(i)) for i in range(1,9)]
print(drop)
driver.fullscreen_window()
# We now have a list of each drag and drop element in their respective lists
# We can now use action chains

for i in range(0,8): # for loop that iterates through each list using indexing
  action.drag_and_drop(drag[i],drop[i]) # we then use the drag and drop method within the ActionChain object. drag is the source, drop is the target and we iterate through each respective list
action.perform() # When for loop is completed the action is peformed

time.sleep(2) # sleep for 2 seconds as button takes a couple seconds to become clickable after the dragging a dropping is complete 
# We then want to compelte the game by submitting and clicking the submit button
submit_button = driver.find_element_by_id('btn')
submit_button.click()

# # When done close the window
driver.quit()
print('Succesful Automation')

# Double clicking game
# The game that will be automated is double clicking the image constanlty resulting in the image to move around

driver.get('https://scraper.dev/test/1.html')

image = driver.find_element_by_id('block') # indentifies element using the elements id attribute
driver.fullscreen_window()
action.double_click(image) # Action double click method is used from the ActionChain object created. This automates a user double clicking on the element
action.perform() # Action is peformed

# We can double click constantly

for i in range(1,100):
  action.double_click(image)
  action.pause(1)
  action.perform()

# Action chains can be expanded in many ways on elements
# Action chains such as:
''' Click and hold
    Context click(right click)
    drag and drop
    key_down
    release
    move_to_element
    move_to_element_by_offset
    and plethora of other mouse movements within ActionChains object'''
    



  







  