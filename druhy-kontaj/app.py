from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime
 
from database import DB_NAME, init_db
from weather import get_weather
 
app = Flask(__name__)
 
# vytvor databázu pri štarte aplikácie
init_db()
 
 
@app.route("/")
def index():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
 
    c.execute("SELECT * FROM weather_data ORDER BY id DESC")
    data = c.fetchall()
 
    conn.close()
 
    return render_template("index.html", data=data)
 
@app.route("/add", methods=["POST"])
def add():
 
    mesto = request.form["mesto"]
 
    teplota, vlhkost, pocasie = get_weather(mesto)
 
    if teplota is None:
        return "Nepodarilo sa získať počasie.", 400
 
    datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
 
    c.execute("""
        INSERT INTO weather_data
        (mesto, teplota, vlhkost, pocasie, datum)
        VALUES (?, ?, ?, ?, ?)
    """, (mesto, teplota, vlhkost, pocasie, datum))
 
    conn.commit()
    conn.close()
 
    return redirect("/")
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

