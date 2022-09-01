import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_button_presence(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert bool(button), 'Page does not contain "Add to basket" button'
    time.sleep(5)
