import requests
from bs4 import BeautifulSoup
import ptime
def price(url):
    st_response = requests.get(url)
    st_soup = BeautifulSoup(st_response.content, "html.parser")
    stock_div = st_soup.find("div", id="nsecp")
    if stock_div!=None:
       return stock_div.text.strip()
    else:
        return None

def INDlist():
    ptime.prinTime()
    url = "https://www.moneycontrol.com/india/stockpricequote/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    stocks = []
    for link in soup.find_all('a', class_='bl_12'):
        stock_name = link.get_text().strip()
        if stock_name=="" or stock_name==" ":
            continue
        stock_price = price(link['href'])
        if stock_price==None:
            continue
        print(stock_name,stock_price)
        stocks.append([stock_name,stock_price])
    ptime.prinTime()
    return stocks

def online():
    import socket
    def is_connected():
        try:
            socket.create_connection(("8.8.8.8", 53))
            return True
        except OSError:
            pass
        return False
    if not is_connected():
        print("Please make sure your device is connected to internet.")
        exit()
online()
print(INDlist())