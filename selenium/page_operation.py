# @Author ZhangGJ
# @Date 2021/04/09 16:09

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://ww.baidu.com')
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

time.sleep(3)
driver.quit()
