# @Author ZhangGJ
# @Date 2021/04/09 16:20

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
time.sleep(3)
search_text.submit()
time.sleep(3)
driver.quit()
