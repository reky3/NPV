from datetime import datetime
import sqlite3
 
from database import DB_NAME, init_db
from weather import get_weather
 
# mestá ktoré sa budú automaticky ukladať
CITIES = [
    "Bratislava",
    "Košice",
    "Prešov",
]
 
# vytvor databázu ak ešte neexistuje
init_db()
 
 
def add_weather(city):
 
    temp, humidity, weather_desc = get_weather(city)
 
    if temp is None:
        return
 
    datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
 
    c.execute("""
        INSERT INTO weather_data
        (mesto, teplota, vlhkost, pocasie, datum)
        VALUES (?, ?, ?, ?, ?)
    """, (city, temp, humidity, weather_desc, datum))
 
    conn.commit()
    conn.close()
 
    print(f"{city} uložené ({datum})")
 
 
if __name__ == "__main__":
 
    for city in CITIES:
        add_weather(city)
