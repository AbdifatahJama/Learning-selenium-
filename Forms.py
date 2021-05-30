from socket import timeout
from string import Template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
import time
import random

PATH  = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# driver.get('https://docs.google.com/forms/d/e/1FAIpQLSf7KPbvQBlio1o498xr09AniiZYcwfQ5pAQ_hWdUxsSjsT_iw/viewform?vc=0&c=0&w=1&flr=0')

# # So the aim of this is to simulate filling in a form 
# # This includes filling in text inputs, checkboxes,radioboxes,dates,dropdown 

# # We can also find how many text inputs there by using the find elements method within webdriver. This will return a list of elements with the same indetifier(class). Normally use class as classes are not unique unlike IDs
# text = driver.find_elements_by_class_name('quantumWizTextinputPaperinputInput') # Returns the elements all with the class attribute 'quantumWizTextinputPaperinputInput'. Returns a list of each element(text box)

# # Filling in text boxes is as simple as indentifying how many text boxes then sending keys to each text box
# print('Number of short text boxes:',len(text))
# print(text)

# txtInputs = ['Abdifatah','Jama','20','Engineering','N/A']
# j = 0 # sets j varaible to 0 which will be used to iterate through txtInputs list when sending keys
# for i in text: # iterates through each text box element
#   i.send_keys(txtInputs[j]) # sends keys into each text box element by iterating through txtInputs via indexing
#   j+=1 # Increases index by 1 via each iteration
# print('FILLED')

# # Simulatating human interaction with radio button
# # radio buttons are a collection where only 1 button can be selected for each question
# # We can also check if a radio button is already selected by checking its status

# The following script involves filling text boxes,selecting radio buttons,checkboxes and dropdown columns

driver.get('https://iqssdss2020.pythonanywhere.com/tutorial/form/search')

# We can check how many text boxes there by using the text box class attribute. 
# Simalar text boxes (short answer text boxes) normally have the same class

text_boxes = driver.find_elements_by_id('search_name')
print(len(text_boxes)) # 1 text box as expected as it uses an ID

# We can now send keys to the text box 
for i in text_boxes:
  i.send_keys('James')
  
# We can now automate the clicking of radio boxes which only allows one radio button to be selected 

button5 = driver.find_element_by_id('p5') # Finds button 5 element using the elements id 
button5.click() # Radio box is then clicked() using clicked in button
print('Is button id5 selected:',button5.is_selected())
time.sleep(5)
button15 = driver.find_element_by_id('p15')
button15.click()
print('Is button id15 selected:',button15.is_selected())
print('Is button id5 still selected', button5.is_selected())
button10 = driver.find_element_by_id('p10')
print('Is button 10 clicked(not clicked yet):',button10.is_selected()) # Checks if radio button using 'is_selected method in selenium. Returns True/False'
button10.click()
print('Is button 10 selected:',button10.is_selected())
a = driver.find_elements_by_name('choice')
print(len(a))

random_button = random.choice(a)
random_button.click()
print('Succesful')

# Check boxes
# Check boxes are slighlty different radio boxes as check boxes mutiple check boxes can be checked(clicked)

# We want to click and check both privacy and terms and condition checkboxes within this script
# We first have to indetify each chechbox using its attributes

privacy_checkbox = driver.find_element_by_id('privacypolicy')
print('Is privacy checkbox checked(selected):',privacy_checkbox.is_selected()) # Again checks if checkbox has been selected using the 'is_selected' method in selenium
privacy_checkbox.click()
print('Is privacy checkbox checked(selected) now:',privacy_checkbox.is_selected())
print('-----------------')

terms_and_condition_checkbox = driver.find_element_by_id('termsconditions')
print('Is terms and conditon checkbox checked(selected):',terms_and_condition_checkbox.is_selected())
terms_and_condition_checkbox.click()
print('Is terms and conditon checkbox checked(selected):',terms_and_condition_checkbox.is_selected())

# Above shows how powerful the 'is_selected()' element is when checking/verifying whether radio buttons and check boxes are selected or not 

# Dropdown list are slighly different to radio boxes and checkboxes as dropdown buttons use select tags to make a dropdown list
# Therefore, to automate a user going through a dropdown list and selecting an option another module must be imported from webdriver

from selenium.webdriver.support.select import Select # Module required to work with dropdown list

dropdown_select = driver.find_element_by_id('search_grade') # Identifies dropdown list using id attribute
dropdown_object = Select(dropdown_select) # Uses Select module from selenium.webdriver libary to create select object with the dropdown variable created earlier 'dropdown_select'

# We can manipulate the select object created now by selecting options in dropdown list in different ways 
dropdown_object.select_by_visible_text('1') # Selecting option in dropdown list via visible text
time.sleep(3)
dropdown_object.select_by_index(0) # Selects options dropdown using index. Ie: index 0 is first option and index 1 is second option in dropdown list
time.sleep(3)
dropdown_object.select_by_value('3') # We can also select options in dropdown list via each options value within the html dom 
print('Succesfully automated drop down list using Select module from selenium libary')

# We can also deselect all options using the Select object created
# dropdown_object.deselect_all()

# We can then submit the form by finding the submit button attribute
submit = driver.find_element_by_name('q')
submit.click() # or submit.submit() can be used in forms, automates pressing the submit button
# Every element in selenium has a submit method. If this is called in a form the webdriver will crawl up the dom finding the submit button
 






























  
  
  



















