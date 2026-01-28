# Weather Web Application 🌦️

A simple and responsive Weather Web Application built with Python (Flask) and HTML/CSS.

## Project Structure
```
weather app/
│
├── app.py              # Main Flask Application
├── venv/               # Virtual Environment
├── requirements.txt    # Project Dependencies
├── templates/
│   └── index.html      # Frontend Interface
├── static/
│   └── style.css       # Styles & Backgrounds
└── README.md           # Documentation
```

## Prerequisites
- Python installed on your system.
- An OpenWeatherMap API Key.

## Setup & Run Instructions

1.  **Activate the Virtual Environment**
    - Windows: `venv\Scripts\activate`
    - Mac/Linux: `source venv/bin/activate`

    *(If the `venv` folder is missing, run `python -m venv venv` first)*

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key**
    - Open `app.py`.
    - Find the line: `API_KEY = "YOUR_API_KEY_HERE"`
    - Replace `"YOUR_API_KEY_HERE"` with your actual OpenWeatherMap API key.

4.  **Run the Application**
    ```bash
    python app.py
    ```

5.  **Access the App**
    - Open your browser and go to `http://127.0.0.1:5000/`.

## Features
- **Search**: Enter any city name to get current weather.
- **Dynamic Backgrounds**: The background changes based on the weather (Sunny ☀️, Rainy 🌧️, Cloudy ☁️, etc.).
- **Details**: Shows Temperature, Humidity, Wind Speed, and Description.
