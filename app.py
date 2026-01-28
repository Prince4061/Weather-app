from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# REPLACE THIS WITH YOUR OPENWEATHERMAP API KEY
API_KEY = "30d8831ae8bd7c6ea65ab173bd366e9f"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None
    background_class = "default"

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            try:
                params = {
                    "q": city,
                    "appid": API_KEY,
                    "units": "metric"  # For Celsius
                }
                response = requests.get(BASE_URL, params=params)
                data = response.json()

                if response.status_code == 200:
                    weather_data = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temp": round(data["main"]["temp"]),
                        "humidity": data["main"]["humidity"],
                        "wind_speed": data["wind"]["speed"],
                        "description": data["weather"][0]["description"].title(),
                        "icon": data["weather"][0]["icon"],
                        "main": data["weather"][0]["main"]
                    }
                    
                    # Determine background class based on weather condition
                    main_weather = weather_data["main"].lower()
                    if "rain" in main_weather or "drizzle" in main_weather:
                        background_class = "rainy"
                    elif "clear" in main_weather:
                        background_class = "sunny"
                    elif "cloud" in main_weather:
                        background_class = "cloudy"
                    elif "snow" in main_weather:
                        background_class = "snowy"
                    elif "mist" in main_weather or "haze" in main_weather or "fog" in main_weather:
                        background_class = "misty"
                    else:
                        background_class = "default"
                        
                else:
                    error_message = f"City not found or API error: {data.get('message', 'Unknown error')}"
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
        else:
            error_message = "Please enter a city name."

    return render_template("index.html", weather=weather_data, error=error_message, background_class=background_class)

if __name__ == "__main__":
    app.run(debug=True)
