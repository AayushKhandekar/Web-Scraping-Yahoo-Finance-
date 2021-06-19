import requests 
import csv
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from selenium import webdriver 
from bs4 import BeautifulSoup 

data_list = []
data_list_new = []
count = 0


# WEB SCRAPING
response = requests.get('https://finance.yahoo.com/most-active').content 
soup = BeautifulSoup(response, 'html.parser') 
header = soup.tr.find_all('span') #contains all column headings
all_rows = soup.find_all('tr')
for row in soup.find_all("tr"):
    data = ([td.text for td in row.find_all("td")[1:-1]])
    data_list.append(data)
 

# DATA CLEANING  
data_list.pop(0) # removes firt element from the list which is []
#print(data_list) #prints the whole table in the form on list

for x in data_list:
    del x[2:6] # deletes the columns 2,3,4,5
    del x[-1] # deletes the last column
    data_list_new.append(x)
# print(data_list_new)


# FINDING THE STOCK PRICE
def Stock_Price(stock_name):
    response = requests.get(stock_url).content 
    soup = BeautifulSoup(response, 'html.parser')
    count = 0
    array = soup.find(id = 'quote-header-info') #stores all id = ''
    array1 = array.find_all('span') # stores all spans with id = ''
    for span in array1:
        count = count + 1
        if count == 4:
            price = str(span) # type casting from bs4 to string
            price = price[74:] 
            price = price[::-1]
            price = price[7:]
            print("Stock Name : " + stock_name + " and Stock Price Rs : "+ price[::-1])

stock_name = raw_input("Enter Stock Name ")
stock_url = 'https://finance.yahoo.com/quote/' + stock_name + '.NS?p=' + stock_name + '.NS&.tsrc=fin-srch'
Stock_Price(stock_name)
