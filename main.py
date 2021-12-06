# Imports libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import pandas as pd

# Sets up constants
BASE_URL = "https://www.levels.fyi/internships/"
DOUBLE_QUOTES = "\""

# Creates driver and gets the webpage
def getPage():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', options=chrome_options)
    driver.get(BASE_URL)

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "internships-table")))

        html = driver.page_source
        page = bs(html, "html.parser")
    finally:
        driver.quit()

        return page

# Finds the table of information and extracts all the relevant data to a list
def extractToList(page):
    table = page.find("table", {"class": "internships-table"})

    tr = table.tbody.find_all("tr")
    rows = []
    for row in tr:
        if row.has_attr("data-index"):
            row_data = row.find_all("td")
            is_open = row_data[3].find("a").text.strip() == "Apply"
            if is_open:
                rows.append(row)

    data = []
    for row in rows:
        row_data = row.find_all("td")

        company = row_data[0].find("h6").text.strip()

        hourly_salary = ""
        has_hourly_salary_info = row_data[1].find("h6") is not None
        if has_hourly_salary_info:
            hourly_salary = row_data[1].find("h6").text.strip()

        housing = ""
        has_housing_info = row_data[2].find("p") is not None
        if has_housing_info:
            housing = row_data[2].find("p").text.strip()

        apply_link = row_data[3].find("a")["href"]

        item = [company, hourly_salary, housing, apply_link]
        data.append(item)

    return data

# Finds the table of information and extracts all the relevant data to a dictionary
def extractToDict(page):
    table = page.find("table", {"class": "internships-table"})

    tr = table.tbody.find_all("tr")
    rows = []
    for row in tr:
        if row.has_attr("data-index"):
            row_data = row.find_all("td")
            is_open = row_data[3].find("a").text.strip() == "Apply"
            if is_open:
                rows.append(row)

    dict = []
    for row in rows:
        row_data = row.find_all("td")

        company = row_data[0].find("h6").text.strip()

        hourly_salary = ""
        has_hourly_salary_info = row_data[1].find("h6") is not None
        if has_hourly_salary_info:
            hourly_salary = row_data[1].find("h6").text.strip()

        housing = ""
        has_housing_info = row_data[2].find("p") is not None
        if has_housing_info:
            housing = row_data[2].find("p").text.strip()

        apply_link = row_data[3].find("a")["href"]

        item = {"Company": company, "Hourly Salary": hourly_salary,
                "Housing": housing, "Apply Link": apply_link}
        dict.append(item)

    return dict

# Creates a pandas dataframe out of the data
def createTable(data):
    dataframe = pd.DataFrame(data)
    dataframe.columns = ["Company", "Hourly Salary", "Housing", "Apply Link"]
    dataframe.sources = [BASE_URL]
    dataframe.attribution = ["Zaheer Mohiuddin", "Zuhayeer Musa"]

    return dataframe

# Prints the dictionary of data to a CSV
def printToCSV(dict):
    with open("internships.csv", "w") as out:
        is_header = True
        for entry in dict:
            if is_header:
                is_header = False
                for key in dict[0].keys():
                    out.write(f"{DOUBLE_QUOTES}{key}{DOUBLE_QUOTES}")
                    if key != "Apply Link":
                        out.write(", ")
                out.write("\n")

            for key in dict[0].keys():
                out.write(f"{DOUBLE_QUOTES}{entry[key]}{DOUBLE_QUOTES}")
                if key != "Apply Link":
                    out.write(", ")
            out.write("\n")

# Starting point for the program
def main():
    page = getPage()
    dict = extractToDict(page)
    printToCSV(dict)

    data = extractToList(page)
    createTable(data)


print()
main()
print()
