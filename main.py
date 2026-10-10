import requests

def get_weather(latitude, longitude, url):
    params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "wind_speed_10m",
                "weather_code"
            ],

            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "weather_code"
            ]
        }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        print("Error connecting to API")
        return None

    daily = data["daily"]

    forecast = []

    for i in range(1, len(daily["time"])):
        date = daily["time"][i]
        max_temp = daily["temperature_2m_max"][i]
        min_temp = daily["temperature_2m_min"][i]
        weather_code2 = daily["weather_code"][i]

        forecast.append((date, min_temp, max_temp, weather_code2))

    temperature = data["current"]["temperature_2m"]
    humidity = data["current"]["relative_humidity_2m"]
    wind = data["current"]["wind_speed_10m"]
    weather_code = data["current"]["weather_code"]

    return temperature, humidity, wind, weather_code, forecast
    
def get_coordinates(city, country):
    url_coding = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json"

    try:
        response_coding = requests.get(url_coding)
        response_coding.raise_for_status()
        data_coding = response_coding.json()
    except requests.RequestException:
        print("Error connecting to API")
        return None
    
    latitude = None
    longitude = None
    found = False

    for i in data_coding["results"]:
        if country == i["country"]:
            latitude = i["latitude"]
            longitude = i["longitude"]
            found = True
            break

    return latitude, longitude, found

def display_weather(temperature, humidity, wind, weather_code, forecast):
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        95: "Thunderstorm"
    }

    print("\nToday:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind}km/h")
    print(f"Weather: {weather_codes.get(weather_code, 'Unknown')}")
    print()
    print("Forecast: ")
    for date, min_temp, max_temp, weather_code2 in forecast:
        weather = weather_codes.get(weather_code2, "Unknown")

        print(
            f"{date} | Min: {min_temp}°C | "
            f"Max: {max_temp}°C | "
            f"Weather: {weather}"
        )



WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

city = input("City: ")
country = input("Country: ")


coordinates = get_coordinates(city, country)

if coordinates is not None:
    latitude, longitude, found = coordinates
    if found:
        result = get_weather(latitude, longitude, WEATHER_URL)

        if result is not None:
            temperature, humidity, wind, weather_code, forecast = result
            display_weather(temperature, humidity, wind, weather_code, forecast)
    else:
        print("\nCity not found")
else:
    print("Error connecting to API")

