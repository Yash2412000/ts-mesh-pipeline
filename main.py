# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:09:01 2023

@author: Yashraj Rai
"""

import csv
from scraper import WebScraper  # Import your WebScraper class from scraper.py

def main():
    # Create an instance of the WebScraper class
    scraper = WebScraper("https://www.nnvl.noaa.gov/view/globaldata.html")

    # Scrape data from the website
    scraped_data = scraper.scrape_data()

    if scraped_data:
        # Save the scraped data to a CSV file
        scraper.save_to_csv(scraped_data, "output3.csv")

if __name__ == "__main__":
    main()
