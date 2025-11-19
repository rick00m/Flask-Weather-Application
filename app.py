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

    if request.method == "POST":
        location = request.form.get("location")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}&units=metric"
        userin = requests.get(url)
        store = userin.json()

        if store["cod"] == 200:
            celcius = store["main"]["temp"]
            wtype = store["weather"][0]["description"]
        else:
            error = "Location not found. Please check your spelling."

    return render_template("weather.html", celcius=celcius, wtype=wtype, error=error)

if __name__ == "__main__":
    app.run(debug=True)


