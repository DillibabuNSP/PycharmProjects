from selenium.webdriver.common.by import By

from lib.constant import URL, ENTERED_FIRST_LIST, ENTERED_LAST_LIST

"""test_validate_users : validates the elements passed on the ToolQA website through database with the data present in 
the database. Faker is used for  entering the data in the database."""


def test_validate_users(driver, tester, load_database):
    driver.get(URL)
    for data in load_database:
        tester.elementToClick(driver.find_element(By.ID, "addNewRecordButton"))
        tester.enterTextValue(driver.find_element(By.ID, "firstName"), data[0])
        tester.enterTextValue(driver.find_element(By.ID, "lastName"), data[1])
        tester.enterTextValue(driver.find_element(By.ID, "userEmail"), data[3])
        tester.enterTextValue(driver.find_element(By.ID, "age"), data[2])
        tester.enterTextValue(driver.find_element(By.ID, "salary"), data[4])
        tester.enterTextValue(driver.find_element(By.ID, "department"), data[5])
        tester.elementToClick(driver.find_element(By.ID, "submit"))
    entered_first_name = driver.find_elements(By.XPATH,
                                              "//div[@class='ReactTable -striped -highlight']/div/div[2]/div/div/div[1]")
    entered_last_name = driver.find_elements(By.XPATH,
                                             "//div[@class='ReactTable -striped -highlight']/div/div[2]/div/div/div[2]")

    for firstname, lastname in zip(entered_first_name, entered_last_name):
        ENTERED_FIRST_LIST.append(firstname.text)
        ENTERED_LAST_LIST.append(lastname.text)
    merged_list = [(ENTERED_FIRST_LIST[values], ENTERED_LAST_LIST[values]) for values in
                   range(0, len(ENTERED_FIRST_LIST))]
    for data in load_database:
        assert (data[0], data[1]) in merged_list
