

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s= Service("C:\\work2\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://login.salesforce.com/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()

driver.find_element(By.ID, "username").send_keys("Parag")
driver.find_element(By.ID, "password").send_keys("hashincluse")
driver.find_element(By.ID, "Login").click()

# Assertion on error message
message = driver.find_element(By.ID, "error").text
# for substring
assert "can't" in message
print("Assertion pass")

# for complete phrase
assert "Please check your username and password. If you still can't log in," \
       " contact your Salesforce administrator." == message
print("Assertion for complete phrase pass")