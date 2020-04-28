from bs4 import BeautifulSoup
from selenium import webdriver
import os
import re
import urllib.parse

# handle input

# open chrome driver
def main(arg, driver):

    def encodeSearch(search):
        return urllib.parse.quote(search)


    search = arg

    # pull info
    url = "https://www.google.com/search?hl=en&q=" + (encodeSearch(search))
    print(url)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #driver.quit()
    status_array = []
    # extracts list elements that have the wanted information aka asD70e refers to COVID status
    delivery_array = []

    for ele in soup.findAll("li", {"class": "asD7Oe"}):
        status_array.append(ele.get('aria-label'))

    if (re.findall("temporarily closed", str(soup), re.IGNORECASE) != []):
        status_array = ["Temporarily Closed"]
        print("match found for temp closed")
        print(status_array, delivery_array)
        return (status_array, [])

    # extract list elements that refer to delivery statuses
    for ele in soup.findAll("span", {"class": "jSC49b"}):
        ele = ele
        try:
            while (ele.find_next_sibling("a").contents):
                delivery_array.append((ele.find_next_sibling("a").contents)[0])
                ele = ele.find_next_sibling("a")
        except:
            continue


    if len(status_array) != 0:
        print(status_array, delivery_array)
        return (status_array, delivery_array)

    status_array.append("No dine-in")

    print(status_array, delivery_array)
    return (status_array, delivery_array)
