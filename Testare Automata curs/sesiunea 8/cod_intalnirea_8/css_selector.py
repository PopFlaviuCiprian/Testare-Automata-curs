from time import sleep
from selenium.webdriver.common.by import By               # librarie ce contine toate actiunile care se pot face in raport cu un element
from selenium import webdriver                            # pachet care contine functii si variabile utile pentru interactiunea cu browserul


# incepand cu selenium 4.6.0 nu mai este nevoie sa facem toate setarile
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com/form")


chrome.find_element(By.CSS_SELECTOR, "input#first-name").send_keys("Iulia")    #   #(diez) = identificator pentru id in HTML/CSS

sleep(2)
# .(punct) = identificator pentru clasa in HTML/CSS
chrome.find_elements(By.CSS_SELECTOR, '.form-control')     # va gasi toate elementele care au clasa form-control (indiferent de tag name)
chrome.find_element(By.CSS_SELECTOR, 'select.form-control')  # va gasi toate elementele cu tag-ul select care au clasa form-control
chrome.find_element(By.CSS_SELECTOR, 'input.form-control')  # va gasi toate elementele cu tag-ul input care au clasa form-control


# selector by css - atribut = valoare
# [] = identificator pentru atribut = valoare

chrome.find_element(By.CSS_SELECTOR, "input[value='radio-button-1']").click()


# <input type="text" class="form-control" id="last-name" placeholder="Enter last name">
chrome.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']").send_keys("Popescu")

# folosind * am facut o cautare pentru o valoare partiala
chrome.find_element(By.CSS_SELECTOR, "input[placeholder*='last name']").send_keys("1111111")


sleep(3)

chrome.quit()