<img width="1919" height="825" alt="Screenshot 2025-11-20 213433" src="https://github.com/user-attachments/assets/cc3cb2bb-5ac3-41a4-a1fd-1f99c61f5dc0" />

# Flask Weather App

A modern Flask web application that lets users search and view current weather information for cities worldwide using the OpenWeatherMap API. Includes quick access boxes for popular cities and a detailed weather results page.

---

## Features

* Search weather by city name.
* Displays:

  * Temperature (°C)
  * Weather description
  * Weather icon
  * Feels like temperature
  * Rain/Snow in last hour (if available)
  * Sunrise and Sunset times
  * Humidity
  * Wind speed
* Quick access weather boxes for cities like Dublin and Sydney on the homepage.
* JSON API endpoint: `/api/weather/<city>` for fetching raw weather data.
* Graceful error handling for invalid or empty location input.

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/flask-weather-app.git
cd flask-weather-app
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies:**

```bash
pip install flask requests
```

4. **Set your OpenWeatherMap API key:**

In `app.py`, replace the `key` variable with your own API key from [OpenWeatherMap](https://openweathermap.org/api).

---

## Usage

1. **Run the Flask app:**

```bash
python app.py
```

2. **Open your browser and visit:**

```
http://127.0.0.1:5000/
```

3. **Search for a city** using the input form or click a quick-access location box.

4. **Access JSON weather data via API endpoint:**

```
http://127.0.0.1:5000/api/weather/<city>
```

Example:

```
http://127.0.0.1:5000/api/weather/Dublin
```

---

## Notes

* Supports special mapping for certain cities like Dublin (IE) and Sydney (AU) for more accurate results.
* Sunrise and sunset times are formatted as `HH:MM`.
* Weather icons are pulled dynamically from OpenWeatherMap.
* Fully responsive design for desktop and mobile screens.

---

## License

This project is licensed under the MIT License.

