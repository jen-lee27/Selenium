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

#infinite scroll -> use loop
before_h = driver.execute_script("return window.scrollY")
while True:
    #scroll all the way to the bottom
    driver.find_element_by_css_selector("body").send_keys(Keys.END)
    time.sleep(1) #so all contents are fully loaded

    #height after scroll
    after_h = driver.execute_script("return window.scrollY")
    if before_h == after_h:
        break

    before_h = after_h

#product info div
items = driver.find_elements_by_css_selector(".basicList_info_area__17Xyo")
for item in items:
    # name = item.find_element_by_css_selector(".basicList_title__3P9Q7 .basicList_link__1MaTN")
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").text
    try:
        price = item.find_element_by_css_selector(".price_num__2WUXn").text
    except:
        price = "n/a"
    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute("href")
    print(name, price, link)