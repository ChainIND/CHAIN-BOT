import os
import logging

from quart import Quart, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

# ==========================================
# LOGGING
# ==========================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ==========================================
# ENVIRONMENT
# ==========================================

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", "10000"))
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing")

if not RENDER_EXTERNAL_URL:
    raise RuntimeError("RENDER_EXTERNAL_URL is missing")

# ==========================================
# QUART
# ==========================================

app = Quart(__name__)

# ==========================================
# TELEGRAM APPLICATION
# ==========================================

telegram_app = Application.builder().token(TOKEN).build()


# ==========================================
# MAIN MENU
# ==========================================

def main_menu():

    keyboard = [
        [
            InlineKeyboardButton(
                "🔧 ADB TOOLS",
                callback_data="adb"
            ),
            InlineKeyboardButton(
                "⚡ FASTBOOT",
                callback_data="fastboot"
            )
        ],
        [
            InlineKeyboardButton(
                "📱 SAMSUNG",
                callback_data="samsung"
            ),
            InlineKeyboardButton(
                "📂 FIRMWARE",
                callback_data="firmware"
            )
        ],
        [
            InlineKeyboardButton(
                "🛠️ DEVICE INFO",
                callback_data="device"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 UPDATES",
                callback_data="updates"
            ),
            InlineKeyboardButton(
                "👨‍💻 SUPPORT",
                callback_data="support"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================================
# ADB MENU
# ==========================================

def adb_menu():

    keyboard = [
        [
            InlineKeyboardButton(
                "📱 DEVICE INFO",
                callback_data="adb_info"
            ),
            InlineKeyboardButton(
                "🔄 REBOOT",
                callback_data="adb_reboot"
            )
        ],
        [
            InlineKeyboardButton(
                "🔁 RECOVERY",
                callback_data="adb_recovery"
            ),
            InlineKeyboardButton(
                "⚡ BOOTLOADER",
                callback_data="adb_bootloader"
            )
        ],
        [
            InlineKeyboardButton(
                "📦 PACKAGE INFO",
                callback_data="adb_packages"
            )
        ],
        [
            InlineKeyboardButton(
                "🧹 APP DATA",
                callback_data="adb_appdata"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 BACK",
                callback_data="menu"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================================
# FIRMWARE MENU
# ==========================================

def firmware_menu():

    keyboard = [

        [
            InlineKeyboardButton(
                "🔎 SEARCH BY MODEL",
                callback_data="fw_search"
            )
        ],

        [
            InlineKeyboardButton(
                "🇰🇷 SAMSUNG",
                callback_data="fw_samsung"
            )
        ],

        [
            InlineKeyboardButton(
                "🇨🇳 XIAOMI",
                callback_data="fw_xiaomi"
            ),
            InlineKeyboardButton(
                "🇨🇳 REDMI",
                callback_data="fw_redmi"
            )
        ],

        [
            InlineKeyboardButton(
                "🇨🇳 POCO",
                callback_data="fw_poco"
            )
        ],

        [
            InlineKeyboardButton(
                "🇨🇳 REALME",
                callback_data="fw_realme"
            ),
            InlineKeyboardButton(
                "🇨🇳 OPPO",
                callback_data="fw_oppo"
            )
        ],

        [
            InlineKeyboardButton(
                "🇨🇳 VIVO",
                callback_data="fw_vivo"
            ),
            InlineKeyboardButton(
                "🇨🇳 iQOO",
                callback_data="fw_iqoo"
            )
        ],

        [
            InlineKeyboardButton(
                "🇨🇳 ONEPLUS",
                callback_data="fw_oneplus"
            ),
            InlineKeyboardButton(
                "🇺🇸 MOTOROLA",
                callback_data="fw_motorola"
            )
        ],

        [
            InlineKeyboardButton(
                "🇨🇳 TECNO",
                callback_data="fw_tecno"
            ),
            InlineKeyboardButton(
                "🇨🇳 INFINIX",
                callback_data="fw_infinix"
            )
        ],

        [
            InlineKeyboardButton(
                "🔙 BACK",
                callback_data="menu"
            )
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
        "📂 Firmware • ADB • Fastboot\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "🤖 Select an option below"
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
        "📂 Firmware model search available.\n"
        "🛠️ Use the buttons to navigate."
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
        "📂 Firmware: <b>AVAILABLE</b>\n"
        "━━━━━━━━━━━━━━━━━━"
    )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=main_menu()
    )


# ==========================================
# FIRMWARE MODEL SEARCH
# ==========================================

async def firmware_model_search(update: Update, context):

    # Only process text when search mode is active
    if not context.user_data.get("firmware_search"):
        return

    model = update.message.text.strip()

    if not model:
        return

    context.user_data["firmware_search"] = False

    model_upper = model.upper()

    # --------------------------------------
    # SAMSUNG
    # --------------------------------------

    if model_upper.startswith(
        (
            "SM-",
            "GT-",
            "SCH-",
            "SGH-",
            "SHV-",
            "SC-"
        )
    ):

        keyboard = [
            [
                InlineKeyboardButton(
                    "🇰🇷 OPEN SAMFW",
                    url="https://samfw.com/"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔎 SEARCH AGAIN",
                    callback_data="fw_search"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 FIRMWARE",
                    callback_data="firmware"
                )
            ]
        ]

        text = (
            "🇰🇷 <b>SAMSUNG FIRMWARE SEARCH</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            f"📱 Model: <code>{model_upper}</code>\n"
            "📦 Source: SamFW\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "SamFW firmware database supports "
            "model, CSC, firmware version and "
            "regional listings.\n\n"
            "👇 Open SamFW and search this model."
        )

    # --------------------------------------
    # XIAOMI / REDMI / POCO
    # --------------------------------------

    elif any(
        keyword in model_upper
        for keyword in [
            "XIAOMI",
            "REDMI",
            "POCO"
        ]
    ):

        keyboard = [
            [
                InlineKeyboardButton(
                    "🇨🇳 OPEN MIFIRM",
                    url="https://mifirm.net/"
                )
            ],
            [
                InlineKeyboardButton(
                    "⚡ FASTBOOT ROM",
                    url="https://mifirm.net/list/fastboot"
                )
            ],
            [
                InlineKeyboardButton(
                    "📦 ZIP ROM",
                    url="https://mifirm.net/list/zip"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔎 SEARCH AGAIN",
                    callback_data="fw_search"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 FIRMWARE",
                    callback_data="firmware"
                )
            ]
        ]

        text = (
            "🇨🇳 <b>XIAOMI / REDMI / POCO</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            f"📱 Model: <code>{model_upper}</code>\n"
            "📦 Source: MiFirm\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Available firmware categories:\n"
            "⚡ Fastboot ROM\n"
            "📦 ZIP / Recovery ROM\n"
            "🌍 Global / India / EEA / China etc.\n\n"
            "👇 Select the required firmware section."
        )

    # --------------------------------------
    # UNKNOWN
    # --------------------------------------

    else:

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔎 SEARCH AGAIN",
                    callback_data="fw_search"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 FIRMWARE",
                    callback_data="firmware"
                )
            ]
        ]

        text = (
            "❓ <b>MODEL NOT RECOGNIZED</b>\n\n"
            f"📱 Model: <code>{model_upper}</code>\n\n"
            "Currently automatic detection supports:\n\n"
            "🇰🇷 Samsung\n"
            "🇨🇳 Xiaomi\n"
            "🇨🇳 Redmi\n"
            "🇨🇳 POCO\n\n"
            "Please enter the exact model code."
        )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==========================================
# CALLBACK HANDLER
# ==========================================

async def button_handler(update: Update, context):

    query = update.callback_query

    await query.answer()

    data = query.data

    # ======================================
    # MAIN MENU
    # ======================================

    if data == "menu":

        text = (
            "👋 <b>CHAIN BOT</b>\n\n"
            "🛠️ <b>INDIAN JTAG TEAM</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "📂 Firmware • ADB • Fastboot\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "🤖 Select an option below"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=main_menu()
        )

    # ======================================
    # ADB
    # ======================================

    elif data == "adb":

        text = (
            "🔧 <b>ADB TOOLS</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "📱 Android Debug Bridge\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Select a tool:"
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=adb_menu()
        )

    # ======================================
    # ADB INFO
    # ======================================

    elif data == "adb_info":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔄 CHECK AGAIN",
                    callback_data="adb_info"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 ADB TOOLS",
                    callback_data="adb"
                )
            ]
        ]

        text = (
            "📱 <b>ADB DEVICE INFO</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "🔌 Connection: <b>NOT CONNECTED</b>\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "⚠️ No CHAIN ADB Agent connected.\n\n"
            "💡 This feature is currently unavailable."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # ADB REBOOT
    # ======================================

    elif data == "adb_reboot":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔄 CONFIRM REBOOT",
                    callback_data="confirm_reboot"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 ADB TOOLS",
                    callback_data="adb"
                )
            ]
        ]

        text = (
            "🔄 <b>ADB REBOOT</b>\n\n"
            "This command will reboot the connected "
            "Android device.\n\n"
            "⚠️ CHAIN ADB Agent is required."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # CONFIRM REBOOT
    # ======================================

    elif data == "confirm_reboot":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 ADB TOOLS",
                    callback_data="adb"
                )
            ]
        ]

        text = (
            "⚠️ <b>ADB AGENT NOT CONNECTED</b>\n\n"
            "The reboot command cannot be sent because "
            "no CHAIN ADB Agent is connected."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # ADB RECOVERY
    # ======================================

    elif data == "adb_recovery":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 ADB TOOLS",
                    callback_data="adb"
                )
            ]
        ]

        text = (
            "🔁 <b>ADB RECOVERY</b>\n\n"
            "⚠️ CHAIN ADB Agent is required.\n\n"
            "This feature will send the recovery reboot "
            "command to the connected device."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # ADB BOOTLOADER
    # ======================================

    elif data == "adb_bootloader":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 ADB TOOLS",
                    callback_data="adb"
                )
            ]
        ]

        text = (
            "⚡ <b>ADB BOOTLOADER</b>\n\n"
            "⚠️ CHAIN ADB Agent is required.\n\n"
            "This feature will reboot the connected "
            "device into bootloader mode."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # PACKAGE INFO
    # ======================================

    elif data == "adb_packages":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 ADB TOOLS",
                    callback_data="adb"
                )
            ]
        ]

        text = (
            "📦 <b>PACKAGE INFO</b>\n\n"
            "⚠️ CHAIN ADB Agent is required.\n\n"
            "This feature will retrieve installed "
            "Android package information."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # APP DATA
    # ======================================

    elif data == "adb_appdata":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 ADB TOOLS",
                    callback_data="adb"
                )
            ]
        ]

        text = (
            "🧹 <b>APP DATA</b>\n\n"
            "⚠️ CHAIN ADB Agent is required.\n\n"
            "This feature will allow supported app "
            "data operations through ADB."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # FASTBOOT
    # ======================================

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

    # ======================================
    # SAMSUNG TOOLS
    # ======================================

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

    # ======================================
    # FIRMWARE MENU
    # ======================================

    elif data == "firmware":

        context.user_data["firmware_search"] = False

        text = (
            "📂 <b>CHAIN FIRMWARE</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "📱 Select your device brand\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "🔎 You can also search directly "
            "by model number."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=firmware_menu()
        )

    # ======================================
    # START FIRMWARE SEARCH
    # ======================================

    elif data == "fw_search":

        context.user_data["firmware_search"] = True

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 FIRMWARE",
                    callback_data="firmware"
                )
            ]
        ]

        text = (
            "🔎 <b>FIRMWARE MODEL SEARCH</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "📱 Send your device model\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Examples:\n\n"
            "🇰🇷 Samsung\n"
            "<code>SM-S928B</code>\n\n"
            "🇨🇳 Xiaomi\n"
            "<code>23127PN0CG</code>\n\n"
            "🇨🇳 Redmi\n"
            "<code>2312DRA50I</code>\n\n"
            "🇨🇳 POCO\n"
            "<code>23122PCD1G</code>\n\n"
            "✍️ Now send the model code."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # SAMSUNG FIRMWARE
    # ======================================

    elif data == "fw_samsung":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🌐 OPEN SAMFW",
                    url="https://samfw.com/"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔎 SEARCH BY MODEL",
                    callback_data="fw_search"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 FIRMWARE",
                    callback_data="firmware"
                )
            ]
        ]

        text = (
            "🇰🇷 <b>SAMSUNG FIRMWARE</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "📦 Source: <b>SamFW</b>\n"
            "📱 Samsung firmware\n"
            "🔎 Search by model\n"
            "🌍 CSC / Region support\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Tap below to open the firmware source."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # XIAOMI FIRMWARE
    # ======================================

    elif data == "fw_xiaomi":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🌐 OPEN MIFIRM",
                    url="https://mifirm.net/"
                )
            ],
            [
                InlineKeyboardButton(
                    "⚡ FASTBOOT ROM",
                    url="https://mifirm.net/list/fastboot"
                )
            ],
            [
                InlineKeyboardButton(
                    "📦 ZIP ROM",
                    url="https://mifirm.net/list/zip"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 FIRMWARE",
                    callback_data="firmware"
                )
            ]
        ]

        text = (
            "🇨🇳 <b>XIAOMI FIRMWARE</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "📦 Source: <b>MiFirm</b>\n"
            "📱 Xiaomi firmware\n"
            "⚡ Fastboot ROM\n"
            "📦 Recovery / ZIP ROM\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Select firmware type."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # REDMI
    # ======================================

    elif data == "fw_redmi":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🌐 OPEN MIFIRM",
                    url="https://mifirm.net/"
                )
            ],
            [
                InlineKeyboardButton(
                    "⚡ FASTBOOT ROM",
                    url="https://mifirm.net/list/fastboot"
                )
            ],
            [
                InlineKeyboardButton(
                    "📦 ZIP ROM",
                    url="https://mifirm.net/list/zip"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 FIRMWARE",
                    callback_data="firmware"
                )
            ]
        ]

        text = (
            "🇨🇳 <b>REDMI FIRMWARE</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "📦 Source: <b>MiFirm</b>\n"
            "📱 Redmi firmware\n"
            "⚡ Fastboot ROM\n"
            "📦 Recovery / ZIP ROM\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Select firmware type."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # POCO
    # ======================================

    elif data == "fw_poco":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🌐 OPEN MIFIRM",
                    url="https://mifirm.net/"
                )
            ],
            [
                InlineKeyboardButton(
                    "⚡ FASTBOOT ROM",
                    url="https://mifirm.net/list/fastboot"
                )
            ],
            [
                InlineKeyboardButton(
                    "📦 ZIP ROM",
                    url="https://mifirm.net/list/zip"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 FIRMWARE",
                    callback_data="firmware"
                )
            ]
        ]

        text = (
            "🇨🇳 <b>POCO FIRMWARE</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "📦 Source: <b>MiFirm</b>\n"
            "📱 POCO firmware\n"
            "⚡ Fastboot ROM\n"
            "📦 Recovery / ZIP ROM\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "Select firmware type."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # OTHER BRANDS
    # ======================================

    elif data in [
        "fw_realme",
        "fw_oppo",
        "fw_vivo",
        "fw_iqoo",
        "fw_oneplus",
        "fw_motorola",
        "fw_tecno",
        "fw_infinix"
    ]:

        brand_names = {
            "fw_realme": "REALME",
            "fw_oppo": "OPPO",
            "fw_vivo": "VIVO",
            "fw_iqoo": "iQOO",
            "fw_oneplus": "ONEPLUS",
            "fw_motorola": "MOTOROLA",
            "fw_tecno": "TECNO",
            "fw_infinix": "INFINIX"
        }

        brand = brand_names.get(
            data,
            "DEVICE"
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 FIRMWARE",
                    callback_data="firmware"
                )
            ]
        ]

        text = (
            f"📱 <b>{brand} FIRMWARE</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "🚧 Source integration is coming soon.\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "CHAIN Team will add a firmware "
            "source for this brand."
        )

        await query.edit_message_text(
            text,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ======================================
    # DEVICE INFO
    # ======================================

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

    # ======================================
    # UPDATES
    # ======================================

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

    # ======================================
    # SUPPORT
    # ======================================

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

    # ======================================
    # PLACEHOLDER
    # ======================================

    elif data in [
        "fastboot_commands",
        "fastboot_info",
        "download_mode",
        "samsung_tools"
    ]:

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 MAIN MENU",
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
# TELEGRAM HANDLERS
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
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        firmware_model_search
    )
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
