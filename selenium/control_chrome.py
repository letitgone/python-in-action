# @Author ZhangGJ
# @Date 2021/04/09 16:02
from selenium import webdriver

driver = webdriver.Chrome()
first_url = 'http://www.baidu.com'
driver.get(first_url)
second_url = 'http://114.115.234.147:8081/'
driver.get(second_url)
driver.back()
driver.forward()
driver.refresh()
driver.quit()