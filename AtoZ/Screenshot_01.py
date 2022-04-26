from tkinter import Image

import ss as ss
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s= Service("C:\\work2\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://www.browserstack.com/"

driver.get(url)
image = ss.full_Screenshot(driver, save_path=r'.' , image_name='name.png')

screen = Image.open(image)
screen.show()

