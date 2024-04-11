from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/')
def get_weather():
    # Obtenir les paramètres de requête
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    api_key = os.getenv('OPENWEATHER_API_KEY')

    if not all([latitude, longitude, api_key]):
        return "Les variables d'environnement LATITUDE, LONGITUDE, et OPENWEATHER_API_KEY sont requises.", 400

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return jsonify({
            "city": data['name'],
            "country": data['sys']['country'],
            "weather_description": weather_description,
            "temperature": temperature
        })
    else:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
