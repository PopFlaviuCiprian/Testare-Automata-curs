"""
Selectia elementelor in pagina cu linkText identifica hyperlink-urile <a> din HTML folosind text-ul care este afisat in pagina defapt
Cum spune si denumirea com lua link-ul in functie de text
Textul pe care il dam noi aici in cod trebuie sa se potriveasca 100% cu text-ul de la <a> folosit in codul HTML al paginii pe care o testam


EX:
<a class="btn btn-lg" href="/autocomplete">Autocomplete</a>

a = este un tag care defineste un element de tip ancora (adica link catre alta pagina)
href = linkul efectiv catre care se navigheaza. De obicei nu se pune linkul complet (cum vedem noi in browser), ci doar o extensie a domeniului
        https://formy-project.herokuapp.com/autocomplete - link complet
        /autocomplete - extensia
        formy-project.herokuapp.com - domeniu

"""


from time import sleep
from selenium.webdriver.common.by import By               # librarie ce contine toate actiunile care se pot face in raport cu un element
from selenium import webdriver                            # pachet care contine functii si variabile utile pentru interactiunea cu browserul


# incepand cu selenium 4.6.0 nu mai este nevoie sa facem toate setarile
chrome = webdriver.Chrome()


chrome.get("https://formy-project.herokuapp.com/")


chrome.find_element(By.LINK_TEXT, "Autocomplete").click()


sleep(2)

chrome.find_element(By.ID, "logo").click()

sleep(2)

chrome.find_element(By.LINK_TEXT, "Drag and Drop").click()

# am pus intr-un try except pentru ca elementul nu se gaseste si sa nu mi se opreasca rularea
try:
    chrome.find_element(By.LINK_TEXT, "Autocomplet").click()
except:
    print("Nu s-a gasit elemtentul")

sleep(3)

chrome.quit()
