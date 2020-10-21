# program to automate google and stackoverflow search and show the result in the browser if it exists

from selenium import webdriver
import requests
from bs4 import BeautifulSoup

path = r"C:\\Program Files (x86)\\geckodriver.exe" # path of driver


def get_response(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")
    return soup.prettify


def search_stackoverflow(query):
    default_url = "https://stackoverflow.com/search?q=" + str(query)
    response = get_response(default_url)
    if "We couldn't find anything for" in str(response):
        print("Searched stackoverflow! No results found!")
        exit()
    else:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(executable_path=path, options=options)
        driver.get(default_url)


def search_google(query):
    default_url = "https://www.google.com/search?q=" + str(query)
    response = get_response(default_url)
    if "did not match any documents" in str(response):
        print("Searched google! No results found!")
    else:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(executable_path=path, options=options)
        driver.get(default_url)


def start():
    g_or_s = input("Enter the search type\n[1] Google\n[2] StackOverflow >> ")
    if g_or_s == "1":
        query = str(input("Enter the query: "))    
        search_google(query)
    elif g_or_s == "2":
        query = str(input("Enter the query: "))    
        search_stackoverflow(query)


if __name__ == "__main__":
    start()
