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
from datetime import date


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
                html = self.url_complete
                r.close
                return html
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def create_soup(self):
        html = self.get_html()
        if html == self.url_complete:
            soup = self.url_complete
        else:
            soup = bs(html, features="html.parser")
        return soup

    def get_info(self):
        """Gets url, title, description, and other information"""
        soup = self.create_soup()
        try:
            info_url = soup.head.find(attrs={"rel": "canonical"})['href']
            info_title = soup.title.text
            info_description = soup.find(attrs={"name": "description"})['content'].replace('\n','')
            info_last_modified_date = soup.find(attrs={"class": "mod-date"}).time['datetime']

            doc_info = [info_url, info_title, info_description, info_last_modified_date]

        except AttributeError as e:
            doc_info = [soup, 'Non 200 Status Code']

        return doc_info


def get_docs(start, end):
    """
    Takes a range of numbers and finds any support docs in given range. 
    Input: numbers
    Output One list of many lists
    """
    pass
    
    empty_list = []
    for count in range(start, end+1):
        webpage = Webpage(count)
        empty_list.append(webpage.get_info())

    full_list = empty_list
    return full_list

def export_csv(full_list):
    """
    Takes in a list, formats into dataframe, then exports csv file.
    Input: list, 
    Output: CSV file
    """
    year = str(date.today().year)
    month = str(date.today().month)
    day = str(date.today().day)
    TODAYS_DATE = '{}{}{}'.format(year,month,day)

    docs_df = pd.DataFrame(full_list)
    docs_df.columns = ["Url","Title","Description","Last Modified"]
    docs_df.to_csv('{}_Apple_Support_docs.csv'.format(TODAYS_DATE), index=False)
    print("CSV File Created")

def main():
    """Checks if there is a pre-existing csv file with any apple helps docs, if so, checks docs, then gets and adds more help docs. If not, creates one and adds some apple help docs."""
    # amount_to_get = int(input("Please enter a number:")
    # Input Starting num, ending num 
    # Get List of URLS
    # Add List to CVS File
    # check for csv doc, if non-existent create one
    # get_docs(amount_to_get)
    pass

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

hello again again
    
"""
