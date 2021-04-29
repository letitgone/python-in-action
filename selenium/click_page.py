# @Author ZhangGJ
# @Date 2021/04/09 17:08
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

above = driver.find_element_by_id('s-usersetting-top')
ActionChains(driver).move_to_element(above).perform()
