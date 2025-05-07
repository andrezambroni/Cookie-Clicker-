from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from webdriver_manager.chrome import ChromeDriverManager


class CookieClicker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {
            "buttons": {
                "cookie": {
                    "xpath": "/html/body/div/div[2]/div[15]/div[8]/button"
                },  # Corrigido o XPath do botão do cookie
                "upgrade": {
                    "xpath": "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]"
                },
            },
            "labels": {"money": {"xpath": "/html/body/div[2]/div[2]/div[15]/div[4]"}},
        }

        # Substituição do executable_path por Service
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def open_website(self):
        self.driver.get(self.SITE_LINK)
        try:
            # Aguarda o carregamento do botão do cookie ou do seletor de idioma
            self.wait.until(EC.presence_of_element_located((By.ID, "langSelect-PT-BR")))
            time.sleep(2)
        except Exception as e:
            print(f"Erro ao carregar o site: {e}")

    def accept_cookies(self):
        try:
            # Aguarda o botão "Got it!" estar visível e clicável
            cookies_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/a[1]"))
            )
            cookies_button.click()
            print("Cookies aceitos com sucesso.")
        except Exception as e:
            print(f"Erro ao aceitar os cookies: {e}")

    def select_language(self):
        try:
            # Aguarda o botão de seleção de idioma aparecer
            self.wait.until(EC.presence_of_element_located((By.ID, "langSelect-PT-BR")))
            # Clica no botão de idioma "Português"
            self.driver.find_element(By.ID, "langSelect-PT-BR").click()
            # Aguarda o site recarregar
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, self.SITE_MAP["buttons"]["cookie"]["xpath"])
                )
            )
            time.sleep(2)
        except Exception as e:
            print(f"Erro ao selecionar o idioma: {e}")

    def click_on_cookie(self):
        try:
            # Aguarda até que o botão do cookie esteja clicável
            cookie_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, self.SITE_MAP["buttons"]["cookie"]["xpath"])
                )
            )
            cookie_button.click()
        except Exception as e:
            print(f"Erro ao clicar no cookie: {e}")

    def get_current_money(self):
        money = self.driver.find_element(
            By.XPATH, self.SITE_MAP["labels"]["money"]["xpath"]
        ).text
        return money.split(" ")[0]

    def get_best_upgrade(self):
        found = False
        i = 2
        while not found:
            objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace(
                "$$NUMBER$$", str(i)
            )
            try:
                classes_objeto = self.driver.find_element(
                    By.XPATH, objeto
                ).get_attribute("class")
                if "enabled" not in classes_objeto:
                    found = True
                else:
                    i += 1
            except:
                found = True
        return i - 1

    def comprar_upgrade(self):
        objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace(
            "$$NUMBER$$", str(self.get_best_upgrade())
        )
        try:
            self.driver.find_element(By.XPATH, objeto).click()
        except:
            pass


cookie = CookieClicker()
cookie.open_website()
cookie.accept_cookies()  # Aceita os cookies
cookie.select_language()  # Seleciona o idioma "Português"

i = 0

while True:
    if i % 500 == 0 and i != 0:
        time.sleep(1)
        cookie.comprar_upgrade()
        time.sleep(1)

    cookie.click_on_cookie()
    i += 1
