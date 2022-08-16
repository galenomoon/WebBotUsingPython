from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# contato@dentistaespecializado.com
# zetalana1970


def alert(type):
    if type == 'error':
        browser.close()
        print('🙁 Ops! Não consegui executar esse comando...')
    if type == 'line':
        print('-------------------------')
    return


def click(path):
    time.sleep(1)
    alert('line')
    print(f'Click em: {path}')
    # try:
    browser.find_element_by_xpath(path).click()
    # except:
    #     alert('error')
    return


def type_text(path, text):
    alert('line')
    print(f"Input {path} selecionado")
    time.sleep(1)
    # try:
    browser.find_element_by_xpath(path).send_keys(text)
    print(f"Texto digitado: {text}")
    # except:
    #     alert('error')
    return


def login(email, password):
    print('-------------------------')
    print("--- Efetuando Login ---")
    type_text('//*[@id="mui-1"]', email)
    type_text('//*[@id="mui-3"]', password)
    click('//*[@id="app-content"]/div/div[1]/div/div/div[4]/button')
    return


def register():
    # type_text('/html/body/md-content/div/div[7]/md-content/div/div[2]/div/form/div[1]/div[1]/input', 'email.do.usuario@teste.com')
    # type_text('//*[@id="Name"]', 'Frajola Santiago')
    click('//*[@id="insertMachine"]')
    click('//*[@id="cbo-mchstr-machine"]/option[6]')
    return


print('Olá, meu nome é')
print("   _____ ____   ____  ____  ___  _      ____\n  |     |    \ /    ||    |/   \| |    /    |\n  |   __|  D  |  o  ||__  |     | |   |  o  |\n  |  |_ |    /|     |__|  |  O  | |___|     |\n  |   _]|    \|  _  /  |  |     |     |  _  |\n  |  |  |  .  |  |  \  `  |     |     |  |  |\n  |__|  |__|\_|__|__|\____|\___/|_____|__|__|")
print('\nSeu robôzinho desenvolvido pra facilitar o seu trabalho! 🤖❤️')

alert('line')

# email = input('Digite seu email de acesso: ')
# password = input('Digite sua senha de acesso: ')

print('* Abrindo site e iniciando cadastro *')
browser = webdriver.Chrome(executable_path='/tmp/chromedriver')
browser.get('https://app.leadlovers.com/v4/OldLeads/Details')
login('contato@dentistaespecializado.com', 'zetalana1970')

print('Fechando Anuncios...')

time.sleep(13)
click('//*[@id="popup-news"]/div[2]/div/div[1]/button')
print('Anuncio fechado!')

register()

browser.close()
print('Cadastro concluído :D')
