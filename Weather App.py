import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            'City': data['name'],
            'Temperature': f"{data['main']['temp']}°C",
            'Weather': data['weather'][0]['description'].title(),
            'Humidity': f"{data['main']['humidity']}%",
            'Wind Speed': f"{data['wind']['speed']} m/s"
        }
        return weather
    else:
        return {'Error': 'City not found or API issue'}

# Replace 'your_api_key_here' with your actual API key
API_KEY = 'de0f135e3854f55bfa0b680d5f0c6fb3'

if __name__ == "__main__":
    city = input("Enter the city name: ")
    weather_info = get_weather(city, API_KEY)
    
    print("\n📍 Weather Report:")
    for key, value in weather_info.items():
        print(f"{key}: {value}")
