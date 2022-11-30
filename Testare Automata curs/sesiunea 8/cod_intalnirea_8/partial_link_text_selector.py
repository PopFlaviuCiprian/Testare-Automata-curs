"""

Face acelasi lucru ca si linkText, doar ca va cauta partial, asa cum spune si denumirea

"""

from time import sleep
from selenium.webdriver.common.by import By               # librarie ce contine toate actiunile care se pot face in raport cu un element
from selenium import webdriver                            # pachet care contine functii si variabile utile pentru interactiunea cu browserul


# incepand cu selenium 4.6.0 nu mai este nevoie sa facem toate setarile
chrome = webdriver.Chrome()


chrome.get("https://formy-project.herokuapp.com/")


chrome.find_element(By.PARTIAL_LINK_TEXT, "Autoc").click()

sleep(3)