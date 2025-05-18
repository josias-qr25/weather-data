import requests

def extract_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code,relative_humidity_2m&temperature_unit=fahrenheit"

    print("Fetching weather data...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Requests error: {e}")
    return {}

def display_weather(weather_data):
    if not weather_data or 'current' not in weather_data:
        print("No weather data available.")
        return

    temp = weather_data['current']['temperature_2m']
    humidity = weather_data['current']['relative_humidity_2m']
    weather_code = weather_data['current']['weather_code']

    weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Light rain",
            63: "Moderate rain",
            65: "Heavy rain"
    }
    condition = weather_codes.get(weather_code, "Unknown")

    print("\nCurrent Weather!")
    print(f"Temperature: {temp}F")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")

def main():
    print("Input Coordinates to Get Weather Data")
    latitude = str(input("Latitude: "))
    longitude = str(input("Longitude: "))
    weather_data = extract_weather(latitude,longitude)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
