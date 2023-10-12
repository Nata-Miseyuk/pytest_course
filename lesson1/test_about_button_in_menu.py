from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


def test_about_button():
    driver.get("https://www.saucedemo.com/")
    # wait = WebDriverWait(driver, 10)
    # url_before = driver.current_url

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(3)

    about_button = driver.find_element(By.CSS_SELECTOR, 'a[id="about_sidebar_link"]')
    about_button.click()
    time.sleep(3)

    # url_after = driver.current_url
    # assert url_after != url_before

    # image_sauce_labs = driver.find_element(By.CSS_SELECTOR, 'img[src="/images/logo.svg"]')
    # image_sauce_labs = wait.until(EC.visibility_of_element_located(image_sauce_labs))
    # assert image_sauce_labs is True
    # assert image_sauce_labs.is_displayed()

    text = driver.find_element(By.XPATH, '//p[contains(text(), "The world relies on your code")]')
    assert text.is_displayed()

    driver.quit()
