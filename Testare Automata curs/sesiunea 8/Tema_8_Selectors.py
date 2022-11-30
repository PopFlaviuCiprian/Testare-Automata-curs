from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome = webdriver.Chrome()

chrome.maximize_window()

'''
By ID Selector
'''
chrome.get('https://www.phptravels.net')

nume = chrome.find_element(By.ID, 'checkin').click()

chrome.find_element(By.ID, 'checkout').click()

sleep(3)

'''
By Link Text selector
'''
chrome.get('https://the-internet.herokuapp.com/')

try:
    chrome.find_element(By.LINK_TEXT, 'A/B Testing').click()
except:
    print('Elementul nu a fost gasit, la revedere')


sleep(5)

'''
By Partial link text
'''

chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Float',).click()
sleep(5)

'''
By name selector
'''
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.NAME, 'firstname',).send_keys('Cipri')
chrome.find_element(By.NAME, 'lastname',).send_keys('POP')
sleep(3)

'''
By Tag Name selector
'''
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.TAG_NAME, 'input',).send_keys('Aici avem inputul')
sleep(3)


'''
By Class_Name
'''
chrome.get('https://formy-project.herokuapp.com/keypress')
chrome.find_element(By.CLASS_NAME,"form-control").send_keys('salut')
sleep(3)

'''
By CSS selector
'''
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.CSS_SELECTOR, 'input#datepicker').send_keys('data curenta')   # css selector dupa id
Select(chrome.find_element(By.CSS_SELECTOR, '.input-xlarge')).select_by_index(1) # css selector dupa clasa
chrome.find_element(By.CSS_SELECTOR,' #profession-1').click() # css selector dupa valoare partiala
sleep(10)

'''
By X_path selector
'''

chrome.get('https://phptravels.net/')
chrome.find_element(By.XPATH,'//input[@id="checkin"]').click()  # atribut valoare
chrome.find_element(By.XPATH,'//input[@id="checkout"]').click()
chrome.find_element(By.XPATH,'//input[@id="checkin"]').click()
sleep(10)


chrome.get('https://formy-project.herokuapp.com/dropdown')
chrome.find_element(By.XPATH, "//button[contains(text(),'Dropdown')]").click()  # dupa text
sleep(3)

chrome.get('https://formy-project.herokuapp.com/modal')
chrome.find_element(By.XPATH, "//button[contains(text(),'Open modal')]").click()  # dupa text
sleep(3)

chrome.get('https://formy-project.herokuapp.com/fileupload')
chrome.find_element(By.XPATH, "//button[contains(text(),'Choose')]").click()  # dupa text
sleep(3)

chrome.get('https://formy-project.herokuapp.com/modal')
chrome.find_element(By.XPATH, "//button[contains(text(), 'mo')]").click() # dupa text partial
sleep(3)

#  //*
chrome.get("https://formy-project.herokuapp.com/autocomplete")
chrome.find_element(By.XPATH, "//*[@id='autocomplete']").send_keys("Adresa mail")
sleep(5)

#  dupa index
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[5]').send_keys('Cod postal')
sleep(5)

# parinte
salvare_text = chrome.find_element(By.XPATH,"//label[contains(text(), 'Street address')]/parent::strong").text
print(salvare_text)
sleep(5)

# descendent
chrome.find_element(By.XPATH,"//label[contains(text(), 'Address')]/parent::strong/following-sibling::input").send_keys("xyz@gmail.com")
sleep(5)


#  dupa | (sau)
chrome.get("https://formy-project.herokuapp.com/buttons")
chrome.find_element(By.XPATH, "//button[contains(text(), 'Left')] | //button[contains(text(), 'Danger')] | //button[contains(text(), 'Info')]").click()
sleep(10)