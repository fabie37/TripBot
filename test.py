from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.skyscanner.net/")
assert "Skyscanner" in driver.title

# Accept the SkyScanner
cookieButton = driver.find_element(By.ID, "acceptCookieButton")
cookieButton.click()
sleep(5)
inputSelector = driver.find_element(By.NAME, "fsc-origin-search")
inputSelector.send_keys("123")

# inputSelector.clear()
# inputSelector.send_keys("Edinburgh (EDI)xxx")
# inputSelector.send_keys(Keys.TAB)
# inputSelector.send_keys("Split (SPU)")
# departData = driver.find_element(By.ID, "depart-fsc-datepicker-button")
# departData.click()
assert "No results found." not in driver.page_source
# driver.close()
