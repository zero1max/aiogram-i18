# Aiogram-i18n Telegram Bot

This is a simple Telegram bot built with [aiogram](https://github.com/aiogram/aiogram) v3 and [aiogram-i18n](https://github.com/aiogram/aiogram-i18n) for internationalization (i18n). The bot supports English, Russian, and Uzbek languages, and demonstrates how to use Fluent `.ftl` files for translations.

## Features

- `/start` command: Greets the user in their selected language.
- `/help` command: Provides help text.
- Language selection: Users can switch between Uzbek 🇺🇿, Russian 🇷🇺, and English 🇬🇧 using keyboard buttons.
- Uses aiogram-i18n middleware for dynamic language switching.
- All messages are translated using Fluent `.ftl` files.

## Project Structure

```
aiogram-i18/
  handlers/
    common.py         # Bot command and message handlers
  keyboards/
    default.py        # Main reply keyboard with language selection
  locales/
    en/ru/uz/         # Translation files for each language
      LC_MESSAGES/
        messages.ftl
  main.py             # Bot entry point
  requirements.txt    # Python dependencies
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd aiogram-i18
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root with your bot token:
     ```
     BOT_TOKEN=your-telegram-bot-token-here
     ```

## Usage

Start the bot with:

```bash
python main.py
```

The bot will respond to `/start` and `/help` commands, and allow users to change the language using the provided keyboard.

## Localization

- Translation files are located in `locales/<lang>/LC_MESSAGES/messages.ftl`.
- Example keys:
  - `hello`: Greeting message with username.
  - `help`: Help text.

## Dependencies

See `requirements.txt` for the full list. Main dependencies:
- aiogram
- aiogram-i18n
- python-dotenv
- fluent.runtime

## License

MIT 