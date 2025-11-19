from flask import Flask, render_template, request
import requests

app = Flask(__name__)

key = "HIDDEN API KEY".strip()

@app.route("/", methods=["GET"])
def home_get():
    return render_template("home.html")

@app.route("/weather", methods=["GET", "POST"])
def weather_getpost(): 
    celcius = None
    wtype = None
    error = None
    gradient = "linear-gradient(to bottom, #fceabb, #f8b500)" 

    if request.method == "POST":
        location = request.form.get("location")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}&units=metric"
        userin = requests.get(url)
        store = userin.json()

        if store["cod"] == 200:
            celcius = store["main"]["temp"]
            wtype = store["weather"][0]["description"]
            
            weather_gradients = {
            "clear": "linear-gradient(to bottom, #fceabb, #f8b500)",             # sunny
            "clouds": "linear-gradient(to bottom, #bdc3c7, #2c3e50)",            # cloudy
            "rain": "linear-gradient(to bottom, #4e54c8, #8f94fb)",              # rain
            "drizzle": "linear-gradient(to bottom, #89f7fe, #66a6ff)",           # drizzle
            "thunderstorm": "linear-gradient(to bottom, #0f0c29, #302b63, #24243e)", # storm
            "snow": "linear-gradient(to bottom, #e6dada, #274046)",              # snow
            "mist": "linear-gradient(to bottom, #606c88, #3f4c6b)",              # mist/fog
            "smoke": "linear-gradient(to bottom, #3e5151, #decba4)",             # smoke
            "haze": "linear-gradient(to bottom, #3e5151, #6190E8)",              # haze
            "dust": "linear-gradient(to bottom, #b79891, #94716b)",              # dust
            "fog": "linear-gradient(to bottom, #757f9a, #d7dde8)",               # fog
            "sand": "linear-gradient(to bottom, #e4c37f, #e0aa55)",              # sand
            "ash": "linear-gradient(to bottom, #606c88, #3f4c6b)",               # volcanic ash
            "squall": "linear-gradient(to bottom, #485563, #29323c)",            # squall
            "tornado": "linear-gradient(to bottom, #000000, #434343)",           
            }

            gradient = weather_gradients.get(wtype, gradient)

        else:
            error = "Location not found. Please check your spelling."

    return render_template("weather.html", celcius=celcius, wtype=wtype, error=error)

if __name__ == "__main__":
    app.run(debug=True)

