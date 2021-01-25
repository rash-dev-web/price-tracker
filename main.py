import requests
from bs4 import BeautifulSoup
import smtplib
import os


MY_EMAIL = os.getenv("MY_EMAIL")
MY_PWD = os.getenv("MY_PWD")
URL = "https://www.flipkart.com/samsung-163-cm-65-inch-ultra-hd-4k-led-smart-tv/p/itm442ae5a2c7000?pid" \
      "=TVSFH37DHP9GZVPM&lid=LSTTVSFH37DHP9GZVPMW4DN3C&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1" \
      "=search&fm=SEARCH&iid=en_4aSx3Jd8wRkjN83TJ7xXkRhzB%2BXcS%2BsGjUhk6hXLF1tZ1" \
      "%2F4lLA25Yot2EueKvMTOvkCDydc75eTseSg53L7LMg%3D%3D&ppt=hp&ppn=homepage&ssid=zjubsq871ik0w1kw1611588197180&qH" \
      "=c9a1fdac6e082dd8 "
headers = {
    # "User-Agent": "Defined"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Accept-Language": "en-US,en;q=0.5",
    # "Origin": "https://www.amazon.in",
    # "Accept": "*/*",
    # "Accept-Encoding": "gzip, deflate, br",
    # "DNT": "1",
    # "Connection": "keep-alive",
}
# Connection
# 	keep-alive
response = requests.get(URL, headers=headers)

amazon_html = response.text
# print(amazon_html)
soup = BeautifulSoup(amazon_html, "lxml")
# print(response)
# #priceblock_ourprice
price = soup.find(name="div", class_="_30jeq3 _16Jk6d")
tv_price = price.getText()

tv_price = tv_price[1:]
tv_price = tv_price.split(",")

total_price = float(tv_price[0]) * 1000 + float(tv_price[1])
print(total_price)
product_title = soup.find(name="span", class_="B_NuCI")
product_title = product_title.getText().encode('utf-8')
print(product_title)
message = f"{product_title} is now {total_price}"
while total_price < 100000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PWD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Low Price Alert\n\n{message}")
        print("email sent!")
        break
