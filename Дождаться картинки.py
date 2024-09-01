from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждем, пока загрузятся все изображения и их количество будет как минимум 4
images = WebDriverWait(driver, 40).until(
    lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4 and 
              all(img.get_attribute("src") for img in d.find_elements(By.TAG_NAME, "img"))
)
#Порядок загрузки изображений идет не по порядку, поэтому наше изображение под цифрой 3, а не 2
third_image = driver.find_elements(By.TAG_NAME, "img")[3]

src_value = third_image.get_attribute("src")

print("src=:", src_value)

driver.quit()