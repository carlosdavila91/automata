from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

def page_is_loaded(driver):
    return driver.find_elements_by_tag_name('body') != None

driver = webdriver.Firefox()

driver.get('https://sede.administracionespublicas.gob.es/icpplus/index.html')

wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

province = 'Barcelona'
certificates = 'Certificados UE.'
tramit = 'POLICIA-CERTIFICADOS UE'
passport_number = 'xxxxxxxxx'
name = 'xxxxxxxxx'

for x in range (0,5):
    provincias = driver.find_elements_by_tag_name('option')
    for p in provincias:
        if p.text == province:
            p.click()
            break

    certificados = driver.find_elements_by_tag_name('a')
    for c in certificados:
        if c.text == certificates:
            c.click()
            break
    tramites = driver.find_elements_by_tag_name('option')
    for t in tramites:
        if t.text == tramit:
            t.click()
            break

    driver.find_element_by_id('btnAceptar').click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.find_element_by_id('btnEntrar').click()

    driver.find_element_by_xpath("//input[@value='Pasaporte / Documento de identidad']").click()

    pasaporte = driver.find_element_by_id('txtIdCitado')
    pasaporte.send_keys(passport_number)

    nombre = driver.find_element_by_id('txtDesCitado')
    nombre.send_keys(name)

    break
