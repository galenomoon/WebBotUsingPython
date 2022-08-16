from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



def alert(type):
    if type == 'error':
        browser.close()
        print('🙁 Ops! Não consegui executar esse comando...')
    if type == 'line':
        print('-------------------------')
    return

def click(path):
    alert('line')
    print(f'Click em: {path}')
    try:
        browser.find_element_by_xpath(path).click()
    except:
        alert('error')
    return

def type_text(path, text):
    alert('line')
    print(f"Input {path} selecionado")
    try:
        browser.find_element_by_xpath(path).send_keys(text)
        print(f"Texto digitado: {text}")
    except:
        alert('error')
    return

def login(email, password):
    print('-------------------------')
    print("--- Efetuando Login ---")
    type_text('//*[@id="mui-1"]', email)
    type_text('//*[@id="mui-3"]', password)
    click('//*[@id="app-content"]/div/div[1]/div/div/div[4]/button')
    return

def register():
    type_text('//*[@id="Email"]', 'email.do.usuario@teste.com')
    type_text('//*[@id="Name"]', 'Frajola Santiago')
    click('//*[@id="insertMachine"]')
    click('//*[@id="cbo-mchstr-machine"]/option[6]')
    return

print('===== TESTE =====')
email = input('Digite seu email de acesso: ')
password = input('Digite sua senha de acesso: ')

print('* Abrindo site e iniciando cadastro *')
browser = webdriver.Chrome(executable_path='/tmp/chromedriver')
browser.get('https://app.leadlovers.com/v4/OldLeads/Details')
login(email, password)
time.sleep(4)
click('//*[@id="popup-news"]/div[2]/div/div[1]/button')

register()

browser.close()
print('Cadastro concluído :D')
