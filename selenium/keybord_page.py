# @Author ZhangGJ
# @Date 2021/04/09 17:17
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
time.sleep(1)
driver.find_element_by_id('kw').send_keys('教程')
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.COMMAND, 'a')
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.COMMAND, 'x')
time.sleep(1)
driver.find_element_by_id('kw').send_keys(Keys.COMMAND, 'v')
time.sleep(1)
driver.find_element_by_id('su').send_keys(Keys.ENTER)
driver.quit()
