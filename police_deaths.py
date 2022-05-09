from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

chrome_driver_path = "chrome_driver/chromedriver.exe"
# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome(executable_path=chrome_driver_path, options=option)
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# --------- Start page -----------
START_PAGE = "https://en.wikipedia.org/wiki/Lists_of_killings_by_law_enforcement_officers_in_the_United_States"
driver.get(START_PAGE)


for i in range(1,13):
    time.sleep(1)
    element = driver.find_element(By.XPATH, f'//*[@id="mw-content-text"]/div[1]/table/tbody/tr[4]/td[{i}]/a')
    element.click()
    driver.current_url

    # --------- Finding header titles ---------
    header_titles = driver.find_elements(By.CLASS_NAME, 'headerSort')
    header_names = driver.find_elements(By.CSS_SELECTOR,'.wikitable tr')


    # --------- Write to csv ----------
    csv_file = open(f'table{i}.csv', 'a', encoding="utf-8", newline='')
    CsvWriter = csv.writer(csv_file)

    list=[]
    for title in header_titles:
        list = list
        title = title.text
        list.append(title)
    CsvWriter.writerow(list)

    for item in header_names:
        list1=[]
        items_in_row = item.find_elements(By.CSS_SELECTOR,'td')
        for item in items_in_row:
            item = item.text.replace('\n', '')
            list1.append(item)
        if len(list1) != 0:
            CsvWriter.writerow(list1)


    time.sleep(1)
    driver.get(START_PAGE)
    time.sleep(1)


driver.quit()


