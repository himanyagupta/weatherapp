# Weather App

A simple command-line weather app built with Python. Enter a city name and it shows the current weather condition and temperature in both Fahrenheit and Celsius, using the [OpenWeatherMap API](https://openweathermap.org/api).

## Features

- Fetches live weather data for any city
- Shows the weather condition (Clear, Clouds, Rain, etc.)
- Displays temperature in °F and °C
- Keeps the API key out of the code using a `.env` file

## Tech Stack

- Python 3
- `requests` for API calls
- `python-dotenv` for environment variables
- OpenWeatherMap API

## Getting Started

1. Clone the repo:
```bash
   git clone https://github.com/himanyagupta/weatherapp.git
   cd weatherapp
```
2. Install dependencies:
```bash
   pip install requests python-dotenv
```
3. Get a free API key from [openweathermap.org](https://openweathermap.org/api). New keys can take a while to activate.
4. Create a `.env` file in the project folder:
```
   API_KEY=your_api_key_here
```
5. Run the app:
```bash
   python app.py
```

## Example

```
enter city:delhi
the weather in delhi is: Clear
the temperature in delhi is: 82 fahrenheit or 28 celsius
```

## Troubleshooting

- **401 error:** the API key is invalid or not activated yet.
- **`KeyError: 'weather'`:** the API returned an error. Print `weather_data.json()` to see the message.
- **`api_key` is `None`:** make sure the file is named exactly `.env` and sits next to `app.py`.

## Author

Himanya Gupta, [GitHub](https://github.com/himanyagupta)
