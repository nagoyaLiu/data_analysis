from selenium import webdriver
from time import sleep 


sleep(3)
#print('here')
browser = webdriver.Chrome('chromedriver.exe')
#sleep(3)
#browser.quit()
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()

