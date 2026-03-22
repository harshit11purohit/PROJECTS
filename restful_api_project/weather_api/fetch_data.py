import requests
from config import API_KEY
#app route methods , response methods 

def fetch_weather_data(city):
    print("[app] City requested:", city)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url)

    if r.status_code != 200:
        return {"error": "Failed to fetch data"}
    
    return r.json()




