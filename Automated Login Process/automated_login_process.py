# import packages
from selenium import webdriver
# Return Key
from selenium.webdriver.common.keys import Keys
import time

def get_drvier():
  # Set options to make browser scraping easier
  options = webdriver.ChromeOptions()
  # disables information bars so it doesn't interfere with cursor
  options.add_argument("disable-infobars")
  # resize browser size to max size
  options.add_argument("start-maximized")
  # avoid issues using a linux machine
  options.add_argument("disable-dev-shm-usage")
  # disable sandbox
  options.add_argument("no-sandbox")
  # helps selenium scrape browsers, avoids  blocking
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  # prevents selenium detection
  options.add_argument("disable-blink-features=AutomationControlled")

  # create chrome driver variable
  driver = webdriver.Chrome(options=options)
  # get webpage to scrape
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver


def main():
  driver = get_drvier()
  # username
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(1)
  # pw and hit return
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  # Home button
  driver.find_element(by="xpath", value="/html/body/nav/div/a")
  print(driver.current_url)

  
# print out main element
print(main())
