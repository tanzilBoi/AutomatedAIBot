import requests
from newsapi import NewsApiClient
from apikey import api_key_for_news

api_address = "https://newsapi.org/v2/everything?q=keyword&apiKey="+ api_key_for_news
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append("Number "+ str(i+1) + ", " + json_data["articles"][i]["title"]+ ".")

    return ar

#ar=news()

#print(arr)