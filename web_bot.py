from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def click(path):
 print('-------------------------')
 time.sleep(1)
 print(f'Click em: {path}')
 return browser.find_element_by_xpath(path).click()

def type_text(path, text):
 print('-------------------------')
 time.sleep(1)
 print(f"Input {path} selecionado")
 print(f"Texto digitado: {text}")
 return browser.find_element_by_xpath(path).send_keys(text)

browser = webdriver.Firefox()

print('===== Cadastrador de Emails Automatico do Galeno =====')
print('* Abrindo site e iniciando cadastro *')
browser.get('https://signup.live.com/')
type_text('//*[@id="MemberName"]', 'luana.2108santiago@outlook.com')
click('//*[@id="iSignupAction"]')
click('//*[@id="ShowHidePasswordCheckbox"]')
type_text('//*[@id="PasswordInput"]', '123lkjaslkj981239KJK')
click('//*[@id="iSignupAction"]')
type_text('//*[@id="FirstName"]', 'Luana')
type_text('//*[@id="LastName"]', 'Santiago')
click('//*[@id="iSignupAction"]')
browser.close()
print('Cadastro concluído :D')
