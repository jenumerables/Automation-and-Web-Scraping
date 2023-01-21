# import packages
from selenium import webdriver


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
  driver.get("http://automated.pythonanywhere.com")
  return driver