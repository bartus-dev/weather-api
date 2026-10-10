# Weather API

A command-line weather application written in Python that retrieves current weather conditions and a multi-day forecast for a city selected by the user.

## Features

- Search for a city by name and country.
- Retrieve current temperature, humidity, and wind speed.
- Display weather conditions using human-readable descriptions.
- Show daily minimum and maximum temperatures for the upcoming days.
- Handle HTTP errors when connecting to the APIs.

## Technologies

- Python
- Requests
- Open-Meteo Forecast API
- Open-Meteo Geocoding API

## Requirements

- Python 3
- The dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/bartus-dev/weather-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd weather-api
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Usage

Run the application:

```bash
python main.py
```

Enter a city name and country when prompted. The application will display the current weather and the forecast for the following days.

## APIs

Weather data is provided by [Open-Meteo](https://open-meteo.com/).

- [Forecast API](https://open-meteo.com/en/docs)
- [Geocoding API](https://open-meteo.com/en/docs/geocoding-api)

## License

This project is available under the MIT License.
