from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime 


app = Flask(__name__)

key = "HIDDEN KEY".strip()

@app.route("/", methods=["GET"])
def home_get():
    return render_template("home.html")

@app.route("/api/weather/<city>")
def home_weather(city):
    country_map = {
        "Dublin": "IE",
        "Sydney": "AU"
    }
    country = country_map.get(city, "")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}{',' + country if country else ''}&appid={key}&units=metric"
    userin = requests.get(url)
    store = userin.json()
    return jsonify(store)

@app.route("/weather", methods=["GET", "POST"])
def weather_getpost():
    celcius = None
    wtype = None
    icon = None
    error = None
    location = None
    feels_like = None
    rain_1h = None
    snow_1h = None
    sunrise = None
    sunset = None
    humidity = None
    wind_speed = None

    if request.method == "POST":
        location = request.form.get("location")
        if location:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}&units=metric"
            resp = requests.get(url)
            store = resp.json()

            if store.get("cod") == 200:
                celcius = store["main"]["temp"]
                wtype = store["weather"][0]["description"]
                icon = store["weather"][0]["icon"]
                feels_like = store["main"].get("feels_like")         
                rain_1h = store.get("rain", {}).get("1h")            
                snow_1h = store.get("snow", {}).get("1h")          
                sunrise = store["sys"].get("sunrise")
                sunset = store["sys"].get("sunset")
                humidity = store["main"].get("humidity")
                wind_speed = store["wind"].get("speed")
            else:
                error = "Location not found. Please check your spelling."
        else:
            error = "Please enter a location."

    return render_template(
        "weather.html",
        location=location,
        celcius=celcius,
        wtype=wtype,
        icon=icon,
        error=error,
        feels_like=feels_like,
        rain_1h=rain_1h,
        snow_1h=snow_1h,
        sunrise=sunrise,
        sunset=sunset,
        humidity=humidity,
        wind_speed=wind_speed
    )


@app.template_filter('datetimeformat')
def datetimeformat(value):
    if value is None:
        return "—"
    return datetime.fromtimestamp(value).strftime("%H:%M")

if __name__ == "__main__":
    app.run(debug=True)

