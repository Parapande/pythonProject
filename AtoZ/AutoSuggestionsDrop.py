import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

j=Service("C:\\Work2\\chromedriver.exe")
driver= webdriver.Chrome(service = j)
driver.get("https://www.yash.com/")
print(driver.current_url)
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@class='icon-search-icon']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='ytSearch_box']").send_keys("car")
time.sleep(1)
items=driver.find_elements(By.XPATH,"//div[@class='ui-menu-item-wrapper']")
print(len(items))
for  item in items:
 print(item.text)
 if item.text == "Healthcare":
      item.click()
      break