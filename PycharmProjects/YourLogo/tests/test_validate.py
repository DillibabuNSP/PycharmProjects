from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


def test_validate():

    options = Options()
    options.binary_location = r'C:\Users\dillibabu.nsp\AppData\Local\Mozilla Firefox'
    driver = webdriver.Firefox(executable_path=r'C:\Users\dillibabu.nsp\drivers\geckodriver.exe', options=options)
    driver.get('http://google.com/')
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # driver.get("http://google.co.in")
