import requests
import json
import datetime

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"  # "metric" For Celsius, change to "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)
    return weather_data

def get_current_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

def display_weather(weather_data):
    if weather_data["cod"] != "404":
        main_info = weather_data["weather"][0]["main"]
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        current_time = get_current_time()
        print("Weather at your location:")
        print(f"Condition: {main_info} ({description})")
        print(f"Temperature: {temperature}°F")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Time: {current_time}")
        print("---------------------------")
    else:
        print("Weather information not available.")

# Example usage
api_key = "5fdb6f142da1debc1b47015c2ad9e647"  # Replace with your OpenWeatherMap API key
city = "Tustin, US"  # Replace with your city name
weather_data = get_weather(api_key, city)
display_weather(weather_data)
