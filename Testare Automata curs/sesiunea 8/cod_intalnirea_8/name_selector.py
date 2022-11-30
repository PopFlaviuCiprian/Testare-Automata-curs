


from time import sleep
from selenium.webdriver.common.by import By               # librarie ce contine toate actiunile care se pot face in raport cu un element
from selenium import webdriver                            # pachet care contine functii si variabile utile pentru interactiunea cu browserul


# incepand cu selenium 4.6.0 nu mai este nevoie sa facem toate setarile
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

chrome.get("http://www.seleniumframework.com/Practiceform/")


# selector by name
chrome.find_element(By.NAME, "country").send_keys("Romania")

chrome.find_element(By.NAME, "company").send_keys("IT Factory")


# am gasit in pagina 2 elemente care indeplinesc criteriul name="email"
# sa vedem cum functioneaza find_element si find_elements

# daca exista mai multe elemente si folosim find_element va lua primul element gasit pe pagina tot timpul
chrome.find_element(By.NAME, "email").send_keys("1111111111")

# prin find_elements imi va gasi toate elementele care indeplinesc conditia si le pune intr-o lista
# am accesat primul element din lista si am introdus text in el
chrome.find_elements(By.NAME, "email")[0].send_keys("000000")

# am accesat al doilea element din lista si am introdus text in el
chrome.find_elements(By.NAME, "email")[1].send_keys("2222222")

sleep(5)