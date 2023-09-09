# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:17:06 2023

@author: Yashraj Rai
"""

import requests
from bs4 import BeautifulSoup
import csv

class WebScraper:
    def __init__(self, url):
        self.url = "https://www.nnvl.noaa.gov/view/globaldata.html"

    def scrape_data(self):
        try:
            # Send an HTTP GET request to the website
            response = requests.get(self.url)

            # Check if the request was successful
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract data from the website using BeautifulSoup
                # Replace this part with your specific data extraction logic
                data_list = []

                # For example, let's extract all the links on the page
                links = soup.find_all('a')
                for link in links:
                    data_list.append(link.get('href'))

                return data_list

            else:
                print(f"Failed to retrieve data from {self.url}. Status code: {response.status_code}")
                return None

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def save_to_csv(self, data, filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Data'])  # Modify the header as needed

                for item in data:
                    csv_writer.writerow([item])

            print(f'Data saved to {filename} successfully.')

        except Exception as e:
            print(f"An error occurred while saving data to CSV: {str(e)}")
