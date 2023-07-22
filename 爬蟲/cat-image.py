import requests
import json

i = int(input())
url = "https://api.thecatapi.com/v1/images/search"

for ii in range(0,i):
    response = requests.get(url)
    data = json.loads(response.text)
    urls = data[0]["url"]
    with open("result.json", "a") as f:
        f.write("\n".join(urls) + "\n")

