# Weather Forecast Telegram Bot

A simple and convenient Telegram bot for getting 3-day weather forecasts. Built with Python using the asynchronous [aiogram](https://docs.aiogram.dev/en/latest/) framework, ensuring high performance and responsiveness.

---

## Features

- 3-day weather forecast for selected cities with detailed information for each day
- Interactive keyboard for city selection
- User access restriction via user_id list
- Easy configuration through `.env` file
- Centralized logging and error handling
- Integration with WeatherAPI service

---

## Requirements

- Python 3.11 or higher
- Dependencies from `requirements.txt` (aiogram, requests, environs, etc.)

---

## Installation and Setup

1. Register your bot with [@BotFather](https://t.me/BotFather) and get the token
2. Get an API key for weather service (e.g., [WeatherAPI](https://www.weatherapi.com/))
3. Clone the repository:

```bash
git clone https://github.com/aleksandr-del/weather-bot.git
cd weather-bot
```

4. Create a `.env` file in the project root and add:

```env
BOT_TOKEN=your_bot_token
WEATHER_API_KEY=your_weather_api_key
USER_IDS=123456789,987654321  # Comma-separated list of user_ids who can use the bot
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the bot:

```bash
python main.py
```

---

## How to Use

- Send the `/start` command to begin and get a welcome message with city selection keyboard
- Choose a city from the available buttons to get a detailed 3-day forecast
- In case of an error, the bot will notify about the inability to retrieve weather data

---

## Weather Data Format

The bot provides detailed weather information in Russian with emojis:

```
🌤️ Прогноз погоды для Moscow

📅 СЕГОДНЯ (2025-10-28)
   🌡️ Температура: 15°C
   ☔ Вероятность дождя: 20%
   ❄️ Вероятность снега: 0%

📅 ЗАВТРА (2025-10-29)
   🌡️ Температура: 12°C
   ☔ Вероятность дождя: 45%
   ❄️ Вероятность снега: 5%

📅 ПОСЛЕЗАВТРА (2025-10-30)
   🌡️ Температура: 8°C
   ☔ Вероятность дождя: 60%
   ❄️ Вероятность снега: 15%
```

---

## Project Structure

```
.
├── main.py                    # Entry point, bot startup and router setup
├── handlers/                  # Command and message handlers
│   └── user.py               # Main handlers for user interaction
├── filters/                   # Custom filters (e.g., UserFilter for access control)
│   └── filters.py
├── keyboard/                  # Keyboards for city selection
│   ├── keyboard.py           # Dynamic keyboard generation
│   └── cities.py             # City configuration
├── service/                   # Weather API integration
│   └── weather_forecast.py   # WeatherAPI service and message formatting
├── config/                    # Configuration loading from .env
│   └── config.py
├── logger/                    # Logging configuration
│   └── settings.py
├── requirements.txt           # Project dependencies
└── README.md                 # Current documentation
```

---

## Configuration

### Supported Cities

Currently configured cities (can be modified in `keyboard/cities.py`):
- Moscow
- Tomsk  
- Nürnberg

### Adding New Cities

To add more cities, simply edit the `cities` list in `keyboard/cities.py`:

```python
cities = "Moscow Tomsk Nürnberg Berlin Paris".split()
```

---

## Tech Stack

- **Python 3.11+**
- **aiogram 3.x** - Telegram Bot API framework
- **WeatherAPI** - Weather data provider
- **requests** - HTTP client for API calls
- **environs** - Environment variable management
- **Modular architecture** - Clean separation of concerns

---

## API Integration

The bot uses [WeatherAPI.com](https://www.weatherapi.com/) to fetch weather data. The service provides:
- Current weather conditions
- 3-day forecast
- Precipitation probabilities
- Temperature data in Celsius

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

This project is open source and available under the MIT License.

---

## Note

The bot interface and weather messages are in Russian language, designed for Russian-speaking users. All weather data, dates, and user interactions are displayed in Russian with appropriate emojis and formatting.
