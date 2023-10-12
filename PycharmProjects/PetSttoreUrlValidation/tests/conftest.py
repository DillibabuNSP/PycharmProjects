import pytest
from selenium import webdriver
from lib.constant import constant


@pytest.fixture()
def init_driver():
    web_driver = webdriver.Chrome(executable_path=constant.Chrome_Path)
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()
