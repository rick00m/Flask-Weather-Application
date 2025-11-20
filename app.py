from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

key = "d0a996d6caf95ca6c84f14a0c4bce795".strip()

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
        error=error
    )



if __name__ == "__main__":
    app.run(debug=True)
