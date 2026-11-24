import requests
 
 
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
 
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
 
        data = response.json()
        current = data["current_condition"][0]
 
        temp = float(current["temp_C"])
        humidity = float(current["humidity"])
        weather_desc = current["weatherDesc"][0]["value"]
 
        return temp, humidity, weather_desc
 
    except Exception as e:
        print(f"Chyba pri získavaní počasia pre {city}: {e}")
        return None, None, None

