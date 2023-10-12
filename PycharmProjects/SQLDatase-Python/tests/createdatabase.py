import mysql.connector


def sample():
    dataBase = mysql.connector.connect(host='localhost', user='root', password='babu@2171')
    cursorObject = dataBase.cursor()
    cursorObject.execute("DROP DATABASE IF EXISTS Divison")
    cursorObject.execute("Create database Division")
    table_name = "CREATE TABLE 'Division'.'department'(product_name VARCHAR(50))"
    cursorObject.execute(table_name)


sample()
