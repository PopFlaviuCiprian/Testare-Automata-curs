"""

EX element HTML:
<input type="text" class="form-control" id="first-name" placeholder="Enter first name">

id = atributul
first-name = valoarea atributului

"""
from time import sleep
from selenium.webdriver.common.by import By               # librarie ce contine toate actiunile care se pot face in raport cu un element
from selenium import webdriver                            # pachet care contine functii si variabile utile pentru interactiunea cu browserul
from selenium.webdriver.chrome.service import Service     # clasa care contine instanta de driver
from webdriver_manager.chrome import ChromeDriverManager  # contine functii si variabile utile pentru a lansa driverul


# initializam chrome
# s = Service(ChromeDriverManager().install())    # momentul in care noi instalam toate pachetele necesare la run-time pentru rularea driverului
# chrome = webdriver.Chrome(service=s)            # lansam browserul de chrome si il salvam intr-o variabila


# incepand cu selenium 4.6.0 nu mai este nevoie sa facem toate setarile de la 13-14
chrome = webdriver.Chrome()

chrome.get('https://formy-project.herokuapp.com/form')       # metoda get este o metoda prin care putem naviga la un anumit link

sleep(3)     # sleep este o metoda prin care punem pauza codului
             # ii spunem sistemului sa astepte 3 secunde inainte sa execute urmatoarele instructiuni


# <input type="text" class="form-control" id="first-name" placeholder="Enter first name">
name = chrome.find_element(By.ID, "first-name")

# metoda send_keys este o metoda pe care o folosim sa scriem intr-un camp din pagina
name.send_keys("Andrei")

# metoda chaining (adica in lant)
chrome.find_element(By.ID, "last-name").send_keys("Popescu")

sleep(2)

name.clear()

sleep(2)

chrome.quit()               # este o metoda folosita pentru a inchide browserul (implicit toate tab-urile)

# chrome.close()            # metoda care inchide tab-ul curent





