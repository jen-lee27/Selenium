from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# browser creation
browser = webdriver.Chrome('C:/chromedriver.exe')
browser.maximize_window()

url = "https://flight.naver.com/flights"
browser.get(url)

browser.find_element_by_css_selector(".tabContent_option__2y4c6.select_Date__1aF7Y").click()
# browser.find_element_by_link_text("가는 날").click()

# 어느새 길어진 그림자를 따라서 땅거미 진 어둠속을 그대와 걷고 있네요 손을 마주 잡고 그 언제까지라도 함께 있는것만으로 눈물이 나는 걸요

# 이번달 27일, 28일 선택
browser.find_elements_by_css_selector(".sc-evZas.dDVwEk.num")[26].click()
browser.find_elements_by_css_selector(".sc-evZas.dDVwEk.num")[27].click()

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[2]").click()
browser.find_element_by_class_name("searchBox_search__2KFn3").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div[2]/div/div[2]")))

    # elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div[2]/div/div[2]/div[1]/b/i")
    print(elem.text)
finally:
    browser.quit()