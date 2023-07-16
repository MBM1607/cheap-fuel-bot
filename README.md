![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Python](https://img.shields.io/badge/Python-2CA5E0?style=for-the-badge&logo=python&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-e06d10?style=for-the-badge&logo=cloudflare&logoColor=white)

# Introduction

This is a simple telegram bot that can be added to any group. It will display
the all the fuel prices for the selected province in Australia.

It uses the [Cloudflare Workers](https://workers.cloudflare.com/) to host the bot.
The bot is written in [Python](https://www.python.org/) and uses the
[python-telegram-bot](https://python-telegram-bot.org/)
library to interact with the Telegram API.

## Usage

To use the bot, simply add it to your group and type `/start` or `/help` to
display the help message containing all the commands.

## Commands

| Command  | Description                                                                     |
| -------- | ------------------------------------------------------------------------------- |
| `/start` | Start the bot, this also displays the help message containing all the commands. |
| `/help`  | Display the help message containing all the commands.                           |
| `ALL`    | Display prices for all australian provinces.                                    |
| `NSW`    | Display prices for New South Wales.                                             |
| `QLD`    | Display prices for Queensland.                                                  |
| `VIC`    | Display prices for Victoria.                                                    |
| `WA`     | Display prices for Western Australia.                                           |
