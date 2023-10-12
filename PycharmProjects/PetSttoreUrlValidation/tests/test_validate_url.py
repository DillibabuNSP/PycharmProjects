import random
import time

from selenium.webdriver.common.by import By
from lib.constant import constant


def test_validate_image_url(init_driver):
    init_driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    init_driver.find_element(By.XPATH, "//div[@id='MenuContent']/a[2]").click()
    init_driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Ajay")
    init_driver.find_element(By.XPATH, "//input[@name='password']").clear()
    init_driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Ajay")
    init_driver.find_element(By.XPATH, "//input[@name='signon']").click()
    pet_division = init_driver.find_elements(By.XPATH, "//div[@id='SidebarContent']/a/img")
    for pet in random.sample(pet_division, 1):
        for select in pet_division:
            if select == pet:
                select.click()
    category_name = init_driver.find_element(By.XPATH, "//div[@id='Catalog']/h2").text
    for key in constant.set_of_species:
        if key == category_name:
            for fish in random.sample(constant.set_of_species[key], 1):
                init_driver.find_element(By.XPATH, "//div[@id='SearchContent']/form/input[1]").send_keys(fish)
    # elif category_name == "Dogs":
    #     for dogs in random.sample(constant.Dogs, 1):
    #         init_driver.find_element(By.XPATH, "//div[@id='SearchContent']/form/input[1]").send_keys(dogs)
    #
    # elif category_name == "Reptiles":
    #     for reptiles in random.sample(constant.Reptiles, 1):
    #         init_driver.find_element(By.XPATH, "//div[@id='SearchContent']/form/input[1]").send_keys(reptiles)
    #
    # elif category_name == "Cats":
    #     for cats in random.sample(constant.Cats, 1):
    #         init_driver.find_element(By.XPATH, "//div[@id='SearchContent']/form/input[1]").send_keys(cats)
    #
    # elif category_name == "Birds":
    #     for birds in random.sample(constant.Birds, 1):
    #         init_driver.find_element(By.XPATH, "//div[@id='SearchContent']/form/input[1]").send_keys(birds)

    init_driver.find_element(By.XPATH, "//div[@id='SearchContent']/form/input[2]").click()
    species = init_driver.find_elements(By.XPATH, "//div[@id='Catalog']//following-sibling::tbody/tr/td/a/img")
    for specie in species:
        constant.Lst_img_url.append(specie.get_attribute("src"))
        assert constant.list_img_url.__contains__(specie.get_attribute('src'))
