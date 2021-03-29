# get data from sh.lianjia.com
# get location from gaode api
# calcuate the distance of houses
import requests
import re
import random
from urllib import parse 
from pyquery import PyQuery as pq
import json
from geopy import distance

def get_data():

    titles = []
    prices = []

    base_url = "http://sh.lianjia.com/chengjiao/pg"
    for i in range(1, 5):
        url = base_url + str(i)
        timeout = random.random() * 100
        response = requests.get(url=url, timeout=timeout)
        doc = pq(response.text)

        title = doc('.info .title').text()
        title = re.sub(r"\d室\d厅 ", "", title)
        title = re.sub(r" \d*\.?\d*平米", "", title)
        title = title.split(" ")
        titles = titles + title

        price = doc('.totalPrice .number').text()
        price = price.split(" ")
        prices = prices + price

    # save data
    with open("data/titles.txt", "a") as f:
        for item in titles:
            f.write(f"{item}\n")
    with open("data/prices.txt", "a") as f:
        for item in prices:
            f.write(f"{item}\n")

def get_location():
    locations = []
    with open("data/titles.txt", 'r') as f:
        titles = f.read().split("\n")
        
    base_url = "https://restapi.amap.com/v3/place/text?"
    parameters = {
        "key": "",
        "types": "120000",
        "city": "021",
        "citylimit": "true"
    }
    for item in titles:
        parameters["keywords"] = item
        url = base_url + parse.urlencode(parameters)
        response = requests.get(url=url)
        response = json.loads(response.text)
        location = response["pois"][0]["location"]
        locations.append(location)
    with open("data/locations.txt", 'a') as f:
        for item in locations:
            f.write(f"{item}\n")

def get_distance():
    distances = []
    people_square = (31.228816, 121.475164)
    with open("data/locations.txt", 'r') as f:
        locations = f.read().split("\n")
    # locations[i][0] longtitude
    # locations[i][i] latitude
    for i in range(0, len(locations)):
        locations[i] = locations[i].split(",")
        locations[i] = (float(locations[i][1]), float(locations[i][0]))
        distances.append(distance.distance(people_square, locations[i]).km)
    for i in range(0, len(distances)):
        distances[i] = round(distances[i], 2)
    with open("data/distances.txt", "a") as f:
        for item in distances:
            f.write(f"{item}\n")

if __name__ == "__main__":
    get_data()
    get_location()
    get_distance()