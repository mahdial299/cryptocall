

import csv
import random
import time
import pyfiglet
import colored
from datetime import datetime
from bs4 import BeautifulSoup
import requests

def get_crypto(coin):
    url = f"https://www.google.com/search?q={coin}+price&sxsrf=AOaemvJxkJI2mosb39pvFv2zVbHFlHp1Rw%3A1642759600754&ei=sIXqYae8LaGH9u8Pu6ONmAI&ved=0ahUKEwin1NCzzML1AhWhg_0HHbtRAyMQ4dUDCA4&uact=5&oq=bitcoin+price&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgAEEMyCggAEIAEEIcCEBQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIIxCwAxAnOgcIABBHELADOgcIABCwAxBDSgQIQRgASgQIRhgAUI0DWNIGYJUJaAFwAngAgAHHA4gBmQmSAQkwLjIuMC4xLjGYAQCgAQHIAQrAAQE&sclient=gws-wiz"
    HTML = requests.get(url)
    soup = BeautifulSoup(HTML.text, 'html.parser')
    text = soup.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    return text



field_names = ["Date", "price"]


with open("data.csv", 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
    csv_writer.writeheader()

while True:

    e = datetime.now()
    crypt = 'bitcoin'
    price = get_crypto(crypt)
    if ',' in price:
        price = price.replace(',', '')

    with open("data.csv", 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        x_value = f'{e.month}{e.day}{e.hour}{e.minute}'

        info = {
            "Date": x_value,
            "price": round(int(float(price[0:14])), 7)
        }

        csv_writer.writerow(info)
        print(x_value, round(int(float(price[0:14])), 7))
        # x_value += 1
        price = get_crypto(crypt)
        # print(f'price : {price[0:17]} IRR')
        # print(e.second, price[0:14])
    time.sleep(60)
        # return e.second, price[0:14]