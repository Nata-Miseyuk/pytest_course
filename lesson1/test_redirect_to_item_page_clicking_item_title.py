from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_redirection_to_item_page_clicking_item_title():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(2)

    text_before = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]').text

    inventory_item_name = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]')
    inventory_item_name.click()
    time.sleep(2)

    text_after = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]').text

    assert text_before == text_after
