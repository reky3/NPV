import sqlite3
 
DB_NAME = "weather.db"
 
 
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
 
    c.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mesto TEXT,
            teplota REAL,
            vlhkost REAL,
            pocasie TEXT,
            datum TEXT
        )
    """)
 
    conn.commit()
    conn.close()
