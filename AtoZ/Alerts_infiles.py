import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s= Service("C:\\work2\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("parag")
driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
time.sleep(1)
alerts= driver.switch_to.alert.accept()
