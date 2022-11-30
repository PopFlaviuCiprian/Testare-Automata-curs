from time import sleep
from selenium.webdriver.common.by import By               # librarie ce contine toate actiunile care se pot face in raport cu un element
from selenium import webdriver                            # pachet care contine functii si variabile utile pentru interactiunea cu browserul
from selenium.webdriver.support.ui import Select


# incepand cu selenium 4.6.0 nu mai este nevoie sa facem toate setarile
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com/form")

# gaseste primul element doar si scrie in el
chrome.find_element(By.CLASS_NAME, "form-control").send_keys("TEST")

chrome.find_elements(By.CLASS_NAME, "form-control")[2].send_keys("TEST2222")


# pot sa selectez o optiune dintr-un dropdown
# chrome.find_elements(By.CLASS_NAME, "form-control")[3].click()
# chrome.find_elements(By.TAG_NAME, "option")[2].click()


# prin clasa Select selectam o optiune dintr-un dropdown prin textul vizibil de pe site al optiunii
Select(chrome.find_elements(By.CLASS_NAME, "form-control")[3]).select_by_visible_text("5-9")
Select(chrome.find_elements(By.CLASS_NAME, "form-control")[3]).select_by_index(1)
Select(chrome.find_elements(By.CLASS_NAME, "form-control")[3]).select_by_value("4")


sleep(5)

chrome.quit()