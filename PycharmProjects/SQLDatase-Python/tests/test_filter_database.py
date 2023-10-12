from selenium.webdriver.common.by import By
from lib.constant import URL, PRODUCT_LIST, PRICE_LIST, SORTED_PRODUCT_LIST, SORTED_PRICE_LIST

"""test_filter_method gets login as the user and gets the name and price of the product and stores in Database. 
Applying the filter and taking the name,price of the product  and validate with the database. Finally the database is 
tear down """


def test_filter_validate_database(driver, database, tester):
    dataBase, cursorObject = database
    driver.get(URL)
    tester.enterTextValue(driver.find_element(By.ID, "user-name"), "standard_user")
    tester.enterTextValue(driver.find_element(By.ID, "password"), "secret_sauce")
    tester.elementToClick(driver.find_element(By.ID, "login-button"))
    product_name = driver.find_elements(By.XPATH, '//a[@href="#"]/div')
    product_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    for name, price in zip(product_name, product_price):
        PRODUCT_LIST.append(name.text)
        PRICE_LIST.append(price.text)
    product_name_data = "INSERT INTO product_table(ProductName,ProductPrice)VALUES(%s,%s)"
    for index in range(len(PRODUCT_LIST)):
        cursorObject.execute(product_name_data, (PRODUCT_LIST[index], PRICE_LIST[index],))
    dataBase.commit()
    cursorObject.execute("SELECT * FROM product_table")
    database_data = cursorObject.fetchall()
    tester.selectByValue(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"),'za')
    sorted_product_name = driver.find_elements(By.XPATH, "//a[@href='#']/div")
    sorted_product_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    for name, price in zip(sorted_product_name, sorted_product_price):
        SORTED_PRODUCT_LIST.append(name.text)
        SORTED_PRICE_LIST.append(price.text)
    merged_list = [(SORTED_PRODUCT_LIST[values], SORTED_PRICE_LIST[values]) for values in
                   range(0, len(SORTED_PRODUCT_LIST))]
    for data in database_data:
        assert data in merged_list
