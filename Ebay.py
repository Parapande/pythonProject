from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Work2\\chromedriver.exe")
driver= webdriver.Chrome(service = s)
driver.get("https://www.ebay.com/")
driver.maximize_window()
print(driver.current_url)
driver.find_element(By.XPATH,"(//i[@class='gh-sprRetina gh-eb-arw gh-rvi-chevron'])[2]").click()
ebay=driver.find_elements(By.XPATH,"//a[@class='gh-eb-oa thrd']")
print(len(ebay))
for ele in ebay:
    print(ele.text)
    if ele.text=='Selling':

        break