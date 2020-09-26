#! /usr/bin/python3

"""
    Checks to see if a support doc on support.apple.com exists,
    and if so, gets title, description, and last modified date.
    Exports information to a csv file

    A few items of housekeeping:
     - this script will randomize its requests so to now bombard the servers.

Here are the steps inline of what this script will do:
#S1 request the webpage
    > returns html as text if webpage is active or not by http responses
#S2 turn webpage into soup for easier handling
#S3 get title, description, and last modified date
#S4 add item to pandas DF
#S5 export DF into CSV

example address: https://support.apple.com/en-us/HT201295

"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import html_file  # for testing

"""
attempting to learn and use classes, lol

class webpage:
    self.page = page
"""

url_main = "https://support.apple.com/en-us/HT"
url_num_append = 200000
url_complete = ''
url_list = []

soup_test = bs(html_file.html_doc, 'html.parser')

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-us',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'}


def is_active(URL):
    try:
        r = requests.get(URL, headers=headers)
        if r.status_code == 200:
            html = r.text
            r.close
            return html
        else:
            r.close
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def create_soup(HTML)
    soup = bs(HTML)






for i in range(10):
    url_num_append = url_num_append + 1
    url_list.append(str(url_main) + str(url_num_append))

print(url_list)
