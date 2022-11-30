from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


# initializam chrome
chrome = webdriver.Chrome()

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/form')

# selenium va cauta toate elementele timp de x secunde
chrome.implicitly_wait(5)

# explicit wait                                 presence_of_element_located((x, y))
# aici gaseste elementul instant, nu e nevoie sa faca wait explicit de 15 sec
first_name = WebDriverWait(chrome, 15).until(EC.presence_of_element_located((By.ID, 'first-name')))
first_name.send_keys('Iulia')

# aici se va astepta implicit
# gaseste elementul instant, nu e nevoie sa faca wait implicit de 5 sec
chrome.find_element(By.ID, 'last-name').send_keys('Albu')



try:
    # explicit wait
    # nu va gasi elementul, va astepta 15 sec timp in care in continuu va cauta elementul
    # iar dupa 15 sec nu il va gasi => eroare
    first_name_2 = WebDriverWait(chrome, 15).until(EC.presence_of_element_located((By.ID, 'first-names')))
    first_name_2.send_keys('Iulia')
except Exception as e:
    print(f'Am cautat elementul timp de 15 secunde in continuu si nu l-am gasit la final: {e}')


# aici se va astepta implicit
# va astepta 5 secunde timp in care va cauta elementul in continuu
# la final nu il va gasi si va da eroare
chrome.find_element(By.ID, 'last-names').send_keys('Albu')

chrome.quit()