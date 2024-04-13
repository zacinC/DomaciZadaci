import csv
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def sort_properties(csv_file):
    # Čitamo podatke iz CSV datoteke i sortiramo ih po cijeni pa po stambenoj površini
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        sorted_properties = sorted(reader, key=lambda x: (float(x['Cijena'].strip('€').replace(',', '')),
                                                          float(x['Stambena Površina'].split()[0])),
                                   reverse=True)
    return sorted_properties

# Funkcija za zapisivanje sortiranih podataka u CSV datoteku


def write_sorted_properties(sorted_properties, csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=sorted_properties[0].keys())
        writer.writeheader()
        writer.writerows(sorted_properties)


browser = webdriver.Chrome()
# Navigate to the webpage
browser.get("https://www.realitica.com/?cur_page=0&for=DuziNajam&pState=Crna+Gora&pZpa=Crna+Gora&opa=Bar&cty=Bar+Centar&qry=Bar&lng=hr")

# Loop to click the element four times
for _ in range(3):
    try:
        tmp_browser = webdriver.Chrome()

        realties = browser.find_elements(By.CLASS_NAME, "thumb_div")
        # print(len(realties))
        for realty in realties:
            try:
                tmp_browser.get(realty.find_element(
                    By.TAG_NAME, 'a').get_attribute("href"))

                listing_header = tmp_browser.find_element(
                    By.XPATH, "//*[@id='listing_body']").text.split('\n', 1)[1]
                about_author_element = tmp_browser.find_element(
                    By.XPATH, "//*[@id='aboutAuthor']").text.rsplit('\n', 1)[0]
                listing_footer = tmp_browser.find_element(By.XPATH,
                                                          "//*[@id='listing_body']/div[6]").text
                listing_lines = (
                    listing_header + about_author_element + listing_footer).split('\n')
                listing_dict = {}
                for line in listing_lines:
                    if ':' in line:
                        key, value = line.split(':', 1)
                        listing_dict[key.strip()] = value.strip()

                csv_file = 'DomaciZadaci\peti_domaci\zad2\listing_data.csv'

                # Write the dictionary to CSV file
                with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(
                        file, fieldnames=listing_dict.keys())

                    # Check if file is empty, if yes, write header
                    if file.tell() == 0:
                        writer.writeheader()

                    # Write the dictionary
                    writer.writerow(listing_dict)

                print("Data appended to listing_data.csv successfully.")

            except Exception as e:
                print(e)
                continue
        tmp_browser.quit()
        sleep(3)
        next_button = browser.find_element(
            By.XPATH, '//*[@id="left_column_holder"]/table/tbody/tr/td/table/tbody/tr/td[5]')
        next_button.click()
        sleep(3)
    except Exception as e:
        print(e)
        continue

# Close the browser
browser.quit()

# Zamijenite s imenom vaše CSV datoteke
csv_file = 'DomaciZadaci\peti_domaci\zad2\listing_data.csv'

sorted_properties = sort_properties(csv_file)
write_sorted_properties(sorted_properties, 'sortirane_nekretnine.csv')

print("Sortirane nekretnine su zapisane u sortirane_nekretnine.csv datoteku.")
