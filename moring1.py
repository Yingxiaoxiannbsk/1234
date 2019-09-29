from selenium import webdriver
import time

driver=webdriver.Chrome()
url='file:///C:/Users/lenovo/Desktop/page/%E6%B3%A8%E5%86%8CA.html'
driver.get(url)

driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_name('passwordA').send_keys('123456')
driver.find_element_by_class_name('telA').send_keys('12345678901')
driver.find_element_by_class_name('emailA').send_keys('123@')
driver.find_element_by_tag_name('button').click()

time.sleep(3)
driver.quit()


