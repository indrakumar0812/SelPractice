from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")

driver.get("https://www.amazon.in/")
driver.implicitly_wait(30)
a1=ActionChains(driver)
category_ele = driver.find_element_by_xpath("//span[text()='Category']")
a1.move_to_element(category_ele).perform()

