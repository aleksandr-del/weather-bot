```md
# Weather-Bot

Weather-Bot — это простой и удобный Telegram-бот для получения прогноза погоды на ближайшие три дня, написанный на Python с использованием асинхронного фреймворка aiogram.

---

## Основные возможности

- Получение прогноза погоды на 3 дня для выбранного города
- Простой интуитивный интерфейс с клавиатурой для выбора города
- Обработка команд и сообщений с помощью aiogram 3.x
- Конфигурация через .env файл для хранения API ключей и списка пользователей
- Логирование событий и ошибок
- Фильтр доступа по user_id

---

## Требования

- Python 3.11+
- Библиотеки из `requirements.txt`, включая aiogram, requests, environs и другие

---

## Быстрый старт

1. Создать Telegram-бота в @BotFather и получить токен
2. Получить API ключ для сервиса погоды (например, WeatherAPI)
3. Клонировать репозиторий:
```

git clone https://github.com/aleksandr-del/weather-bot.git
cd weather-bot

```
4. Создать файл `.env` в корне проекта со следующими переменными:
```

BOT_TOKEN=your_telegram_bot_token
WEATHER_API_KEY=your_weather_api_key
USER_IDS=123456789,987654321

```
5. Установить зависимости:
```

pip install -r requirements.txt

```
6. Запустить бота:
```

python main.py

```

---

## Использование

- Отправьте команду `/start` для начала работы и вывода приветственного сообщения с клавиатурой
- Выберите город из списка кнопок для получения прогноза погоды
- При успешном запросе бот выдаст прогноз на сегодня, завтра и послезавтра с температурой и вероятностью осадков
- В случае ошибки вы получите уведомление об невозможности получить прогноз

---

## Структура проекта

- `main.py` — основной скрипт запуска бота
- `handlers/` — обработчики команд и сообщений (например, `user.py`)
- `filters/` — пользовательские фильтры (например, `UserFilter` для ограничения доступа)
- `keyboard/` — формирование клавиатур с городами
- `service/` — логика получения прогноза погоды через WeatherAPI (`weather_forecast.py`)
- `config/` — загрузка настроек из `.env` с помощью environs
- `logger/` — настройка логирования

---

## Рекомендации по развитию

- Добавить асинхронные HTTP запросы для повышения отзывчивости
- Расширить список городов и добавить навигацию по клавиатуре
- Реализовать кэширование запросов для снижения нагрузки на API
- Добавить поддержку языков и единиц измерения
- Улучшить обработку ошибок и логирование

---

## Лицензия

Проект распространяется под MIT License.

---

Если возникнут вопросы или нужны улучшения, обращайтесь!
```

<span style="display:none">[^1][^10][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://docs.aiogram.dev/en/v2.25.1/examples/

[^2]: https://github.com/pluresque/awesome-aiogram

[^3]: https://docs.aiogram.dev/en/latest/api/bot.html

[^4]: https://github.com/welel/aiogram-bot-template

[^5]: https://aiogram-birdi7.readthedocs.io/en/latest/examples/

[^6]: https://docs.aiogram.dev/en/v2.25.1/examples/echo_bot.html

[^7]: https://docs.aiogram.dev/en/latest/utils/formatting.html

[^8]: https://aiogram-birdi7.readthedocs.io/en/latest/

[^9]: https://docs.aiogram.dev/en/v2.25.1/

[^10]: https://docs.aiogram.dev/en/latest/api/index.html

