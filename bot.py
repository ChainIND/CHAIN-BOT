import os
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# -----------------------------
# Logging
# -----------------------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# -----------------------------
# Environment
# -----------------------------
TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is missing.")

if not RENDER_EXTERNAL_URL:
    raise RuntimeError("RENDER_EXTERNAL_URL environment variable is missing.")

# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Telegram Application
# -----------------------------
telegram_app = Application.builder().token(TOKEN).build()


# -----------------------------
# Commands
# -----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to CHAIN Bot!\n\n"
        "🛠️ INDIAN JTAG TEAM\n\n"
        "Use /help to see available commands."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 CHAIN Bot Commands\n\n"
        "/start - Start bot\n"
        "/help - Help\n"
        "/status - Bot status"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 CHAIN Bot is Online!\n"
        "⚡ Status: Active"
    )


telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("help", help_command))
telegram_app.add_handler(CommandHandler("status", status))


# -----------------------------
# Health Check
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    return "CHAIN Bot is Online! 🟢", 200


@app.route("/health", methods=["GET"])
def health():
    return "OK", 200


# -----------------------------
# Telegram Webhook
# -----------------------------
@app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, telegram_app.bot)

    await telegram_app.process_update(update)

    return "OK", 200


# -----------------------------
# Start
# -----------------------------
async def setup_bot():
    await telegram_app.initialize()

    webhook_url = f"{RENDER_EXTERNAL_URL}/webhook"

    await telegram_app.bot.set_webhook(
        url=webhook_url
    )

    await telegram_app.start()

    logging.info("CHAIN Bot started!")
    logging.info("Webhook: %s", webhook_url)


if __name__ == "__main__":
    import asyncio

    asyncio.run(setup_bot())

    app.run(
        host="0.0.0.0",
        port=PORT
    )
