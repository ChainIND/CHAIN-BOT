import os
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", "10000"))
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing")

if not RENDER_EXTERNAL_URL:
    raise RuntimeError("RENDER_EXTERNAL_URL is missing")

app = Flask(__name__)

telegram_app = Application.builder().token(TOKEN).build()


async def start(update: Update, context):
    await update.message.reply_text(
        "👋 Welcome to CHAIN Bot!\n\n"
        "🛠️ INDIAN JTAG TEAM\n\n"
        "/help - Commands\n"
        "/status - Bot status"
    )


async def help_command(update: Update, context):
    await update.message.reply_text(
        "🤖 CHAIN Bot\n\n"
        "/start - Start bot\n"
        "/help - Help\n"
        "/status - Status"
    )


async def status(update: Update, context):
    await update.message.reply_text(
        "🟢 CHAIN Bot is Online!\n"
        "⚡ Status: Active"
    )


telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("help", help_command))
telegram_app.add_handler(CommandHandler("status", status))


@app.route("/")
def home():
    return "CHAIN Bot is Online 🟢", 200


@app.route("/health")
def health():
    return "OK", 200


@app.route("/webhook", methods=["POST"])
async def webhook():
    try:
        data = request.get_json(force=True)

        update = Update.de_json(
            data,
            telegram_app.bot
        )

        await telegram_app.process_update(update)

        return "OK", 200

    except Exception as e:
        logging.exception("Webhook error")
        return "ERROR", 500


async def initialize_bot():
    await telegram_app.initialize()

    webhook_url = f"{RENDER_EXTERNAL_URL}/webhook"

    await telegram_app.bot.delete_webhook()

    await telegram_app.bot.set_webhook(
        url=webhook_url
    )

    logging.info("=================================")
    logging.info("CHAIN BOT STARTED")
    logging.info("Webhook: %s", webhook_url)
    logging.info("=================================")


if __name__ == "__main__":
    import asyncio

    asyncio.run(initialize_bot())

    app.run(
        host="0.0.0.0",
        port=PORT
    )
