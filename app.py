from flask import Flask, request
import telegram

import config
from utils import fetch_prices

bot = telegram.Bot(token=config.BOT_TOKEN)

app = Flask(__name__)


@app.route("/{}".format(config.BOT_TOKEN), methods=["POST"])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    def send_message(text):
        bot.send_message(
            chat_id=update.message.chat.id,
            text=text,
            reply_to_message_id=update.message.message_id,
            parse_mode=telegram.ParseMode.MARKDOWN_V2,
        )

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode("utf-8").decode()

    # the first time you chat with the bot AKA the welcoming message
    send_message(config.WELCOME_MESSAGE if text == "/start" else fetch_prices(text))

    return "ok"


@app.route("/set_webhook", methods=["GET", "POST"])
def set_webhook():
    s = bot.setWebhook("{URL}{HOOK}".format(URL=config.BOT_URL, HOOK=config.BOT_TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route("/")
def index():
    return "."


if __name__ == "__main__":
    app.run(threaded=True)
