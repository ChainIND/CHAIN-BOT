import os
import logging

from quart import Quart, request
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

app = Quart(__name__)

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


@app.get("/")
async def home():
    return "CHAIN Bot is Online 🟢", 200


@app.get("/health")
async def health():
    return "OK", 200


@app.post("/webhook")
async def webhook():
    try:
        data = await request.get_json()

        update = Update.de_json(
            data,
            telegram_app.bot
        )

        await telegram_app.process_update(update)

        return "OK", 200

    except Exception:
        logging.exception("Webhook error")
        return "ERROR", 500


@app.before_serving
async def startup():

    await telegram_app.initialize()
    await telegram_app.start()

    webhook_url = f"{RENDER_EXTERNAL_URL}/webhook"

    await telegram_app.bot.delete_webhook()

    await telegram_app.bot.set_webhook(
        url=webhook_url
    )

    logging.info("=================================")
    logging.info("CHAIN BOT STARTED")
    logging.info("Webhook: %s", webhook_url)
    logging.info("=================================")


@app.after_serving
async def shutdown():

    await telegram_app.stop()
    await telegram_app.shutdown()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=PORT
    )
