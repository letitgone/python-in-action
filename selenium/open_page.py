# @Author ZhangGJ
# @Date 2021/04/09 15:22
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("Selenium")
# driver.find_element_by_id("su").click()
# driver.quit()

driver.set_window_size(480, 800)
driver.quit()

