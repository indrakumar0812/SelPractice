from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.implicitly_wait(10)
#driver.find_element_by_id("datepicker").click()
#frame_val=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
#driver.switch_to.frame(frame_val)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))
#driver.find_element_by_xpath("//input[@class='hasDatepicker']").click()
driver.find_element_by_xpath("//input[@class='hasDatepicker']").send_keys("05/05/2012")
driver.find_element_by_xpath("//input[@class='hasDatepicker']").send_keys(Keys.ENTER)
# month=driver.find_element_by_xpath("//select[@data-handler='selectMonth']")
# #Return type is WebElement>>click,send_keys
# s1=Select(month)#where to select
# s1.select_by_visible_text("May")#what to select
# year =driver.find_element_by_xpath("//select[@data-handler='selectYear']")
# s2=Select(year)
# s2.select_by_visible_text("2016")
#
# #18/05/2015
#
# driver.find_element_by_xpath("//a[text()='18']").click()