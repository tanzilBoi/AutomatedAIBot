import requests

url="https://official-joke-api.appspot.com/jokes/random"
json_data=requests.get(url).json()

arr=["",""]
arr[0]=json_data["setup"]
arr[1]=json_data["punchline"]

def joke():
    return arr