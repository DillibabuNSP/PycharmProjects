import pytest
from faker import Faker
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


"""load_database: provieds the data to the database through python using SQL query"""


@pytest.fixture()
def load_database(database):
    dataBase, cursorObject = database
    faker = Faker()
    mySql_insert_query = "INSERT INTO web_table(FirstName,LastName,Age,Email,Salary,Department)VALUES(%s,%s,%s,%s,%s," \
                         "%s) "
    for index in range(7):
        records_to_insert = (
            faker.first_name(), faker.last_name(), faker.random_int(18, 60), faker.email(),
            faker.random_int(20000, 90000), faker.job())
        cursorObject.execute(mySql_insert_query, records_to_insert)
    dataBase.commit()
    cursorObject.execute("SELECT * FROM web_table")
    database_data = cursorObject.fetchall()
    return database_data


"""tester: provides thereusable methods to the test cases."""


@pytest.fixture()
def tester():
    action = Action()
    return action
