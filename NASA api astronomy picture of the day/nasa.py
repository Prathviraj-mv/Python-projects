import requests

# api key can be found in nasa website
# lastest astromony picture of the day will be displayed 


api_end = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": "ur api key"
}

response = requests.get(api_end, params=params)
data = response.json()
image_url = data["hdurl"]
print(image_url)




