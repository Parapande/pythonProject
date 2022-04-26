import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\work2\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.amazon.in")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.implicitly_wait(5)

# Searching for books
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("books")

# click on search
driver.find_element(By.ID, "nav-search-submit-button").click()

# selecting our desired book
books = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")
print(len(books))
time.sleep(2)
for book in books:
    # print(book.text)
    if book.text == "You Can":
        book.click()
        break

# you can book is now opened in new tab so -- window handle concept
childwindow = driver.window_handles[1]
parentwindow = driver.window_handles[0]
driver.switch_to.window(childwindow)

# Add to cart
driver.find_element(By.ID, "add-to-cart-button").click()
driver.close()
driver.switch_to.window(parentwindow)
time.sleep(2)

# selecting 2nd book from parent window
for book in books:
    if book.text == "World’s Greatest Classics (Box Set of 4 Books)":
        book.click()
        break

# switching to child window
child = driver.window_handles[1]
driver.switch_to.window(child)
driver.find_element(By.ID, "add-to-cart-button").click()

# click on cart to check items
driver.find_element(By.LINK_TEXT, "Cart").click()
time.sleep(2)

# Assertion to check we selected proper books or not
cartbooks = driver.find_elements(By.CLASS_NAME, "a-truncate-cut")

for cartbook in cartbooks:
    assert cartbook.text == "World’s Greatest Classics (Box Set of 4 Books)"
    break

# assertion on 2nd book
bookName = driver.find_element(By.XPATH, "(//span[@class='a-truncate-cut'])[2]").text
assert "You Can" in bookName

# click on proceed to buy
time.sleep(2)
driver.find_element(By.XPATH, "//span[@id='sc-buy-box-ptc-button']").click()
