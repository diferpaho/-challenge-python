import requests

url="https://restcountries.com/v2/name/peru"
r = requests.get(url)
data = r.json()

for i in data:
    print(i["region"])
    print(i["name"])
    print(i["languages"][0]["nativeName"])
