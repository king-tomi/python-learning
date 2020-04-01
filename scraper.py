import requests
from bs4 import BeautifulSoup
from requests import RequestException
import json
import pandas as pd

url = "https://www.weforum.org/agenda/2020/02/coronavirus-covid-19-threat-opinion-poll-public-concern/"
def parse_request(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")
        return soup
    except RequestException:
        return None

soup = parse_request(url)

result = soup.find_all(class_="st__content-block st__content-block--list")
co_list = []
for item in result:
    co_list.append(item.find('ul'))
final = []
for ul in co_list:
    final.append(ul.find("li"))

new = []
for item in final:
    new.append(item.text)


data = pd.DataFrame(new,columns=["Opinions"])
data.to_csv("opinions.csv")
