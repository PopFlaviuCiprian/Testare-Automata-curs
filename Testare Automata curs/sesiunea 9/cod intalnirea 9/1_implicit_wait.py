from selenium.webdriver.common.by import By
from selenium import webdriver

# initializam chrome
chrome = webdriver.Chrome()

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/form')


"""
Exemplu: Vrem sa cautam un elemnt cu id-ul first-name pe pagina
Sistemul va cauta acel element, si daca il va gasi, va trece instant la urmatoarea instructiune

Daca nu il gaseste, sistemul va continua sa il caute pe toata durata stabilita in implicit wait
si daca nu il gaseste pana la finalul duratei, va returna eroare

Daca nu am avea  acel implicit wait, atunci va returna eroare instant
"""

chrome.implicitly_wait(10)

# aici a gasit elementul instant pentru ca exista in pagina, nu a fost nevoie sa astepte 6 sec
chrome.find_element(By.ID, 'first-name').send_keys("Iulia")

print('Instructiunea urmatoare 1')

# chrome.implicitly_wait(2)  # aici s-a suprascris primul implicit wait pus in fisier

# element cu id-ul dat nu exista in pagina
# va astepta 6 secunde, timp in care va cauta in continuu elementul
# cand expira cele 6 secunde iar elem nu a fost gasit => eroare
chrome.find_element(By.ID, 'first-name-fdhkfjshdkj').send_keys("Nu gasesc")

print('Instructiunea urmatoare 2')

chrome.quit()

"""
Setam implicit wait in secunde:
    - o modalitate prin care definim un timp global de asteptare pana cand sa dea eroare cand un element nu e gasit
    - se va instantia in momentul in care va fi executat instructiunea de implicit wait si va fi distrus in momentul in care executie se incheie si browser

Selenium va cauta toate elemtele timp de x secunde

Diferenta intre implicit wait si sleep este ca instructiunea de sleep va astepta orice ar fi(va pune pauza in cod orice ar fi):
iar implicit wait continua sa caute in acel nr de secunde elementul (vezi explicatie mai sus)
"""