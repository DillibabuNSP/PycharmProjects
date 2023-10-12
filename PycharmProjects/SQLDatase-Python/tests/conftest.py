import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from lib import action
from lib.action import Action
from lib.constant import BROWSERNAME
from selenium.webdriver.edge.service import Service as EdgeService
import mysql.connector


@pytest.fixture()
def driver():
    if BROWSERNAME == 'Firefox':
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif BROWSERNAME == 'Chrome':
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif BROWSERNAME == 'MSEdge':
        web_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@pytest.fixture()
def database():
    dataBase = mysql.connector.connect(host='localhost', user='root', password='babu@2171', database='product')
    cursorObject = dataBase.cursor()
    yield dataBase, cursorObject
    cursorObject.execute("DELETE FROM product_table")
    dataBase.commit()


@pytest.fixture()
def tester():
    action = Action()
    return action
