# @Author ZhangGJ
# @Date 2021/04/09 16:31

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://ww.baidu.com')
size = driver.find_element_by_id('kw').size
print(size)

text = driver.find_element_by_id('bottom_layer').text
print(text)

attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

result = driver.find_element_by_id('kw').is_displayed()
print(result)

driver.quit()
