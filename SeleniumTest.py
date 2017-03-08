from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# go to the google home page
driver.get("http://10.234.4.25/serverconfig/")

try:
	InputElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
except:
	driver.quit()


inputElement = driver.find_element_by_name("Username")

inputElement.send_keys("admin")

inputElement = driver.find_element_by_name("Password")

inputElement.send_keys("admin")

inputElement.submit()

element = WebDriverWait(driver, 5)

driver.quit()