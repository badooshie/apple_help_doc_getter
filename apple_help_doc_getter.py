#! /usr/bin/python3

"""
    Checks to see if a support doc on support.apple.com exists,
    and if so, gets title, description, and last modified date.
    Exports information to a csv file

    A few items of housekeeping:
     - this script will randomize its requests so to now bombard the servers.

Here are the steps inline of what this script will do:
#S1 request the webpage
    > based on 200 response, returns html as text or if non 200, returns non 200 string
#S2 turn webpage into soup for easier handling
#S3 get title, description, and last modified date
#S4 add item to pandas DF
#S5 export DF into CSV

Redesign to include classes
#C Class that creates a webpage instance.  This class contains methods to get website info.


example address: https://support.apple.com/en-us/HT201295

"""
import requests
import pandas as pd
import html_file  # for testing
from bs4 import BeautifulSoup as bs
from time import sleep
from random import randint


class Webpage:

    def __init__(self, num):
        self.num = num
        self.url_main = 'https://support.apple.com/en-us/HT'
        self.url_num_base = 200000
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-us',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'}
        self.url_complete = str(self.url_main + str(self.url_num_base + self.num))

    def get_html(self):
        try:
            r = requests.get(self.url_complete, headers=self.headers)
            if r.status_code == 200:
                html = r.text
                r.close
                return html
            else:
                html = 'Non 200 Status Code'
                r.close
                return html
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def create_soup(self):
        html = self.get_html()
        soup = bs(html, features="html.parser")
        return soup

    def get_info(self):
        """Gets url, title, description, and other information"""
        soup = self.create_soup()

        info_url = soup.head.find(attrs={"rel": "canonical"})['href']
        info_title = soup.title.text
        info_description = soup.find(attrs={"name": "description"})['content'].replace('\n','')
        info_last_modified_date = soup.find(attrs={"class": "mod-date"}).time['datetime']

        doc_info = {info_url: [info_title, info_description, info_last_modified_date]}

        return doc_info


    def print_basic_info(doc_info):
        """Prints url, title, description, and last updated date"""
        print(doc_info.key, doc_info.values[:2])
        # needs ''.join(doc_info.keys()) to get key isolated as string
        pass

    def print_full_info(doc_info):
        """Prints url, title, description, and other fun things"""
        # TODO
        pass


def get_docs(amount_to_get):
    pass


def main():
    """Checks if there is a pre-existing csv file with any apple helps docs, if so, checks docs, then gets and adds more help docs. If not, creates one and adds some apple help docs."""
    amount_to_get = int(input("Please enter a number: "))
    get_docs(amount_to_get)

if __name__ == "__main__":
    main()



"""
# maybe this should be a global function? and not a class
class link_list:
    url_list = []
    
soup_test = bs(html_file.html_doc, 'html.parser')

for i in range(10):
    url_num_append = url_num_append + 1
    url_list.append(str(url_main) + str(url_num_append))

for i in url_list:
    print(i)
    sleep_for = randint(1,6)
    sleep(sleep_for)
"""
