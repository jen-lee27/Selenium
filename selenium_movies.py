from selenium import webdriver
import time

browser = webdriver.Chrome("C:/chromedriver.exe")
browser.maximize_window()

url = "https://play.google.com/store/movies"
browser.get(url)

interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # browser.execute_script("window.scrollTo(0, 1080)")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if prev_height == curr_height:
        break

    prev_height = curr_height

print("finished!")

movies = browser.find_elements_by_css_selector(".hP61id")
for movie in movies:
    if movie.find_element_by_css_selector(".SUZt4c.P8AFK"):
        title = movie.find_element_by_css_selector("div > .Epkrse").text
        print(title)
