from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
driver.get("http://jqueryui.com/droppable/")
driver.implicitly_wait(30)

var = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to.frame(var)
src = driver.find_element_by_xpath("//*[@id='draggable']")
dest = driver.find_element_by_xpath("//*[@id='droppable']")
a1 = ActionChains(driver)
a1.drag_and_drop(src,dest).perform()