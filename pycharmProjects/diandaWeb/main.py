import selenium
from selenium import webdriver
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://192.168.1.248:31100/users/login?path=/")
driver.find_element_by_id("userName").send_keys("176021732945")