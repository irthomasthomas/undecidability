**Prompt:**
Write an interesting and unique shell script that uses curl and public apis

**Response:**
Script: Daily Inspiration and Weather Forecast

Description:
This script fetches a daily inspirational quote and the current weather forecast for a specified location. It uses the `zenquotes.io` API for the quote and the `OpenWeatherMap` API for weather data. Replace `YOUR_OPENWEATHERMAP_API_KEY` with your actual API key from OpenWeatherMap and set `LOCATION` to your desired location.

```sh
#!/bin/bash

# Variables
API_KEY="YOUR_OPENWEATHERMAP_API_KEY"
LOCATION="London,uk" # Format: city,country_code
QUOTE_API="https://zenquotes.io/api/today"
WEATHER_API="http://api.openweathermap.org/data/2.5/weather"

# Fetch Inspirational Quote
quote_response=$(curl -s "$QUOTE_API")
quote_text=$(echo $quote_response | jq -r '.[0].q')
quote_author=$(echo $quote_response | jq -r '.[0].a')

# Fetch Weather Data
weather_response=$(curl -s "$WEATHER_API?q=$LOCATION&appid=$API_KEY&units=metric")
weather_condition=$(echo $weather_response | jq -r '.weather[0].main')
temperature=$(echo $weather_response | jq -r '.main.temp')

# Output
echo "Today's Inspiration: \"$quote_text\" - $quote_author"
echo "Weather in $LOCATION: $weather_condition, ${temperature}°C"
```

Save the script as `daily_inspiration_weather.sh`, give it execute permissions with `chmod +x daily_inspiration_weather.sh`, and run it in the terminal.

Explanation:
1. The script sets up variables for API keys and endpoints.
2. It uses `curl` to fetch data from the `zenquotes.io` API for the inspirational quote.
3. It parses the JSON response with `jq` to extract the quote and author.
4. It then uses `curl` to fetch weather data from OpenWeatherMap using the specified `LOCATION` and `API_KEY`.
5. The JSON response from the weather API is parsed to get the main weather condition and the temperature.
6. Finally, it prints out both the inspirational quote and the weather details to the terminal.

Ensure `jq` is installed on the system for JSON parsing, and substitute `YOUR_OPENWEATHERMAP_API_KEY` with a valid API key from OpenWeatherMap.

<details><summary>Metadata</summary>

- Duration: 33539 ms
- Datetime: 2023-12-26T18:58:40.655904
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 1.0}
```

