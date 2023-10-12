import random

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from lib.action import Action
from lib.constant import BROWSERNAME
from selenium.webdriver.edge.service import Service as EdgeService
import mysql.connector

"""driver: passes the webdriver to the test cases"""


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


"""database: connect to the database through python"""


@pytest.fixture()
def database():
    dataBase = mysql.connector.connect(host='localhost', user='root', password='babu@2171', database='toolsqa')
    cursorObject = dataBase.cursor()
    yield dataBase, cursorObject


"""filter_data: provides the data to the database through python using SQL query"""


@pytest.fixture()
def filter_data(database):
    dataBase, cursorObject = database
    salary = random.randint(20000, 50000)
    Age_1 = random.randint(25, 45)
    Age_2 = random.randint(25, 45)
    records = (salary, Age_1, Age_2)
    cursorObject.execute("UPDATE toolsqaweb_tables SET Salary = %s WHERE Age BETWEEN %s AND %s ", records)
    dataBase.commit()
    cursorObject.execute("SELECT * FROM toolsqaweb_tables WHERE Salary = %s", [salary])
    myresult = cursorObject.fetchall()
    return myresult, salary


"""tester: provides thereusable methods to the test cases."""


@pytest.fixture()
def tester():
    action = Action()
    return action
