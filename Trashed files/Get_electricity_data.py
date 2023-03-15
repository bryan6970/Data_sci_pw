# import the necessary libraries
import sys
import time
import tkinter as tk
import tkinter.messagebox as messagebox
from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select


def _scroll_to_end(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page
        time.sleep(1)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def _scroll_to_element(driver, element):
    # Scroll to the element using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", element)

    # Hover over the element to make sure it's in view
    action = ActionChains(driver)
    action.move_to_element(element).perform()


# create a webdriver object and set the path to the Chrome web_driver
service = Service('../venv/chromedriver.exe')
web_driver = webdriver.Chrome(service=service)

web_driver.get("https://www.emcsg.com/marketdata/priceinformation#priceDataView")

input("set your shiz")

# # Wait for page to load
# wait = WebDriverWait(web_driver, 10)
# wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/h2")))
#
# _scroll_to_end(web_driver)
x = '0'
while x == "0":
    try:
        input("END calander")
        END_CALENDAR_ELEMENT = web_driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/form/div[2]/div[7]/div[5]/div[2]/div[3]/div[2]/a')

        input("END month")
        END_MONTH_ELEMENT = web_driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/form/div[2]/div[4]/div[6]/div[2]/div[3]/div[2]/div/div/div/div/select[1]")


        input('END year')
        END_YEAR_ELEMENT = web_driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/form/div[2]/div[7]/div[5]/div[2]/div[3]/div[2]/div/div/div/div/select[2]")

        input('Continue')
        END_SELECT_MONTH_ELEMENT = Select(END_MONTH_ELEMENT)
        END_SELECT_YEAR_ELEMENT = Select(END_YEAR_ELEMENT)

        input('END calander')
        END_FULL_CALENDAR_ELEMENT = web_driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/form/div[2]/div[7]/div[5]/div[2]/div[3]/div[2]/div/div/table/tbody")

        input('download btn')
        DOWNLOAD_BTN = web_driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/form/div[3]/input")

        ##########

        input('Start with START')

        START_CALENDAR_ELEMENT = web_driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/form/div[2]/div[4]/div[6]/div[2]/div[2]/div[2]/a")
        input('month')
        START_MONTH_ELEMENT = web_driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/form/div[2]/div[4]/div[6]/div[2]/div[2]/div[2]/div/div/div/div/select[1]")
        input('year')
        START_YEAR_ELEMENT = web_driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/form/div[2]/div[4]/div[6]/div[2]/div[2]/div[2]/div/div/div/div/select[2]")

        START_SELECT_MONTH_ELEMENT = Select(START_MONTH_ELEMENT)
        START_SELECT_YEAR_ELEMENT = Select(START_YEAR_ELEMENT)
        input('full calander')
        START_FULL_CALENDAR_ELEMENT = web_driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/form/div[2]/div[4]/div[6]/div[2]/div[2]/div[2]/div/div/table/tbody")
    except:
        x = input()




input('before start')

for year in range(2017,2020):
    START_CALENDAR_ELEMENT.click()
    START_SELECT_YEAR_ELEMENT.select_by_value(year)
    START_CALENDAR_ELEMENT.click()

    END_CALENDAR_ELEMENT.click()
    END_SELECT_YEAR_ELEMENT.select_by_value(year + 1)
    END_CALENDAR_ELEMENT.click()

    for month in range(12):
        START_CALENDAR_ELEMENT.click()

        START_SELECT_MONTH_ELEMENT.select_by_value(month)

        # find the first element of the first tr
        FIRST_DAY = START_FULL_CALENDAR_ELEMENT.find_element(By.XPATH, './tr[1]/*[1]')

        FIRST_DAY.click()

        END_CALENDAR_ELEMENT.click()

        END_SELECT_MONTH_ELEMENT.select_by_value(month)

        # find the last element of the last tr
        LAST_DAY = END_FULL_CALENDAR_ELEMENT.find_element(By.XPATH, './tr[last()]/*[last()]')

        LAST_DAY.click()

        DOWNLOAD_BTN.click()

        time.sleep(1)








