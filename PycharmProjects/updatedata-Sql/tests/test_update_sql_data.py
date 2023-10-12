import random

import pytest
from faker import Faker
from selenium.webdriver.common.by import By

from lib.constant import URL


@pytest.fixture()
def update_sql_data(driver, database):
    driver.get(URL)
    elemt = []
    for rows in range(1, 4):
        row = []
        for column in range(1, 7):
            webelement = driver.find_element(By.XPATH,
                                             "//div[@class='rt-tbody']/div[" + str(rows) + "]/div/div[" + str(
                                                 column) + "]")
            row.append(webelement.text)
        elemt.append(row)
    dataBase, cursorObject = database
    mySql_insert_query = "INSERT INTO toolsqaweb_tables(FirstName,LastName,Age,Email,Salary,Department)VALUES(%s,%s," \
                         "%s,%s,%s,%s) "
    for index in elemt:
        records_to_insert = (index[0], index[1], index[2], index[3], index[4], index[5])
        cursorObject.execute(mySql_insert_query, records_to_insert)
    dataBase.commit()
    cursorObject.execute("SELECT Salary FROM toolsqaweb_tables")
    before_result = cursorObject.fetchall()
    return before_result


def test_filter_database(database, update_sql_data):
    faker = Faker()
    dataBase, cursorObject = database
    salary = faker.random_int(20000, 90000)
    Age_1 = random.randint(25, 45)
    Age_2 = random.randint(25, 45)
    records = (salary, Age_1, Age_2)
    cursorObject.execute("UPDATE toolsqaweb_tables SET Salary = %s WHERE Age BETWEEN %s AND %s ", records)
    dataBase.commit()
    cursorObject.execute("SELECT Salary FROM toolsqaweb_tables")
    after_result = cursorObject.fetchall()
    after_result_list=[]
    before_result_list = []
    for i in after_result:
        name = int(''.join(map(str, i)))
        after_result_list.append(name)
    print(after_result_list)
    for j in update_sql_data:
        name = int(''.join(map(str, j)))
        before_result_list.append(name)
    print(before_result_list)
    assert after_result_list != before_result_list
    # assert all([after != before for after, before in zip(after_result_list, before_result_list)])
