import requests

def get_weather(city):
    API_KEY = 'b81d207631a96f8f3c9f43cf72abebb6'
    BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(BASE_URL)
    data = response.json()
    
    if response.status_code == 200:
        main = data.get('main')
        weather = data.get('weather')
        if main and weather:
            print(f"Temperature: {main['temp']}")
            print(f"Humidity: {main['humidity']}")
            print(f"Weather: {weather[0]['description']}")
        else:
            print("Error: Unexpected response structure.")
    else:
        print(f"Error: {data.get('message', 'Failed to retrieve data')}")

city = input("Enter the city: ")
get_weather(city)