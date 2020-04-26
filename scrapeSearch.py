from bs4 import BeautifulSoup
from selenium import webdriver
import os
import re


# handle input

# open chrome driver
def main(arg):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    def encodeSearch(search):
        return (search.replace(" ", "%20"))

    #driver = webdriver.Chrome(executable_path='/Users/dantelacu/Documents/scrape-covid/python-google-places/chromedriver')

    search = arg

    # pull info
    url = "https://www.google.com/search?hl=en&q=" + (encodeSearch(search))
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    status_array = []
    # extracts list elements that have the wanted information
    for ele in soup.findAll("li", {"class": "asD7Oe"}):
        status_array.append(ele.get('aria-label'))

    return status_array
