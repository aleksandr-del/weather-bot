import requests
from requests.exceptions import HTTPError


def _create_message(data: dict) -> str:
    location = data["location"]
    current = data["current"]
    forecast = data["forecast"]["forecastday"]

    message = f"""🌤️  Прогноз погоды для {location["name"]}
{"=" * 30}

📅 СЕГОДНЯ ({forecast[0]["date"]})
   🌡️  Температура: {current["temp_c"]}°C
   ☔  Вероятность дождя: {current["daily_chance_of_rain"]}%
   ❄️  Вероятность снега: {current["daily_chance_of_snow"]}%

📅 ЗАВТРА ({forecast[1]["date"]})
   🌡️  Температура: {forecast[1]["day"]["avgtemp_c"]}°C
   ☔  Вероятность дождя: {forecast[1]["day"]["daily_chance_of_rain"]}%
   ❄️  Вероятность снега: {forecast[1]["day"]["daily_chance_of_snow"]}%

📅 ПОСЛЕЗАВТРА ({forecast[2]["date"]})
   🌡️  Температура: {forecast[2]["day"]["avgtemp_c"]}°C
   ☔  Вероятность дождя: {forecast[2]["day"]["daily_chance_of_rain"]}%
   ❄️  Вероятность снега: {forecast[2]["day"]["daily_chance_of_snow"]}%"""

    return message


def get_weather_forecast(api_key: str, city: str) -> str | None:
    base_url = "http://api.weatherapi.com/v1"
    api_method = "/forecast.json"
    params = {
        "key": api_key,
        "q": city,
        "days": "3",
        "hour": "12",
        "lang": "de",
    }
    headers = {"Content-Type": "application/json"}
    url = base_url + api_method
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        filtered_data = {
            "location": {
                "name": data["location"]["name"],
                "country": data["location"]["country"],
            },
            "current": {
                "last_updated": data["current"]["last_updated"],
                "temp_c": data["current"]["temp_c"],
                "daily_chance_of_rain": data["forecast"]["forecastday"][0]["day"].get(
                    "daily_chance_of_rain", 0
                ),
                "daily_chance_of_snow": data["forecast"]["forecastday"][0]["day"].get(
                    "daily_chance_of_snow", 0
                ),
            },
            "forecast": {
                "forecastday": [
                    {
                        "date": day["date"],
                        "day": {
                            "avgtemp_c": day["day"]["avgtemp_c"],
                            "daily_chance_of_rain": day["day"].get(
                                "daily_chance_of_rain", 0
                            ),
                            "daily_chance_of_snow": day["day"].get(
                                "daily_chance_of_snow", 0
                            ),
                        },
                    }
                    for day in data["forecast"]["forecastday"]
                ]
            },
        }
        return _create_message(filtered_data)

    except HTTPError as err:
        logger.error(err)
        return
