"""

Xpath (XML Path Language) este un limbaj de expresii utilizat pentru a selecta portiuni dintr-un document XML (XHTML)


xpath este o modalitate prin care putem sa cautam un anumit element in HTML prin intermediul adresei sau distantei fata de inceputul fisierului HTML


EXEMPLU:
<input type="text" class="form-control" id="first-name" placeholder="Enter first name">


    full xpath = /html/body/div/form/div/div[1]/input

    xpath simplu = calea relativa = //input[@id='first-name'] sau //*[@id="first-name"] (* gaseste toate elementele)
    //              -> metoda de cautare care anunta sistemul ca nu va cauta de la inceput, ci pornind de la un element specific
    input           -> anuntam sistemul ca vrem sa sara la primul input gasit
    []              -> facem filtrarea pe baza unei perechi atribut=valoare
    @id=first-name  -> gasim elementele care indeplinesc aceasta conditie




x y axis navigation
cu parent in sus


cu /elem_type - ajungem la elementul copil
cu //elem_type - cauta prin toti descendentii

cu parent::elem_type - merge la parintele de tip elem_type
cu following-sibling - merge la fratele urmator de la acelasi nivel de tip elem_type
cu preceding-sibling - merge la fratele anterior de la acelasi nivel de tip elem_type

Navigarea din parinte in copil se face cu /
Navigarea din copil in parinte sau intre frati se face cu <selector>::

"""



from time import sleep
from selenium.webdriver.common.by import By               # librarie ce contine toate actiunile care se pot face in raport cu un element
from selenium import webdriver                            # pachet care contine functii si variabile utile pentru interactiunea cu browserul


# incepand cu selenium 4.6.0 nu mai este nevoie sa facem toate setarile
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com/form")


chrome.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Iulia")

sleep(3)

# gasim elementul de tip label care are textul exact 'First name', navigam in sus la parintele strong si apoi navigam la fratele lui input
chrome.find_element(By.XPATH, "//label[text()='First name']/parent::strong/following-sibling::input").clear()

sleep(3)

# gasim elementul de tip label care contine textul 'Last', navigam in sus la parintele strong si apoi navigam la fratele lui input
chrome.find_element(By.XPATH, "//label[contains(text(),'Last')]/parent::strong/following-sibling::input").send_keys("Victor")

sleep(3)

# verificam daca butonul este activ pe pagina
chrome.find_element(By.XPATH, "//a[contains(@class,'btn')]").is_enabled()

# text este o metoda care returneaza continutul text al elementului HTML (adica valoare care se alfa intre tag-uri, pe care o vedem vizibila pe interfata)
saved_text = chrome.find_element(By.XPATH, "//a[contains(@class,'btn')]").text
assert saved_text == 'Submit', 'Error, buton is not named correctly'

chrome.quit()