from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 크롬 드라이브실행.
driver = webdriver.Chrome()

#URL 주소 추가해서 실행.
driver.get("https://www.google.co.kr")

# 창이 오픈되고 3초를 대기한다.
time.sleep(3)

# 검색어 찾기.
searchBox = driver.find_element(By.CLASS_NAME, 'gLFyf')
#XPath를 사용하는 경우.
#'//*[@id="gNO89b"]'
#searchBox = driver.find_element(By.XPATH, "//*[@id='ApjFqb']")

searchBox.send_keys("맥북")
searchBox.send_keys(Keys.RETURN)
time.sleep(5)