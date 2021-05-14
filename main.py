from selenium import webdriver
from decouple import config

# some important variables
PATH = config("CHROME_PATH")
driver = webdriver.Chrome(executable_path=PATH)
web_page = config("URL")
if __name__ == "__main__":
    driver.get(web_page)  # loads a page for testing
    print(driver.title)  # access the title of the web page
