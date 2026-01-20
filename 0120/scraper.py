# import the required library
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate a Chrome options object
options = webdriver.ChromeOptions()

# set the options to use Chrome in headless mode
options.add_argument("--headless=new")

# initialize an instance of the chrome driver (browser)
driver = webdriver.Chrome(options=options)

# visit your target site
driver.get("https://news.daum.net/employ")

# ul = driver.find_element(By.CSS_SELECTOR, "ul.list_newsbasic")
# extract all the product containers
products = driver.find_elements(By.CSS_SELECTOR, ".item_newsbasic")

product_data = []

for p in products:
    title = p.find_element(By.CSS_SELECTOR, ".tit_txt").text
    desc = p.find_element(By.CSS_SELECTOR, ".desc_txt").text

    product_data.append({
        "Title": title,
        "Desc": desc,
    })

# print the extracted data
print(product_data)

# release the resources allocated by Selenium and shut down the browser
driver.quit()

file_name = "daum_news.csv"

with open(file_name, mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["Title", "Desc"]
    )
    writer.writeheader()
    writer.writerows(product_data)

print(f"{file_name} 저장 완료")
