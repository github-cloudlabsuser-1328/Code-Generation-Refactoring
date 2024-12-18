# a simple script to get the weather of a city from the openweathermap api

import requests
import json
import os

def get_weather(city):
    api_key = os.environ.get('WEATHER_API_KEY')

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching data, please try again and ensure you entered a valid city")
        return
    return response.json()

def print_weather(data):
    """Print the weather data in a readable format

    example data:
    ```json
    {
        "coord": {
            "lon": 4.8897,
            "lat": 52.374
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03n"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 280.39,
            "feels_like": 276.32,
            "temp_min": 279.73,
            "temp_max": 281.46,
            "pressure": 1011,
            "humidity": 74,
            "sea_level": 1011,
            "grnd_level": 1011
        },
        "visibility": 10000,
        "wind": {
            "speed": 7.72,
            "deg": 190
        },
        "clouds": {
            "all": 40
        },
        "dt": 1734497702,
        "sys": {
            "type": 2,
            "id": 2012552,
            "country": "NL",
            "sunrise": 1734508004,
            "sunset": 1734535662
        },
        "timezone": 3600,
        "id": 2759794,
        "name": "Amsterdam",
        "cod": 200
    }
    ```
    """
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    print(f'Temperature: {temperature}K')
    print(f'Humidity: {humidity}%')
    print(f'Description: {description}')

def main():
    city = input("Enter city: ")
    weather = get_weather(city)
    print_weather(weather)

if __name__ == "__main__":
    if os.environ.get('WEATHER_API_KEY') is None:
        print("Please set the WEATHER_API_KEY environment variable")
    else:
        main()