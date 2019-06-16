import time

from selenium import  webdriver
driver=webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")

driver.get("https://phptravels.com/")
time.sleep(10)

p_wid=driver.current_window_handle
driver.find_element_by_xpath("//span[text()='Login']").click()
var = driver.window_handles
for i in var:
    #print(i)
    if(p_wid!=i):
        driver.switch_to.window(i)#switch to child window
driver.find_element_by_id("inputEmail").send_keys("qspiders")
#driver.close()#closes current window
driver.quit()#closes currently browser session

#[w_id_1,w_id_2]>>List
#window_handles>>is a method>>returns window id's