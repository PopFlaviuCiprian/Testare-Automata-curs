from browser import Browser
from selenium.webdriver.common.by import By


class HomePage(Browser):
    LOGHIN_PAGE = (By.LINK_TEXT, "Form Authentication")
    FILE_DWNL_PAGE = (By.LINK_TEXT, "File Download")
    DWNL_OBJECT = (By.LINK_TEXT, "LambdaTest.txt")
    JAVA_ALERT =(By.LINK_TEXT, "JavaScript Alerts")
    CLK_BTN = (By.XPATH, '//button[text()="Click for JS Confirm"]')


    # navigam catre homepage
    def go_to_home_page(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    # dam click pe linkul form_authentification
    def go_to_loghin(self):
        self.driver.find_element(*self.LOGHIN_PAGE).click()


    # dam click pe linkul Download_File si downloadam fisierul Lambda Test
    def go_to_page_file_dwnl(self):
        self.driver.find_element(*self.FILE_DWNL_PAGE).click()
        self.driver.find_element(*self.DWNL_OBJECT).click()

    #dam click pe linkul JavaScript Alerts
    def go_to_java_alerts(self):
        self.driver.find_element(*self.JAVA_ALERT).click()
        self.driver.find_element(*self.CLK_BTN).click()
        buton = self.driver.switch_to.alert
        print(f'Preluam textul de pe alerta care este {buton}')
        buton.accept()  # apasam ok pe buntonul alerta



