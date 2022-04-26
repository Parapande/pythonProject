import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Work2\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://parag.pande@yash.com:Password@2020@you.yash.com/Pages/default.aspx")
driver.maximize_window()
print(driver.current_url)
# switch to infogram vai you portal with the use of windowhandles
driver.find_element(By.XPATH, "//a[@title='YASH Infogram']").click()
parent = driver.window_handles[0]
child = driver.window_handles[1]
driver.switch_to.window(child)
time.sleep(5)
#Enters the requried Passkeys
driver.find_element(By.XPATH, "//input[@name='UserName']").send_keys("parag.pande@yash.com")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='passwordInput']").send_keys("Password@2020")
time.sleep(3)
driver.find_element(By.XPATH, "//span[@id='submitButton']").click()
# home page then dropdown
time.sleep(2)
driver.find_element(By.XPATH, "//span[@id='customHeaderModulePickerBtn-inner']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@id='__item7-__list4-9']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[@id='__button5-inner']").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//div[@class='sapMSLITitleOnly'])[3]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//textarea[@rows='7']").send_keys("paragpande")
time.sleep(2)
driver.find_element(By.XPATH, "//bdi[@id='__button90-BDI-content']").click()
