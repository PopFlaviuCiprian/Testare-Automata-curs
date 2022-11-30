from time import sleep
from selenium.webdriver.common.by import By               # librarie ce contine toate actiunile care se pot face in raport cu un element
from selenium import webdriver                            # pachet care contine functii si variabile utile pentru interactiunea cu browserul


# incepand cu selenium 4.6.0 nu mai este nevoie sa facem toate setarile
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com/form")


# gaseste primul element care indeplineste conditia tot timpul
chrome.find_element(By.TAG_NAME, "input").send_keys("TEST")

# gaseste toate elementele care indeplinesc conditia si il accesam pe al treilea prin index [2]
chrome.find_elements(By.TAG_NAME, "input")[2].send_keys("TEST2222")

sleep(5)

chrome.quit()