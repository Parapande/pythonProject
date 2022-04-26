import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Work2\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.javatpoint.com/python-armstrong-number")
driver.maximize_window()
print(driver.current_url)
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Programs").click()
web = driver.find_element(By.XPATH, "//h1[@class='h1']").text
assert "Python Programs | Python Programming Examples" in web
print("is pass")

