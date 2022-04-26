from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Work2\\chromedriver.exe")
driver= webdriver.Chrome(service = s)

driver.get("https://www.Amazon.in")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'Electronics')]").click()