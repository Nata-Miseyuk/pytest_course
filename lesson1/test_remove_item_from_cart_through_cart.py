from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()


def test_remove_item_from_cart_through_cart():
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 5)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # adding item to the cart
    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    # going to the cart:
    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()

    # emptying the cart:
    cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    cart_badge.is_displayed()
    cart_item = driver.find_element(By.CLASS_NAME, 'cart_item')

    sauce_labs_backpack = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
    remove_button = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    time.sleep(2)
    remove_button.click()
    time.sleep(5)

    cart_badge = wait.until(EC.invisibility_of_element_located(cart_badge))

    assert cart_badge is True
    assert cart_item.is_displayed() is False

    driver.quit()
