#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

#service = Service('./chromedriver')
#driver = webdriver.Chrome(service=service)

#driver.get('https://codeit.kr')



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# browser creation
driver = webdriver.Chrome('C:/chromedriver.exe')
# driver = webdriver.Firefox()
# open website
driver.get('https://www.naver.com')
driver.implicitly_wait(3);

# upon shopping menu click
driver.find_element_by_css_selector('a.nav.shop').click()

time.sleep(2)
# search bar click
search = driver.find_element_by_css_selector('input._searchInput_search_input_QXUFf')
search.click()

#search
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)