from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")


input_field = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
input_field.send_keys('SkyPro')

blue_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
blue_button.click()


button_text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(button_text)
