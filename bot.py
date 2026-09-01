import os
import logging

from quart import Quart, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

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


# ==========================================
# MAIN MENU
# ==========================================

def main_menu():

    keyboard = [
        [
            InlineKeyboardButton("🔧 ADB TOOLS", callback_data="adb"),
            InlineKeyboardButton("⚡ FASTBOOT", callback_data="fastboot")
        ],
        [
            InlineKeyboardButton("📱 SAMSUNG", callback_data="samsung"),
            InlineKeyboardButton("📂 FIRMWARE", callback_data="firmware")
        ],
        [
            InlineKeyboardButton("🛠️ DEVICE INFO", callback_data="device"),
        ],
        [
            InlineKeyboardButton("📢 UPDATES", callback_data="updates"),
            InlineKeyboardButton("👨‍💻 SUPPORT", callback_data="support")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================================
# START
# ==========================================

async def start(update: Update, context):

    text = (
        "👋 <b>Welcome to CHAIN Bot!</b>\n\n"
        "🛠️ <b>INDIAN JTAG TEAM</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "🤖 Select an option below\n"
        "━━━━━━━━━━━━━━━━━━"
    )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=main_menu()
    )


# ==========================================
# HELP
# ==========================================

async def help_command(update: Update, context):

    text = (
        "🤖 <b>CHAIN BOT HELP</b>\n\n"
        "Available Commands:\n\n"
        "▶️ /start - Main Menu\n"
        "▶️ /help - Help\n"
        "▶️ /status - Bot Status\n\n"
        "🛠️ Use the buttons to navigate the bot."
    )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=main_menu()
    )


# ==========================================
# STATUS
# ==========================================

async def status(update: Update, context):

    text = (
        "🟢 <b>CHAIN BOT STATUS</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "⚡ Status: <b>ONLINE</b>\n"
        "🌐 Server: <b>RENDER</b>\n"
        "🔗 Webhook: <b>ACTIVE</b>\n"
        "━━━━━━━━━━━━━━━━━━"
    )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=main_menu()
    )


# ==========================================
# CALLBACK HANDLER
# ==========================================

async def button_handler(update: Update, context):

    query = update.callback_query

    await query.answer()

    data = query.data


    # --------------------------------------
    # MAIN MENU
    # --------------------------------------

    if data == "menu":

        text = (
            "👋 <b>CHAIN BOT</b>\n\n"
            "🛠️ INDIAN JTAG TEAM\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "🤖 Select an option below\n"
            "━━━━━━━━━━━━━━━━━━"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=main_menu()
        )


    # --------------------------------------
    # ADB
    # --------------------------------------

    elif data == "adb":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📱 ADB COMMANDS",
                    callback_data="adb_commands"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔄 REBOOT",
                    callback_data="adb_reboot"
                ),
                InlineKeyboardButton(
                    "ℹ️ DEVICE INFO",
                    callback_data="adb_info"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="menu"
                )
            ]
        ]

        text = (
            "🔧 <b>ADB TOOLS</b>\n\n"
            "Android Debug Bridge Tools\n\n"
            "Select an option:"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # --------------------------------------
    # FASTBOOT
    # --------------------------------------

    elif data == "fastboot":

        keyboard = [
            [
                InlineKeyboardButton(
                    "⚡ FASTBOOT COMMANDS",
                    callback_data="fastboot_commands"
                )
            ],
            [
                InlineKeyboardButton(
                    "ℹ️ DEVICE INFO",
                    callback_data="fastboot_info"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="menu"
                )
            ]
        ]

        text = (
            "⚡ <b>FASTBOOT TOOLS</b>\n\n"
            "Fastboot device utilities\n\n"
            "Select an option:"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # --------------------------------------
    # SAMSUNG
    # --------------------------------------

    elif data == "samsung":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📱 DOWNLOAD MODE",
                    callback_data="download_mode"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔧 SAMSUNG TOOLS",
                    callback_data="samsung_tools"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="menu"
                )
            ]
        ]

        text = (
            "📱 <b>SAMSUNG TOOLS</b>\n\n"
            "Samsung device utilities\n\n"
            "Select an option:"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # --------------------------------------
    # FIRMWARE
    # --------------------------------------

    elif data == "firmware":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📦 FIRMWARE INFO",
                    callback_data="firmware_info"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔍 CHECK FIRMWARE",
                    callback_data="check_firmware"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="menu"
                )
            ]
        ]

        text = (
            "📂 <b>FIRMWARE TOOLS</b>\n\n"
            "Firmware utilities and information\n\n"
            "Select an option:"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # --------------------------------------
    # DEVICE INFO
    # --------------------------------------

    elif data == "device":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📱 ADB DEVICE INFO",
                    callback_data="adb_info"
                )
            ],
            [
                InlineKeyboardButton(
                    "⚡ FASTBOOT INFO",
                    callback_data="fastboot_info"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="menu"
                )
            ]
        ]

        text = (
            "🛠️ <b>DEVICE INFO</b>\n\n"
            "Choose device mode:"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # --------------------------------------
    # UPDATES
    # --------------------------------------

    elif data == "updates":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="menu"
                )
            ]
        ]

        text = (
            "📢 <b>CHAIN UPDATES</b>\n\n"
            "Latest updates will be available here.\n\n"
            "🛠️ INDIAN JTAG TEAM"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # --------------------------------------
    # SUPPORT
    # --------------------------------------

    elif data == "support":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="menu"
                )
            ]
        ]

        text = (
            "👨‍💻 <b>CHAIN SUPPORT</b>\n\n"
            "For support and assistance,\n"
            "contact INDIAN JTAG TEAM.\n\n"
            "🛠️ CHAIN TEAM"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # --------------------------------------
    # PLACEHOLDER PAGES
    # --------------------------------------

    elif data in [
        "adb_commands",
        "adb_reboot",
        "adb_info",
        "fastboot_commands",
        "fastboot_info",
        "download_mode",
        "samsung_tools",
        "firmware_info",
        "check_firmware"
    ]:

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="menu"
                )
            ]
        ]

        text = (
            "🚧 <b>FEATURE COMING SOON</b>\n\n"
            "This feature is currently under development.\n\n"
            "🛠️ <b>CHAIN BOT</b>\n"
            "INDIAN JTAG TEAM"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# ==========================================
# HANDLERS
# ==========================================

telegram_app.add_handler(
    CommandHandler("start", start)
)

telegram_app.add_handler(
    CommandHandler("help", help_command)
)

telegram_app.add_handler(
    CommandHandler("status", status)
)

telegram_app.add_handler(
    CallbackQueryHandler(button_handler)
)


# ==========================================
# WEB ROUTES
# ==========================================

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


# ==========================================
# STARTUP
# ==========================================

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


# ==========================================
# SHUTDOWN
# ==========================================

@app.after_serving
async def shutdown():

    await telegram_app.stop()

    await telegram_app.shutdown()


# ==========================================
# LOCAL RUN
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=PORT
    )
