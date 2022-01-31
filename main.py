"""

OBS:
1- Primeiramente instale um executavel chamado chromedriver.exe link downloads
para linux ou windowns: https://chromedriver.chromium.org/downloads
e so jogar na raiz da sua pasta onde esta o seu codigo
"""

from email import message
from webbrowser import Chrome
import pyautogui
from selenium import webdriver
from time import sleep


class BotPostarFoto:
    def __init__(self):
        self.nome_fotos = [] # caminho das fotos
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.chrome = webdriver.Chrome(executable_path='./chromedriver.exe') # este self.chrome serve para abrir o chromedriver.exe quando ele for chamado
        
    def acessar_site(self, link):
        self.chrome.get(link)
    
    
    def sair_chrome(self):
        self.chrome.close()
        
    
    def postar_foto(self):
        agora_nao = self.chrome.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
        agora_nao.click()
        sleep(1)
        for t in self.nome_fotos:
            sleep(2)
            bt_add_foto = self.chrome.find_element_by_css_selector('#react-root > div > div > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(3) > div > button > div > svg')
            bt_add_foto.click()
            
            bt_selecionar_foto = self.chrome.find_element_by_css_selector('body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.uYzeu > div._C8iK > div > div > div.qF0y9.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.kEKum > div > button')
            bt_selecionar_foto.click()
            sleep(3)
        
        
            for l in t:
               pyautogui.keyDown(l)
               pyautogui.keyUp(t)
        
            sleep(1)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            sleep(3)
            
            bt_avancar = self.chrome.find_element_by_css_selector('body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div:nth-child(3) > div > button')
            bt_avancar.click()

            bt_avancar2 = self.chrome.find_element_by_css_selector('body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div:nth-child(3) > div > button')
            bt_avancar2.click()
            sleep(2)
            
            bt_compartilhar = self.chrome.find_element_by_css_selector('body > div.RnEpo.gpWnf.Yx5HN > div.pbNvD > div > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div:nth-child(3) > div > button')
            bt_compartilhar.click()
            
            sleep(5)
            bt_fechar = self.chrome.find_element_by_css_selector('body > div.RnEpo.gpWnf.Yx5HN > div.NOTWr > button > div > svg')
            bt_fechar.click()
        
        
    def connectar_intagram(self):
        nome_usuario = self.chrome.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
        nome_usuario.click()
        nome_usuario.send_keys('')
        
        senha_usuario = self.chrome.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
        senha_usuario.click()
        senha_usuario.send_keys('')
        
        
    def conectar_pelo_face(self):
        bt_conect_face = self.chrome.find_element_by_css_selector('#loginForm > div > div:nth-child(5) > button > span.KPnG0')
        bt_conect_face.click()
        sleep(2)
        
        email_ou_numeroTL = self.chrome.find_element_by_css_selector('#email')
        email_ou_numeroTL.send_keys('') # seu email do facebook
        
        senha_face = self.chrome.find_element_by_css_selector('#pass')
        senha_face.click()
        senha_face.send_keys('') # sua senha do facebook
        
        bt_entrar = self.chrome.find_element_by_css_selector('#loginbutton')
        bt_entrar.click()
        
              
if __name__ == '__main__':
    bot = BotPostarFoto()
    bot.acessar_site('https://www.instagram.com/')
    sleep(3)
    bot.conectar_pelo_face()
    sleep(10)
    bot.postar_foto()
    bot.sair_chrome()