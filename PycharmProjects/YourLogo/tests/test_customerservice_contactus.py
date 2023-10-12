import random
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from lib.constant import URL, LST_VISIBLE_TEXT, TEXT_MESSAGE, ALERT_MASSAGE, INVALID_EMAIL_MASSAGE, INVALID_REF_MASSAGE, \
    INVALID_SELECT_MASSAGE

fake_data = Faker()
""" test_customerservice_validinput : This method enter in to Yourlogo application and 
enters the valid input and verifies the message."""


def test_customerservice_validinput(driver):
    driver.get(URL)
    driver.find_element(By.XPATH, '//div[@id="contact-link"]/a').click()
    element = driver.find_element(By.ID, "id_contact")
    option = Select(element)
    for text in random.sample(LST_VISIBLE_TEXT, 1):
        option.select_by_visible_text(text)
    driver.find_element(By.ID, "email").send_keys("xyz@admin.com")
    driver.find_element(By.ID, "id_order").send_keys(fake_data.random_number(digits=8))
    driver.find_element(By.ID, "message").send_keys(TEXT_MESSAGE)
    driver.find_element(By.XPATH, "//button[@id ='submitMessage']").click()
    alert_message = driver.find_element(By.CSS_SELECTOR, "p.alert.alert-success")
    assert alert_message.text == ALERT_MASSAGE, "The Message is not Displayed"


""" test_customerservice_invalidinput : This method enter in to Yourlogo application and 
enters the invalid input and verifies the message."""


def test_customerservice_invalidinput(driver):
    driver.get(URL)
    driver.find_element(By.XPATH, '//div[@id="contact-link"]/a').click()
    element = driver.find_element(By.ID, "id_contact")
    option = Select(element)
    for text in random.sample(LST_VISIBLE_TEXT, 1):
        option.select_by_visible_text(text)
    driver.find_element(By.ID, "id_order").send_keys(fake_data.random_number(digits=8))
    driver.find_element(By.ID, "message").send_keys(TEXT_MESSAGE)
    send_button = driver.find_element(By.XPATH, "//button[@id ='submitMessage']")
    send_button.click()
    alert_message_email = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-danger'] ol li")
    assert alert_message_email.text == INVALID_EMAIL_MASSAGE, "The Message is not Displayed"
    driver.back()
    driver.find_element(By.ID, "email").send_keys("xyz@admin.com")
    driver.find_element(By.ID, "message").clear()
    send_button.click()
    alert_message_ref = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-danger'] ol li")
    assert alert_message_ref.text == INVALID_REF_MASSAGE, "The Message is not Displayed"
    driver.back()
    driver.find_element(By.ID, "message").send_keys(TEXT_MESSAGE)
    option.select_by_value(0)
    send_button.click()
    alert_message_dropdown = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-danger'] ol li")
    assert alert_message_dropdown.text == INVALID_SELECT_MASSAGE, "The Message is not Displayed"
