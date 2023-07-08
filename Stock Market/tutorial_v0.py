import requests
from bs4 import BeautifulSoup

def price(url):
    response = requests.get(url)    
    soup = BeautifulSoup(response.content, "html.parser")
    my_div = soup.find("div", id="nsecp")
    my_text = my_div.text.strip()
    print(my_text)

url = "https://www.moneycontrol.com/india/stockpricequote/power-generationdistribution/adanipower/AP11"
price(url)